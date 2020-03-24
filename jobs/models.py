from django.db import models

# Create your models here.
class Job(models.Model):


    # images
    image = models.ImageField(upload_to='images/') #image of type imagefield accepts types of photos, puts it into a file called images 
    # summary
    summary= models.CharField(max_length=200) #how long the summary is 

    def __str__(self):
        return self.summary