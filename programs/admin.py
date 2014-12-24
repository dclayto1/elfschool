from django.contrib import admin

# Register your models here.
from programs.models import Curriculum
admin.site.register(Curriculum)

from programs.models import Schedules
admin.site.register(Schedules)

from programs.models import Tuition
admin.site.register(Tuition)

from programs.models import AdmissionsCal
admin.site.register(AdmissionsCal)

from programs.models import ParentInfo
admin.site.register(ParentInfo)