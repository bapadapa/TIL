from hr.models import Job
from django.shortcuts import render

# Create your views here.
def  list_jobs (request):
    return render(request,'list_jobs.html',{'jobs' : Job.objects.all()})
