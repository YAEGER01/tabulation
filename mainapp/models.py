from django.db import models


class EsLogUser(models.Model):
    username = models.CharField(max_length=50, blank=True)
    action = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'esloguser'


class JudgeApproval(models.Model):
	approved = models.BooleanField(default=False)
	class Meta:
		db_table = 'judgeapproval'


class Event(models.Model):
    evdes = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = 'event'


class Resnoshow(models.Model):
	noshow = models.IntegerField(default=0)
	class Meta:
		db_table = 'resnoshow'


class Rescri(models.Model):
	evid = models.IntegerField(null=True, blank=True)
	scri = models.IntegerField(null=True, blank=True)
	inscore = models.FloatField(default=0)
	class Meta:
		db_table = 'rescri'

class Candidate(models.Model):
    cano = models.IntegerField(null=True, blank=True)
    cname = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'candidate'


class Criteria(models.Model):
    ctitle = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'criteria'


class Judge(models.Model):
	jname = models.CharField(max_length=100, blank=True)
	uname = models.CharField(max_length=100, blank=True)
	event = models.ForeignKey('Event', on_delete=models.CASCADE, null=True, blank=True)
	class Meta:
		db_table = 'judge'


class Score(models.Model):
    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE, null=True, blank=True)
    value = models.FloatField(default=0)
    class Meta:
        db_table = 'score'


class Gradminpas(models.Model):
	username = models.CharField(max_length=50, blank=True)
	spassword = models.CharField(max_length=128, blank=True)
	class Meta:
		db_table = 'gradminpas'


class Gradinsname(models.Model):
	fname = models.CharField(max_length=50, blank=True)
	lname = models.CharField(max_length=50, blank=True)
	ulevel = models.CharField(max_length=5, blank=True)
	class Meta:
		db_table = 'gradinsname'


class Judgesapproved(models.Model):
	name = models.CharField(max_length=100, blank=True)
	class Meta:
		db_table = 'judgesapproved'


class Approval(models.Model):
    approved = models.BooleanField(default=False)
    class Meta:
        db_table = 'approval'

class SAdmin(models.Model):
	userid = models.AutoField(primary_key=True)
	username = models.CharField(max_length=50, null=True, blank=True)
	userlevel = models.CharField(max_length=5, null=True, blank=True)
	uname = models.CharField(max_length=50, null=True, blank=True)
	spassword = models.BinaryField(null=True, blank=True)

	class Meta:
		db_table = 'sadmin'

class Scorevents(models.Model):
	evid = models.AutoField(primary_key=True)
	evdes = models.CharField(max_length=150, null=True, blank=True)

	class Meta:
		db_table = 'scorevents'

class SJudge(models.Model):
	ejid = models.AutoField(primary_key=True)
	evid = models.ForeignKey(Scorevents, on_delete=models.RESTRICT, null=True, blank=True, db_column='evid')
	jname = models.CharField(max_length=100, null=True, blank=True)
	uname = models.CharField(max_length=30, null=True, blank=True)
	category = models.CharField(max_length=20, null=True, blank=True)
	spassword = models.BinaryField(null=True, blank=True)

	class Meta:
		db_table = 'sjudge'

class Scri(models.Model):
	scri = models.AutoField(primary_key=True)
	ctitle = models.CharField(max_length=50, null=True, blank=True)
	cper = models.IntegerField(null=True, blank=True)
	evid = models.ForeignKey(Scorevents, on_delete=models.RESTRICT, null=True, blank=True, db_column='evid')
	category = models.CharField(max_length=20, null=True, blank=True)
	status = models.CharField(max_length=2, null=True, blank=True)
	minrate = models.CharField(max_length=4, null=True, blank=True)

	class Meta:
		db_table = 'scri'

class SCandidates(models.Model):
	sconid = models.AutoField(primary_key=True)
	evid = models.ForeignKey(Scorevents, on_delete=models.RESTRICT, null=True, blank=True, db_column='evid')
	ejid = models.ForeignKey(SJudge, on_delete=models.RESTRICT, null=True, blank=True, db_column='ejid')
	cano = models.IntegerField(null=True, blank=True)
	cname = models.CharField(max_length=100, null=True, blank=True)
	course = models.CharField(max_length=10, null=True, blank=True)
	category = models.CharField(max_length=20, null=True, blank=True)
	canstatus = models.CharField(max_length=2, null=True, blank=True)

	class Meta:
		db_table = 'scandidates'

class Sinscore(models.Model):
	id = models.AutoField(primary_key=True)
	sconid = models.ForeignKey(SCandidates, on_delete=models.RESTRICT, null=True, blank=True, db_column='sconid')
	evid = models.ForeignKey(Scorevents, on_delete=models.RESTRICT, null=True, blank=True, db_column='evid')
	ejid = models.ForeignKey(SJudge, on_delete=models.RESTRICT, null=True, blank=True, db_column='ejid')
	scri = models.ForeignKey(Scri, on_delete=models.RESTRICT, null=True, blank=True, db_column='scri')
	inscore = models.CharField(max_length=6, default='0', null=True, blank=True)
	category = models.CharField(max_length=20, null=True, blank=True)
	subdon = models.CharField(max_length=2, default='0', null=True, blank=True)
	cristat = models.CharField(max_length=2, null=True, blank=True)
	rankscore = models.SmallIntegerField(default=0, null=True, blank=True)

	class Meta:
		db_table = 'sinscore'

class Resall(models.Model):
	sconid = models.IntegerField(null=True, blank=True)
	evid = models.IntegerField(null=True, blank=True)
	ejid = models.IntegerField(null=True, blank=True)
	scri = models.IntegerField(null=True, blank=True)
	inscore = models.CharField(max_length=6, null=True, blank=True)
	category = models.CharField(max_length=20, null=True, blank=True)

	class Meta:
		db_table = 'resall'

class Rescri(models.Model):
	sconid = models.IntegerField(null=True, blank=True)
	evid = models.IntegerField(null=True, blank=True)
	ejid = models.IntegerField(null=True, blank=True)
	scri = models.IntegerField(null=True, blank=True)
	inscore = models.CharField(max_length=6, null=True, blank=True)
	category = models.CharField(max_length=20, null=True, blank=True)

	class Meta:
		db_table = 'rescri'

class Resnoshow(models.Model):
	noshow = models.CharField(max_length=3, null=True, blank=True)

	class Meta:
		db_table = 'resnoshow'

class Judgesapproved(models.Model):
	ejid = models.IntegerField(null=True, blank=True)
	evid = models.IntegerField(null=True, blank=True)
	sconid = models.IntegerField(null=True, blank=True)
	aprem = models.CharField(max_length=2, null=True, blank=True)

	class Meta:
		db_table = 'judgesapproved'

class Judgecriteria(models.Model):
	ejid = models.IntegerField(null=True, blank=True)
	scri = models.IntegerField(null=True, blank=True)

	class Meta:
		db_table = 'judgecriteria'
