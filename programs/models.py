from django.db import models

# Create your models here.
class Curriculum(models.Model):
	curriculum_month = models.CharField(max_length=15)
	curriculum_letters = models.CharField(max_length=26)

	curriculum_unit = models.TextField()
	curriculum_cognitive = models.TextField()
	curriculum_motor = models.TextField()

	def __unicode__(self):
		return self.curriculum_month


class Schedules(models.Model):
	schedules_day = models.TextField()
	schedules_age = models.TextField()

	def __unicode__(self):
		return self.schedules_day


class Tuition(models.Model):
	tuition_schedule = models.TextField()
	tuition_yearly = models.TextField()
	tuition_monthly = models.TextField()

	def __unicode__(self):
		return self.tuition_schedule

class AdmissionsCal(models.Model):
	admissionsCal_item = models.TextField()

	def __unicode__(self):
		return self.admissionsCal_item[:10]


class ParentInfo(models.Model):
	parentInfo_item = models.TextField()

	def __unicode__(self):
		return self.parentInfo_item[:10]