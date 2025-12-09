

from django.db import models

class Score(models.Model):
    value = models.IntegerField(default=0)

class Candidate(models.Model):
    name = models.CharField(max_length=100, blank=True)



class Criteria(models.Model):
    name = models.CharField(max_length=100, blank=True)

class Event(models.Model):
    name = models.CharField(max_length=100, blank=True)

class Judge(models.Model):
    name = models.CharField(max_length=100, blank=True)

class JudgeCriteria(models.Model):
    judge = models.ForeignKey(Judge, on_delete=models.CASCADE)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
