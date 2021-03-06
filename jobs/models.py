from django.db import models


# Create your models here.
class Job(models.Model):

    # images
    # image of type imagefield accepts types of photos, puts it into a file called images 
    image = models.ImageField(upload_to='images/')
    # summary
    # how long the summary is
    summary = models.CharField(max_length=200) 

    # discription
    # when pressing on the links
    description = models.CharField(max_length=10000, default='defualt')
    def __str__(self):
        return self.summary

   
  
