from django.shortcuts import render
from home.models import About

# Create your views here.
def index(request):

	context = {'about_': About.objects.all()}

	return render(request, 'home_index.html', context)