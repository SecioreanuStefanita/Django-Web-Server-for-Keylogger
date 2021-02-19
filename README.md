# Django-Web-Server-for-Keylogger
# Disclaimer: This is the Server part of my python project:FOR PART 1 CHECK Python-Keylogger Repo


# How to Use
Download the server files. Entre with Windows powerShell in the project folder 
First make sure to change the settings for the mySQL DB in settings.py with your mySQL connection 
In the Windows PowerShell write the following commands to make the migrations to the DB,  activate the env and run the server:
• /Scripts/env/activate
• cd KeyloggerServer
• python manage.py migrate
• python manage.py makemigrations 
• python manage.py runserver

After all this steps you just run the external script from the Python-Keylogger Repo and every minute the keys are sent to the server and stored in the DB. You can see them in the Infected PCS page and for all the info press the See Logs button. 

# What I Learned
• Working with Django framework for web-dev

• Processing GET and POST requests 

• Working with dictionaries for data processing

• Working with mySQL in a python env, making migrations 
