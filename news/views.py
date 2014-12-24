from django.shortcuts import render
from news.models import News
from news.models import NewsLetter
from news.models import Calendar
from datetime import date

# Create your views here.
def index(request):

	calendarJSON = calendarParse(Calendar.objects.all())



	context = {'news_': News.objects.all(),
				'newsLetter_':NewsLetter.objects.last(),
				'calendar_':calendarJSON
				}

	return render(request, 'news_index.html', context)


def calendarParse(allEvents):
	totalStr = "defaultDate: '" + str(date.today()) + "',"
	totalStr += "events: [ "

	for each in allEvents:
		totalStr += "{ title: '" + each.calendar_event_title + "',"
		totalStr += "start: '" + each.calendar_event_start + "',"
		totalStr += "end: '" + each.calendar_event_end[:-2]+str(int(each.calendar_event_end[-2:])+1) + "' },"

	totalStr = totalStr[:-1] + " ]"

	return totalStr