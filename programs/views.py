from django.shortcuts import render
from programs.models import Curriculum
from programs.models import Schedules
from programs.models import Tuition
from programs.models import AdmissionsCal
from programs.models import ParentInfo

# Create your views here.
def index(request):

	context = { 'curriculum_':Curriculum.objects.all(),
				'schedules_':Schedules.objects.all(),
				'tuition_':Tuition.objects.all(),
				'admissionsCal_':AdmissionsCal.objects.all(),
				'parentInfo_':ParentInfo.objects.all(),
				}

	return render(request, 'programs_index.html', context)