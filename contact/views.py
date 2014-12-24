from django.shortcuts import render
from django.http import HttpResponseRedirect
from contact.models import Faculty
import subprocess

# Create your views here.
def index(request):

	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		comment = request.POST['comment']

		f = open('/tmp/tmp.txt','w')
		f.write("From: ElfSchool\nSubject: Elf School Question/Comment!!\nName - %s\nEmail - %s\n\n%s\n" % (name, email, comment))
		f.close()
		subprocess.call(["contact/mailTo.sh"])

		return HttpResponseRedirect('/contact/')


	context = {
				'faculty_':Faculty.objects.all(),
				}


	return render(request, 'contact_index.html', context)