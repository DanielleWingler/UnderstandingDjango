UnderstandingDjango
===================

Generic basic code with precise understandable documentation to get a django site up and running.


This repository is beginner focused and assumes that there is no prior coding experience. There is a requirement of having python already installed and a command prompt (terminal) working in ubuntu.

This code and information is based on the django 1.6 version. The official documentation can be found at ![django project website](https://www.djangoproject.com/).

The newest and constantly changing django version can be gotten from the ![djano repo](https://github.com/django/django).

The code presented in this repo will automatically be created when you create your first project. However we have placed comments throughout the code that will help in determining what the code does and how it should be changed for certain purposes. The file structure in the repo represents the actual file structure created on your computer when you initiate the site. 

All you need to do once you have python and django 1.6 installed is type:

```
django-admin.py startproject TestSite

```
We decided to go with the name TestSite in this repo, but you can name it whatever you like.

```
cd TestSite
python manage.py runserver

```
Open a browser and type in http://127.0.0.1:8000/ (not a link-- copy and paste into browser after running code in terminal).

You have a locally hosted django site.

The below screenshot is what the index page looks like. This is what it should look like when you go directly to 
http://127.0.0.1:8000/ and have started the runserver code successfully in a terminal.

![This is a photo of the site](http://i.imgur.com/kPMJMnS.png)

The below screenshot is of the admin back-end of the above site. You can access it by going to http://127.0.0.1:8000/admin/

![This is a photo of the site](http://i.imgur.com/764q4WN.png)

The belowscreenshot is what it looks like once you logged in from the page above. This is where the creation of the
blog posts happen. The username and password is created during the process of the admin creation when starting a 
django project.

![This is a photo of the site](http://i.imgur.com/WY46MZB.png)

The main inspiration for this repo came from a blog called Creative Bloq. There is a post created called Get started with Django. It can be found at http://www.creativebloq.com/netmag/get-started-django-7132932. It provides a written step-by-step creation, but there are a few syntax errors and code left out that is addressed and included in this repo.
