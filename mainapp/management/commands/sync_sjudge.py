from django.core.management.base import BaseCommand
from django.db import transaction
from mainapp.models import Judge, SJudge, Scorevents
import hashlib


class Command(BaseCommand):
    help = 'Sync existing Judge rows into legacy SJudge rows so judges can log in. Default is dry-run. Use --apply to perform changes.'

    def add_arguments(self, parser):
        parser.add_argument('--apply', action='store_true', help='Apply changes (create missing SJudge rows).')

    def handle(self, *args, **options):
        apply_changes = options.get('apply', False)
        judges = Judge.objects.all()
        created = []
        skipped = []

        self.stdout.write('Scanning %d Judge rows...' % judges.count())

        for j in judges:
            uname = (j.uname or '').strip()
            jname = (j.jname or '').strip()
            event = j.event
            # Try to find matching Scorevents by pk or by evdes if available
            scorevent = None
            if event is not None:
                # If Event has same PK as Scorevents, try direct lookup
                try:
                    scorevent = Scorevents.objects.get(pk=event.pk)
                except Scorevents.DoesNotExist:
                    # Fallback: try matching by description if available
                    evdes = getattr(event, 'evdes', None)
                    if evdes:
                        scorevent = Scorevents.objects.filter(evdes=evdes).first()

            # Build intended uname; skip if uname empty
            if not uname:
                skipped.append((j.pk, 'empty_uname'))
                continue

            exists = SJudge.objects.filter(uname=uname).exists()
            if exists:
                skipped.append((j.pk, 'exists'))
                continue

            # Prepare spassword: use md5 of uname (or jname) to generate a deterministic default
            seed = uname.encode('utf-8')
            md = hashlib.md5(seed).hexdigest().encode('utf-8')

            self.stdout.write('Will create SJudge for Judge.pk=%s uname=%s event=%s' % (j.pk, uname, getattr(scorevent, 'evid', None)))

            if apply_changes:
                with transaction.atomic():
                    sj = SJudge()
                    if scorevent is not None:
                        sj.evid = scorevent
                    sj.jname = jname or uname
                    sj.uname = uname
                    sj.category = getattr(j, 'category', '') or ''
                    sj.spassword = md
                    sj.save()
                    created.append(sj.pk)

        self.stdout.write('\nSummary:')
        self.stdout.write('  To be created: %d' % len(created) if apply_changes else '  Would create: %d' % (len(created) if created else 'unknown until --apply'))
        self.stdout.write('  Skipped: %d' % len(skipped))
        if skipped:
            for s in skipped[:50]:
                self.stdout.write('    %s' % (s,))

        if apply_changes:
            self.stdout.write('\nCreated SJudge IDs: %s' % (created,))
        else:
            self.stdout.write('\nDry-run complete. Re-run with --apply to create missing SJudge rows.')
