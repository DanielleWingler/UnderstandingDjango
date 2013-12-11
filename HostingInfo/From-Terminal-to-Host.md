#From Terminal Set-Up to PythonAnywhere.com

We decided to try to use Pythonanywhere.com to host the test site since it supports sqlite, which our site uses. However, it is important to note that we had to get an account for $5 a month in order to have SSH access to the account.

This section goes over several key tasks discussed in class, including:

*Basic python programming

*Commandline posts to github.com

*SSH

*Cloning a Github Repository

Pythonanywhere.com allows you to build your Django site directly from their site.  They have an virtualenvironment that allows you to write code, and you can share that environment with others. 

However, you can also create the Django site locally and then push the files to github or dropbox and the pull those files into a directory on pythonanywhere.com.  This is very similar to the jekyll-github model learned in class.

Listed below are the steps we've been taking to get the website from terminal to github to pythonanywhere. [This link](https://drive.google.com/file/d/0BylRKPHp7PBCd1hjWkZrb3cyaDA/edit?usp=sharing) will take you to a document that gives screenshots of this process to date. 

##Build Django Site Locally

First and foremost, we used the following sources to help us build the website in the Ubuntu terminal:

(1) [Creative Bloq's Get Started with Django](http://www.creativebloq.com/netmag/get-started-django-7132932).  Note, there are some small programming errors in this example, so read it carefully.

(2) [Django's Documentation](9https://docs.djangoproject.com/en/1.6/) is really good. It covers a lot of material, which can be good, and daunting. 

The link above provides screenshots of what the basic site will look like. 

##Push Site Files to Github

Once you have it hosting locally, you can push it to github.com.  I folllowed my blog post on how to do this from an earlier class. That blg post can be found here: ["How I made this happen through the command line"](http://silshack.github.io/fall2013/2013/10/14/something-unique-post.html) 

As you make changes, you can push them github to keep track of changes.

## Set-Up Pythonanywhere.com / SSH Install

Pythonanywhere has varying degrees of accounts.  They have a free option that will support one python application, such as a djago site.  It also will support Flask.  The free option will not give you SSH access. However, the $5 a month "Hacker version" will, and you can cancel it at anytime. 

One nice thing about pythonanywhere is that it allows you to use their console to write python code. Plus, you can share this console with another person, which is particularly useful when you run into trouble and need someone to look at your code.

From your terminal, you can acccess pythonanywhere by accessing through SSH.  This [file](https://drive.google.com/file/d/0BylRKPHp7PBCd1hjWkZrb3cyaDA/edit?usp=sharing) shows screenshot with specific code on how to do this. Also, pythonanywhere has great documentation on how to do this [here.](https://www.pythonanywhere.com/wiki/SSHAccess)

##Configure Your WSGI File

There is a tab in anywherepython.com where you will need to add your new folder paths so that the site knows where to read your files. 

##Next Milestone: Figure Out Configuration

To date, the contributors have had some issues with the configuration and have spent (many) hours trying to fix this. I believe the problem is the result of some faulty original code, which pythonanywhere is having trouble reading. For future reference, it may be easier to just build a site directly in pythonanywhere's web console. 


