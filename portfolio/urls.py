"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import jobs.views
#for static 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # is sent to the correspoding folder, jobs.view.home
    path('', jobs.views.home, name='home'),
    # this path, they input a number after and it is stored as job_id
    # and this goes to jobs.view.detail, and the name is detail for this 
    path('jobs/<int:job_id>', jobs.views.detail, name='detail')
    
] 
#this below is all adding paths when using static files and media files in this case 

# things you want to use when showing static files^^
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#upload the image that corresponds to the summary
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

