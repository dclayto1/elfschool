from django.db import models

# Create your models here.
class Faculty(models.Model):
	faculty_firstName = models.CharField(max_length=20)
	faculty_lastName = models.CharField(max_length=20)
	faculty_position = models.CharField(max_length=20)
	faculty_email = models.TextField()

	def __unicode__(self):
		return self.faculty_firstName + " " + self.faculty_lastName