from django.shortcuts import render, get_object_or_404
from .models import Project


# Create your models here.
def homeproj(request):

    # gets all job obvjects from database
   
    projects = Project.objects

    # goes to templates/jobs/then html file
    # pass in above data we want into the home.html file to be used
    return render(request, 'projects/homeproj.html', {'projects': projects})

def projdetail(request, proj_id):

    project_detail = get_object_or_404(Project, pk=proj_id)

    return render(request, 'projects/pdetail.html', {'project': project_detail})
    