#Web Hosting a Django Site

Unlike jekyll, Django cannot be hosted by github.

Most django web host, you have to pay for either monthly or annually. However, there are few that will allow you to host your site for free within a limited scope (generally based on site activity).

Those sites with free hosting availability including:

*Python Anywhere:  [pythonanywhere.com](https://www.pythonanywhere.com/pricing/)
NOTE: They will support sqlite. The free version is pretty limited in scope, but the hacker version for a flat $5 a month adds a little bit more functionality. 

*Heroku: [devcenter.heroku.com](https://devcenter.heroku.com/articles/getting-started-with-django)
NOTE: Heroku does not support SQL lite, so you will need to re-configure your database. Their database is postgres. They also have some paid components.

To pay for web hosting, visit django project site [here.] (https://code.djangoproject.com/wiki/DjangoFriendlyWebHosts)

###Recommendations for choosing a hosting site:

(1) Map out the functionalities you want your database to have and then assess your options.

(2) Understand the versions/types of each component you are using -- django, python, database.  Read about the different versions and don't always assume the newest version is the best.  Also, make sure whatever site you choose to host to can support all of the decisions you have made on software versions and database types.

(3) Decide whether its better to build your site locally and then connect it to a hosting site, or if it is easier to build the site with the tools provided by the site. For example, anywherepython has a built-in console, so you can code directly on their web interface. Plus you can share that console with another user. 
