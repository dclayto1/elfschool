from django.db import models

# Create your models here.
class About(models.Model):
	about_title = models.CharField(max_length=50)

	about_text = models.TextField()

	def __unicode__(self):
		return self.about_title