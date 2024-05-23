![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for Codeanywhere. If you are using Gitpod then you need [this template](https://github.com/Code-Institute-Org/gitpod-full-template) instead.  We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **August 30th, 2023**

## GitPod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.


To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

Happy coding!

### Game Together

## Introduction

# Visit the Website Here

# Visit the Project's GitHub Repository Here
[](https://github.com/DoubleARon96/project-4-gamer-group)

# Responsive Image

# Website Highlights


## UX
the UX is a main part of the site by making it simple and easy to understand parts of the ux are 
* Strategy
* Scope
* Structure
* Skeleton
* Surface

# Strategy
![frameplan](/workspace/project-4-gamer-group/assests/readme_images/plan-data-a.png)

![rough-plan](/workspace/project-4-gamer-group/assests/readme_images/rough-plan.jpg)

When planning the site I could relate to the group i am aiming to draw in.

so when planning i thought about how i struggle to play groupe games now because all my friends have different hours, so i thought if i could make a site that can be assessed at anytime and responses don't have to be instant.

Target audience :
* 18 to 50 years old 
* people that are working full time and have not a lot of spare time.
* people that like to game in groups 


# Purpose
the purpose of this website it to be able to bring people together in a controlled and monitored way while gaming.
the plan is to make it easier for people like me that don't have much spare time to game and when they do they cant find anyone to play with, so with this i added functions to the site so that admins and superusers can make sessions and only registered people can join for extra protection.

# User Stories

# For the Future
the future i plan to add more interactivity like an voice chat to the sessions the users will be able to post images from games and have a profile with a logo or profile picture.
Scope


# Structure

# Project Applications

# Project Databases
![db_plan](assests/readme_images/plan-data-c.png)
this was my origanl plan for the data bases but lack of time i have streamlimed the data bases to fit into one.

# Accounts 
the accounts are the authentication so users can get around the site and if they dont meet the requirements they wont be able to get around the site.

# Posts/Sessions
within this it will hold the users data that made it and will have players that leave questions in the question part, it will also store the game , the amount of players and a brief description of what the host has planned 

# Surface

# Font
sadly I haven't added a basic font to the website.

# Icons
Icons i used where from font awesome

# Colours
i choose the green white and black because the glow makes it feels more game like and simple colours so its not hard to see or read the text 

# Responsive Screens
i made the site responsive with the help of bootstrap because of the columns and being able to make it fit the page no matter what screen the user is using.

# Features

  # Landing Page

  # Navigation Bar

  # Questions

# Django Template Pages
 
Error Pages
Technologies Used
Languages
Tools
Styling
Validation
Databases
Testing
Code Validation
W3C HTML Validator

Only Attempt of the Django Templates

W3C CSS Validator
First Attempt of CSS Files

Final Attempt of JavaScript Files
Python Syntax Checker PEP8 Validation
First Attempt of Python Files
Final Attempt of Python Files
Lighthouse
Final Attempt for Lighthouse
Responsiveness
Web Aim Contrast Checker

Manual Testing
Automated Testing
Bugs
Resolved
Unresolved
Deployment
Create Application
ElephantSQL
Cloudinary ??
Final Repo Preparations
Heroku Deploy
Credits
For Code Help and Advice
Helpful Resources
For Content and Code
 
UX
User Experience of UX focuses on how accessible the website is to the user and it’s ease of use, which is pivotal the website’s success.

Therefore, the UX aspect of the project can be broken down into 5 Planes:

The Strategy Plane
The Scope Plane
The Structure Plane
The Skeleton Plane
The Surface Plane
 
Strategy
In order to ensure the project aligns with these planes, it is vital to keep the target audience at the forefront at all times. It is vital to ensure that the project has real world use and that its design is transferrable to other sports events which also require the user to book a ticket.

The target audience consists of:

25 – 45 year olds.

Purpose

 

User Stories


 

For Future Sprints

 

Scope



Structure


Project Applications

Project Databases


Database Tables
 

WebsiteUser


It can be broken down as follows:

username - Unique username that user has chosen when registering.
first_name - First name of user.
last_name - Last name of user.
email - User's email that they didn't use to login.

 

Ticket

It can be broken down as follows:


 
Skeleton

 

Wirefames


Basic wireframes can be found below (Note that these vary slightly from the final website design):

Home Page

 
Surface

 

Font:
 

Icons
In order to obtain some icons for the website, Font Awesome will be utilised.


 

Colours


Features
Existing Features
Landing Page

Landing Page
 

Navigation Bar

 



Login and Create a Profile – Tells the user that they must login and create a profile before they can buy up to 5 tickets. If they are not logged in, the button will say “Login”, but if they are logged in, the button will say 
 



Django Template Pages

Password Reset Page on Mobile

Sign In Page on Large Screen
 

Messages
Django handles messages by default using 'django.contrib.messages' and you can create them within the suitable views.py, displaying them in the associated HTML file.

They are seen when the user has successfully created, edited or deleted .

Success Message

Error Message
 

Error Pages
404 and 500 error pages have been created as they are the most common errors that users will come across that the messages cannot account for.

This 404 template was copied and altered to fit the rest of the website’s style.

404 Page
 

Back to Top
 

Technologies Used
Languages
HTML - To create the Django templates for the associated views and models in the project applications.
CSS - To style the website.
JavaScript - To create the flag animation and change the track image provided when clicked.
Python – Is the primary language of Django and used to create all forms, models and views.
 
Tools
Django – The framework used in this project to incorporate databases with a website.
Crispy Forms – Formats the models into forms on webpages using the |crispy filter and {% crispy %} tag.
Gitpod – Used as the development environment.
GitHub – The project’s Version Control Management System.
Heroku – To deploy the webpage.
 
Styling
Bootstrap – To provide extra styling and out-of-the-box elements e.g. carousel.
Font Awesome – For the social media icons and carousel icons.

 
Validation
W3C HTML Validation Service –
W3C CSS Validation Service –
JSHint – 
Python Syntax Checker PEP8 – 
Web AIM – 
Lighthouse – 
 
Databases
ElephantSQL – The final database used for the deployed project.

  Back to Top
 

Testing
Code Validation
W3C HTML Validator

 

First Errors of Home Page
.

First W3C HTML Validator Test Result of Home Page
 

Final Attempt of Home Page
No issues arose.



Only Attempt of the Django Templates
No issues arose when validating each of the pages. The following screenshot was obtained for all.

Final W3C HTML Validator Test Result of Django Templates
 

First Attempt of Tickets Sold Page


First W3C HTML Validator
 




W3C CSS Validator
I validated my CSS upon completion with W3C CSS Validation Service. The attempt for the Website can be seen below. Note that the Flag Icons CSS file was not validated as it was not created by myself.

First Attempt of CSS Files
No issues arose on any of the personalised CSS files.

W3C CSS Validator Test Result
 

JSHint
 

Python Syntax Checker PEP8 Validation

Lighthouse

 

Responsiveness


This included:


Browser Compatibility

Manual Testing

Automated Testing


Tests were conducted for the following files:






Bugs

Unresolved

Deployment
During the process of coding up the website, the code was deployed on GitHub to allow for continuous manual testing and code validation. The following steps were conducted to deploy the website on GitHub:

Create Application
Create a Heroku account if you don’t have one and login.
Create a new application, by selecting the “new” button on the top right of the dashboard and click “Create new app”.
Choose a unique name for the application and select the region you live in, followed by "Create App".
 
ElephantSQL
Go to elephantsql.com, login with GitHub and create a new instance.
Copy the URL once the project instance has been created. This value can also be saved with as environment variable used to equal the DATABASES variable in settings.py.
Install the dj-database-url package version 0.5.0 by using pip3 install dj_database_url==0.5.0 to format the URL into one that Django can use, subsequently updating the requirements.txt.
 
 
Final Repo Preparations
Make sure to make any migrations in the project, by typing python3 manage.py makemigrations followed by python3 manage.py migrate into the terminal.
Ensure a Procfile, which contains web: gunicorn [project_name].wsgi:application is added to the project.
 
Heroku Deploy
Go back to Heroku and when the Project’s page opens up, go to the "settings" tab and scroll down to the “Config Vars” section.
Enter the following key-valuen pairs in the “Config Vars” section:
Key = PORT : Value = 8000
Key = SECRET_KEY : Value = Django Secret Key value obtained from settings.py
Key = DATABASE_URL : Value = ElephantSQL URL from point 5.
Go to the “Deploy” tab next and scroll down to the GitHub deployment method.
Search for the suitable repository and then connect to it by selecting the “Connect” button.
Scroll down to the bottom of the “Deploy” Page and select the type of deployment you want to conduct. If you opt to “Automatically Deploy”, it will deploy every time you push new code to your repository. Otherwise, you will have to manually deploy, by selecting the button at the bottom of the page.
The application is now deployed!

  Back to Top
 

Credits
For Code Help and Advice
Harry Dhillon
Ciaran Merrit

 
Helpful Resources