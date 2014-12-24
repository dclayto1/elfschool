from django.db import models

# Create your models here.
class News(models.Model):
	news_item = models.TextField()

	def __unicode__(self):
		return self.news_item[:10]


class NewsLetter(models.Model):
	newsLetter_file = models.CharField(max_length=50)

	def __unicode__(self):
		return self.newsLetter_file


class Calendar(models.Model):
	calendar_event_title = models.TextField()
	calendar_event_start = models.CharField(max_length=10)
	calendar_event_end = models.CharField(max_length=10)

	def __unicode__(self):
		return self.calendar_event_title
