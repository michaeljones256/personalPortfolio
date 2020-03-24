from django.shortcuts import render, get_object_or_404
#import model we want 
from .models import Job 
# Create your views here.
def home(request):

    # gets all job obvjects from database
    jobs = Job.objects

    # goes to templates/jobs/then html file
    # pass in above data we want into the home.html file to be used
    return render(request, 'jobs/home.html', {'jobs': jobs})

def detail(request, job_id):
    # job_id from the request /jobs/#job_id# 

    # every model has a pk, primary key, each addtional model is pk+=1 and starts at 1
    # if this case is true its equal to job_detail or it spits a 404 error (if there is a job_id that meets some pk)
    job_detail = get_object_or_404(Job, pk=job_id)
    # pass in the key word in the hmtl file 'jobs' to be equal to the value of job_detail
    return render(request, 'jobs/detail.html', {'job': job_detail})
