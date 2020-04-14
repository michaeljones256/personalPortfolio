
    Trying to keep a log for future reference 3/19
# Portfolio/django basics
  - Overall built in Django format to follow which is nice
  - Database implemantation/ {sqlite} without a server, store the information used locally that will be implimented on the web site
  - Url matching inputs to the views
  - access sqlite from windows power shell
  - there can be multiple 'jobs'(in this case) folders on a single django project, you can categorize things differently but the urls.py is over arching and implements all folders that are similar to 'jobs' and they should all provide something different to the website, the url page talks to views in each of these 'jobs' folders through their corresponding path(SEE urls.py for proof, there can be multiple 'jobs' folders for more complex websites)
  -

## Database(sqlite)
  - in powershell type ```sqlite FILENAME.db``` for creating a database, and then type ```.databases``` for it to be set in your documents
  - Migrations is a way to set up a databases for a project
    - jobs/models.py, this is the data types the database will store, and in order for this to happen we have to set up a migration 
    - ```python manage.py makemigrations``` (run anytime you make a new model or you make changes to a model)- this will add new migration
    - ```python manage.py migrate``` run through migrations and get the sqlite database all set up, when you run server there should be no migration warnings and ready to save things into database through django
    - set up admin account, ```python manage.py createsuperuser```, then you can now go to the /admin for the link and add data to data base and such

## Output, views.py, and HTML
   - import your models to the views.py, get the objects from that import and you can pass them to the HTML file  
   - the website is totally based off the database so it will update the website as soon as you update the database on the admin site
   - to be able to see more information about a given job or project on this site 
     -  set up another view called detail
     -  update the urls.py to match a path to this view
     -  make a details.html because it will be a new webpage and copy code from html and revise
     -  the details.html will hold detailed information about a job or project, and it will import this detailed information from the datebase as well
     -  NOTE: using {{}} for when your using an information that has been passed to that html template, you use {%%} for other things (good example in details.html for the difference)

## Style
  - bootstrap for a template and then import their css and js in their source code so it displays as it should
    - Update the source code to your liking
  - with static files(in this case a picture of myself) you have to change the settings.py to show the path to these images, and then change the url.py for this as well
    - need static files to be collective before use so always run ```python manage.py collectstatic``` when adding static files
  - Download bootstrap css and js so there are no links in our code and it can run without internet, also used popper.js and jquery.js
    - Put these css folder and js fodler and popper.js and jquery.js files in the "static" folder, and re collect them
    - this alows you to change the pervious bootstrap "stylesheet" and the ending scripts on the bottom in the home.html, as a result you have these script tags pointing to local files which is good
      - the advantage to this is you are not dependent on their websites and are no suspect of malicious code because you downloaded there documentation
  - add media__url and media_root in settings to be able to display the corresponding picture to each summary on home.html
    - see code for this in url.py, setting.py, home.html
