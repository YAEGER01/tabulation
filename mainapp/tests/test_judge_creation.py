from django.test import TestCase, Client
from mainapp.models import Event, SJudge


class JudgeCreationTest(TestCase):
    def setUp(self):
        # create an event to assign the judge to
        self.event = Event.objects.create(evdes='Test Event')
        self.client = Client()

    def test_admin_can_create_judge_and_sjudge_record(self):
        # Simulate admin session (views check for 'logid' and 'ctrlid')
        session = self.client.session
        session['logid'] = 1
        session['ctrlid'] = 1
        session.save()

        post_data = {
            'txtname': 'Judge Test',
            'txtuname': 'judgetest',
            'optevent': str(self.event.pk),
            'txtpassword': 'secret123',
        }

        response = self.client.post('/admin/judgelist/', post_data, follow=True)
        # After creation, the view redirects back to judgelist; ensure no server error
        self.assertIn(response.status_code, (200, 302))

        # Verify SJudge record exists for the created username
        sj = SJudge.objects.filter(uname='judgetest').first()
        self.assertIsNotNone(sj, 'SJudge login row was not created')
