from django.contrib import admin

# Register your models here.
from news.models import News
admin.site.register(News)

from news.models import NewsLetter
admin.site.register(NewsLetter)

from news.models import Calendar
admin.site.register(Calendar)