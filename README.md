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

Game Together

Introduction

Visit the Website Here

Visit the Project's GitHub Repository Here

Responsive Image

Website Highlights

Table of Contents
UX
Strategy
Purpose
User Stories
For This Sprint
For Future Sprints
Scope
Sprint 1
Sprint 2
Future Sprints
Structure
Project Applications
Project Databases
WebsiteUser
Ticket
Surface
Font
Icons
Colours
Responsive Screens
Features
Existing Features
Landing Page
Navigation Bar

Django Template Pages
Messages
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
The WebsiteUser model is used to obtain more information from the user than just their username, email and password. It provides relevant information with regards to the person who made the booking of a ticket and can be used to influence decisions that the race organisers will do to enhance the race experience.

It can be broken down as follows:

username - Unique username that user has chosen when registering.
first_name - First name of user.
last_name - Last name of user.
email - User's email that they didn't use to login.
fave_team - User's favourite current Formula 1 team.
nationality - User's nationality that they identify as.
Note that the details of an entry in the WebsiteUser model, will not be used in the Ticket model, apart from as a foreign key in the booked_by field. This is due to enabling the user to alter their details which will be shared on the ticket if they opt to share it with all users in the "Tickets Sold" page. Therefore, the user will not have to input the same data twice into 2 different models to protect their privacy, becasue if they had to input the same data twice, it would be bad practice.
 

Ticket
The Ticket model is used to store ticket information, regardless of if it being a new ticket, or if it is an existing ticket that is being edited or deleted. Information from the ticket booking can be shared if the person booking the ticket opts to share the details on the “Tickets Sold” page.

It can be broken down as follows:

for_self - Boolean value if ticket is for the user or a non-user.
booked_by - Connection to the current user's WebsiteUser object.
first_name - First name of user.
last_name - Last name of user.
booked_on - DateTime of when the form was booked for easier organisation.
nickname - A nickname that the user may have for the shared ticket.
fave_team - User's favourite current Formula 1 team.
nationality - User's nationality that they identify as.
seat_number - The seat number in which the user will sit.
stand - The stand letter in which the user will be sitting in.
show - Boolean value if the user wants to share their attendance in the “Tickets” Sold page.
 
Skeleton
The skeleton provides a broad initial idea that is further refined and built on. It enables the creation of a plan that aligns with the requirements of the user stories and the sprints. Therefore, wireframes can be created to act as a design aid and provide the website skeleton.
 

Wirefames
Balsamiq was used to create the conception for the website appearance and flow. I initially created a mobile version in-line with my mobile-first approach and then followed with a medium and large screen version. The key is to make sure that the website is responsive on various screens.

Basic wireframes can be found below (Note that these vary slightly from the final website design):

Home Page
Tickets Sold – The My Tickets Page is very similar, as it shows only the user’s tickets with edit and delete buttons beneath and has an extra button to redirect to the user’s profile.
Buy Tickets – The pages to edit and delete the tickets are very similar.
 
Surface
The surface plane refers more to the aesthetics and the interface itself. It’s important to select the right colour, font and icons for your website to ensure it is as appealing as possible.
 

Font
The fonts used were the official Formula 1 fonts. They were sourced from here and were used in suitable sections.

The Formula 1 fonts that were used are and they can be seen below:

Formula1-Black
Formula1-Bold
Formula1-Regular
Formula1-Wide
Fonts

The font was loaded into the project used .tff files and following the steps found at this link.
 

Icons
In order to obtain some icons for the website, Font Awesome will be utilised. Icons were only utilised in the carousel to add a bit of character to the main page and for social media icons.

For the user’s nationality, their country’s flag will be displayed on the ticket. The flag-icons CSS library was used to create these.
 

Colours
To select the colour palette for the project, I was inspired by the official Formula 1 colour scheme, which heaving relies on a distinct shade of an orange based red, black and white. When checking the contrast of the colours on Web AIM, the red with the white passed as well as the black with the red.:

Colour Palette

Where:

#E13726 (also known as --f1-red) is used for the background of one of the carousel slides as well as the majority of the backgrounds of the buttons on the website.
#fff (also known as white) is used for the majority of the websites background and the font colour of many buttons.
#000 (also known as --black) is used for the background of one of the carousel slides and for the majority of the font.
#2cd341 (also known as --green) is used for the background of one of the carousel slides and occasionally is a background colour for a button if it is next to a button in --f1-red.
#ebff00 (also known as --yellow) is used for the background of one of the carousel slides and often for buttons in their hover state.
Each Formula 1 team also required a set of colours based on their 2022 colour scheme and can be seen in the diagram below. These colours were used to created the ticket styling,

F1 Colours
 

Responsive Screens
The website will be built for a small mobile screen of width 320px and then will also meet the requirements for a medium/tablet, large and extra-large screen, as shown in the table below.

Screen Size	Breakpoint
small/mobile	320px
medium/tablet	768px
large	992px
extra-large	1400+px

  Back to Top
 

Features
Existing Features
Landing Page
The landing page is the first introduction to the website that the user generally has and therefore, it needs to be visibly attractive and easy to navigate. The large Formula 1 Dublin City Grand Prix logo at the top of the page tells the user clearly what the website is about.

A labelled navigation bar with various headings provides the user with details regarding how to use the website effectively.

A carousel with bright slides attracts the user to its content, which prompts the user to create a profile, show the tickets that have already been bought or to obtain more race details.

Landing Page
 

Navigation Bar
The navigation bar is designed to be responsive for the different screen sizes and collapses into a hamburger button if there is not enough room on the screen to fit. Each item within the navigation bar links to a section on the website. In order to increase each items readability, aria-labels are used:

Navigation Bar for Large Screens

The navigation bar is white in colour with black font to contrast each other easily and to increase readability. If the user is hovering over the various navigation bar items, if it is over a particular one, it will cause the font to turn red.

The hamburger button matches the red colour used for the project along with the red border at the bottom of the navigation bar which acts as a clear divider between the navigation bar and the content of the webpage.

Navigation Bar for Small Screens
 

Information Carousel
The information carousel is used at the top of the home page to attract users to its contents. The slides vary in colour to draw the user’s attention compared to the predominantly white sections above and below it. The design is responsive and each slide's contents can be seen clearly on various devices.

Information Carousel on Small Screens

The slides are broken down as follows:

Slide 1: Promote “Tickets Sold” page – Encourages user to see who is going, which either encourages them to buy a ticket or find out more about the race.
Slide 2: Urge the user to create a profile – It is vital for the user to create a profile in order to buy a ticket.
Slide 3: Acquire race details – The slide teases some of the race details, drumming up excitement about the event.
Information Carousel on Large Screens
 

Race Details Section
In order to promote the race, details regarding the track and the event need to be provided. 3 eye catching details regarding when the event will take place and track characteristics – length and turns, provide a quick snapshot.

Race Details Section on Large Screens

A schematic of the track along with 4 stands is shown. Within the paragraphs, the user is prompted to click on this schematic in order to turn it into an image of the track mapped out onto its real life route on Google Images. Some of the tourist attractions nearby are also briefly mentioned in this section.

On smaller screens, all the element stack up on top of each other so the content is still easy to follow.

Race Details Section on Small Screens
 

How to Book Tickets Section
The “How to Book” section provides information to the user regarding the steps they are required to follow in order to book a ticket. It consists of 3 informative cards that remain spread out on 1 row when the screen is large, but all stack on top of each other when the screen becomes small.

How to Book Section on Small Screens

The 3 cards consist of the following information and provide buttons which link to the suitable webpage:

Login and Create a Profile – Tells the user that they must login and create a profile before they can buy up to 5 tickets. If they are not logged in, the button will say “Login”, but if they are logged in, the button will say “Profile”.
My Tickets – Tells the user to go to the “My Tickets” page in order to book, edit or delete a ticket.
Show Tickets – Tells the user that if they have opted to share their ticket details that it will be shown on a page called “Tickets Sold” and they can view who else has booked a ticket.
How to Book Section on Large Screens
 

Footer
The footer works in tandem with the navigation bar menu as it enables the user to visit various pages on the website. It also consists of related social media links which act as method of connecting the user with the race organisers and allows users to contact the race organisers via a direct message.

It's simple, yet clean design, means that it is easy to navigate, with icons being used for social media channels being self-explanatory. The layout also remains the same for all screen sizes due to its simplicity.

Footer on Mobile Screen
 

Tickets Sold Page
As previously mentioned, the “Tickets Sold” page consists of the users’ tickets that have opted to share some of their details to other website users. It contains a descriptive paragraph at the top to provide the user with some details, followed by a button to encourage the user to buy a ticket.

Tickets Sold Page on Large Screen

On smaller screens, the tickets stack on top of each other.

Tickets Sold Page on Mobile

At the base of the page, 3 cards per row and up to 6 per page, show each suitable ticket and the owners stand and seat, favourite team and nationality. This can be used to check what seats might be free and to see who is sitting nearby.

Sample Ticket
 

Profile
The Profile page allows users to provide specific details about themselves which help influence data-driven decisions made by the race organisers. The user can fill in fields: First Name, Last Name, Email, Favourite Team and Nationality. This helps to create a data entry regarding the user into the WebsiteUser table. This acts as an identifier as to who bought the tickets.

Profile on a Large Screen

Similarly, the form narrows on smaller screens, but is stacked in the same manner, with a submit button at its base.

Profile on a Mobile

If the user has already created a profile, by opening the profile page, it will preload the information and enable the user to edit their previously entered details.

Note that the details themselves, added to the WebsiteUser model, will not be used in the Ticket model. This is due to enabling the user to alter their details, which will be shared on the ticket. Therefore, the user will not have to input the same data twice into 2 different models to protect their privacy, as inputting the same data twice is poor practice.
 

My Tickets Page
The “My Tickets” Page is very similar in design to the Tickets Sold Page in which it contains an explanatory paragraph at the top of the page followed by a ticket prompting the user to buy a ticket, but instead it only displays the user’s own tickets. It also has an extra button for the profile in case the user forgot to fill in their profile beforehand.

Below each ticket, there is a section with an edit and delete button. The “Edit” button allows the user to edit the ticket once it has been clicked. The ”Delete” button allows users to delete the ticket via a suitable form.

On smaller screens, instead of lining up 3 in a row, tickets stack up on top of one another.

My Tickets Page on Large Screen
 

New Ticket Page
In order to book a ticket, the user must click “Book a Ticket” on the “My Tickets” page. This will redirect the user to a blank form, where they can declare if they are booking for themselves or for someone else, as they can only buy 1 ticket for themselves and a maximum of 5 total tickets. They can then fill out the following fields: First Name, Last Name, Nickname, Favourite Team and Nationality.

New Ticket Page on Large Screen

An image of the track layout with stands and an individual stand with seat numbers can be seen. The user should select a seat and stand in the dropdown menus. If the specific seat has already been taken, the user will be notified and they will have to fill out the form and select a new seat.

At the end of the form, the user is prompted if they want to share their ticket details on the “Tickets Sold” page and the form is recorded as an entry in the into the Ticket table.

The page is responsive and therefore the track stand and seating images stack on top of each other on small screens.

New Ticket Page on Large Screen
 

Edit Ticket Page
The “Edit Ticket” Page is basically identical to the New Ticket Page, but it just loads the form with previously entered values from the specific ticket.
 

Delete Ticket Page
The “Delete Ticket” Page is basically identical to the Edit Ticket Page, but it just includes a button at the top of the page to redirect the user back to the “My Tickets” page in case they clicked delete by mistake. The user has to scroll down to the bottom of the page to delete the ticket to ensure that the decision is intentional.
 

Flag Animation
A checkered flag animation is run when the user opens the home page. This is a novel, extra feature of the website to pique the user’s interest in the movement.

The animation uses JavaScript to push the flag down the screen slowly and it eventually stops at the base of the page on large screens.

If the user clicks on the flag on the website, they will be redirected to the “Tickets Sold” page.
 

Django Template Pages
This project utilises allauth to allow users to register, login, logout etc. on the website and provides excellent out-of-the-box functionality. This creates basic templates to conduct these tasks, but in order to align them with the style of the rest of the website, they had to adopt the project’s base file and were spaced to ensure the user experience was good.

Password Reset Page on Mobile

Sign In Page on Large Screen
 

Messages
Django handles messages by default using 'django.contrib.messages' and you can create them within the suitable views.py, displaying them in the associated HTML file.

They are seen when the user has successfully created, edited or deleted either their profile or ticket at the top of the page and they follow the Bootstrap 5 naming convention. Therefore, they are pre-styled based on their message type.

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
Cloudinary - Used to store website's images.
Gitpod – Used as the development environment.
GitHub – The project’s Version Control Management System.
Heroku – To deploy the webpage.
Balsamiq – For the creation of associated wireframes.
 
Styling
Bootstrap – To provide extra styling and out-of-the-box elements e.g. carousel.
Font Awesome – For the social media icons and carousel icons.
Flag Icons CSS – For the flag icons on the ticket based on the user’s nationality.
Formula 1 Fonts – The fonts that Formula 1 uses on their website, which inspired the fonts for this website.
 
Validation
W3C HTML Validation Service – To validate all the HTML files, including the templates from Django itself, due to editing them.
W3C CSS Validation Service – To validate the “style.css” page as well as the specific css page made to create the Formula 1 teams’ logos.
JSHint – To validate the code within the “script.js” file.
Python Syntax Checker PEP8 – To validate all the Python files, making sure they align with PEP8.
Web AIM – To analyse the colour contrast properties between colours.
Lighthouse – To check the website’s performance and accessibility, making sure the best practices are used.
 
Databases
SQLite - The default database on Django, utilised for unittesting.
ElephantSQL – The final database used for the deployed project.

  Back to Top
 

Testing
Code Validation
W3C HTML Validator
I validated my HTML at various stages of the website creation using the W3C HTML Validation Service. The various attempts for the Website can be seen below.
 

First Attempt of Home Page
The primary issue that arose in the first attempt was the inclusion of a <button> tag inside an <a> tag. This was rectified by replacing the <button> tags with <span> tags.

First W3C HTML Validator Test Result of Home Page
 

Final Attempt of Home Page
No issues arose.

Note that the same result was obtained when validating the Profile, New Ticket, Edit Ticket and Delete Ticket pages.

Final W3C HTML Validator Test Result of Home Page
 

Only Attempt of the Django Templates
No issues arose when validating each of the pages. The following screenshot was obtained for all.

Final W3C HTML Validator Test Result of Django Templates
 

First Attempt of Tickets Sold Page
The primary issue that arose in the first attempt was similar to the Home Page i.e. the inclusion of a <button> tag inside an <a> tag. This was rectified by replacing the <button> tags with <span> tags.

An additional issue occurred due to dealing with the .svg files of the F1 teams’ logos where the version was included as 1.0, but 1.1. was required. This was fixed by removing the version attribute.

First W3C HTML Validator Test Result of Show Tickets Page
 

Final Attempt of Tickets Sold Page
No issues arose.

Note that the same result was obtained when validating the My Tickets page as the errors were due to the ticket card information one each page.

Final W3C HTML Validator Test Result of Show Tickets Page
 

W3C CSS Validator
I validated my CSS upon completion with W3C CSS Validation Service. The attempt for the Website can be seen below. Note that the Flag Icons CSS file was not validated as it was not created by myself.

First Attempt of CSS Files
No issues arose on any of the personalised CSS files.

W3C CSS Validator Test Result
 

JSHint
The primary JavaScript document script.js was often run through JSHint to check for any syntax or declaration errors. Below contains the returned results of the script.

Final Attempt of JavaScript Files
No issues arose.

JSHint Result
 

Python Syntax Checker PEP8 Validation
The Python Syntax Checker PEP8 was used to check all the Django Python files – scanning for any syntax or declaration errors. Below contains the returned results of the scripts.
 

First Attempt of Python Files
Many warning and errors were obtained in the first run through the PEP8 linter. They mainly consisted of lines that were too long, over-indentation or under-indentation of items and then too many or too few blank lines. These were all easy to rectify quite quickly.
 

Final Attempt of Python Files
No issues arose in any of the files and their accompanying test_ files, as seen in the sample one below for the “Show Attendees” application’s test_views.py page.

Python Syntax Checker PEP8
 

Lighthouse
In order to verify the suitability of the webpage, Lighthouse, a tool found in Chrome Developer Tools was used to check a broad variety. This includes:

Performance – Based on how fast the website loads and contributes to the overall UX.
Accessibility – Based on how easy it is to use the website regardless if people might use a screen reader, etc.
Best Practices – Based on the best practices used in industry.
Final Attempt for Lighthouse
After completing the project, Lighthouse was used to check the suitability on the website. The following result was obtained:

Lighthouse Final Attempt
 

Responsiveness
The responsiveness of the design was manually checked using the Chrome Developer Tools for various screens. The manual testing itself will be discussed here.

This included:

iPhone SE
Pixel 5
Samsung Galaxy S8, S20 Ultra
iPad Air and Mini
Galaxy Fold
Nest Hub and Hub Max
I also opted to use the responsiveness option and checked the screens at the following width sizes:

320px
768px
992px
1400px
No issues arose, due to the responsive design of the website with rem and % values.
 

Web Aim Contrast Checker
The Web AIM was used, as described in the Colours section.

For the red and white, the contrast check between them passed, as it exceeded the contrast ratio criteria of 4.5, as seen below, as no narrow font is used to contrast the red and white:

Web Aim Contrast Result for White and Red

For the red and black, the contrast check between them passed, as it exceeded the contrast ratio criteria of 4.5, as seen below, as no narrow font is used to contrast the red and black:

Web Aim Contrast Result for Black and Red
 

Browser Compatibility
The website was tested on a variety of browsers to ensure that it was fully functional.

On desktop, Google Chrome, Mozilla Firefox and Microsoft Edge were utilised.

On mobile, Google Chrome was utilised.

The responsiveness and the appearance remained relatively the same across the various devices and browsers.
 

Manual Testing
As detailed above, the website was used on a variety of browsers and devices. It was tested by friends and family to catch any mistakes. The User Stories and page elements are manually tested in this separate Markdown page:

MANUAL_TESTS

Automated Testing
The automated testing is conducted using Django’s built-in TestCase class, which is an extension of the unittest Python library.

Tests were conducted for the following applications and related files:

race_details:
urls.py
views.py
show_attendees:
urls.py
views.py
booking:
urls.py
views.py
models.p
forms.py
They were run by putting python3 manage.py test into the terminal.

In order to check how much code is tested using the unit tests, coverage reports were generated.

The following steps were conducted to obtain the coverage report for each application:

pip3 install coverage - to install coverage.
coverage run --source=[type in application name] manage.py test - to run the tests.
coverage report - to generate the report.
coverage html - to create a specific interactive report called index.html within a new folder called htmlcov.
python3 -m http.server - to view the special report when you click on the htmlcov/ folder in the static website.
The following reports were obtained:

race_details - 94% Coverage
race_details coverage
 

show_attendees - 100% Coverage
show_attendees coverage
 

booking - 80% Coverage
booking coverage
  Back to Top
 

Bugs
Resolved
Bug	Fix	Useful Source	Associated Image
Navbar border does not fill 100% of the screen width	Copied a navbar from the bootstrap documentation, as the navbar was confused with all the margin and padding classes.	Bootstrap Navbar	Navbar with Short Border
template_name is a standard variable name in Django views using the TemplateView class, but it was not working	Ensured that the correct variable was changed from home_page to template_name in race_details app.	Useful YouTube Video	-
CSS files wouldn't load as obtained a static not registered error	I put {% load static %} at top of base file	Remember Static Tag	-
An issue with links connecting to sections on the same page but with a different id	Use this for the link {% url 'home' %}#section-id	Link to Specific Section on Page	-
Issue with saving profile if it already existed	Make sure to clearly define the create a data entry and edit an entry in a model views. Scott from Code Institute tutor support helped and also a techwithtim resource	TechWithTim Django Forms	Saving Profile Error
h-100 Bootstrap 5 style not working on cards within carousel	max-height style applied to carousel was removed and the h-100 was changed to the carousel-inner sections	-	-
The user could purchase more than 5 tickets	Within the logic, the number of tickets that the user had was increased by 1 to anticipate the user buying another when filling out the “New Ticket” form.	-	-
When creating the error 500 page, the associated function prevented the website from running	Removed the extra exception parameter left in the function that was copied from the 404 function	-	-
Deployment was not working as Django couldn't find allauth	I was saving everything to requirement.txt instead of requirements.txt – the name was updated	-	-
Database error was obtained when testing	Swapped to the local SQLite database in settings.py, instead of using the ElephantSQL database for deployment	Both my mentor Harry and Jason from Code Insititute mentioned this as a potential fix	Database Issue
Messages not Appearing	Changed the HTML block location to the top of the page, just underneath the navbar and added x symbol functionality to close by setting button to data-bs-dismiss='alert'	Bootstrap 5 Alert Button Changes	-
Issue with <button> tag wrapped by <a> tag when validating code	Changed the <button> to a <span>	Anchor Tags Cannot Wrap Buttons	-
JavaScript was trying to run animation even though it doesn’t exist on any other page apart from home page and is leading to a console error	Added an if statement to check if the flag exists and if it does, then run the associated function.	-	-

 

Unresolved
No unresolved bugs were left in the project.


  Back to Top
 

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
 
Cloudinary
Create a cloudinary account.
Add any images for your project in the “Media Library”.
Copy the Cloudinary API URL from your dashboard.
 
Final Repo Preparations
Make sure to make any migrations in the project, by typing python3 manage.py makemigrations followed by python3 manage.py migrate into the terminal.
Ensure a Procfile, which contains web: gunicorn [project_name].wsgi:application is added to the project.
 
Heroku Deploy
Go back to Heroku and when the Project’s page opens up, go to the "settings" tab and scroll down to the “Config Vars” section.
Enter the following key-valuen pairs in the “Config Vars” section:
Key = PORT : Value = 8000
Key = SECRET_KEY : Value = Django Secret Key value obtained from settings.py
Key = DATABASE_URL : Value = ElephantSQL URL from point 5.
Key = CLOUDINARY_URL : Value = Cloudinary API URL from your Cloudinary account in point 9.
Go to the “Deploy” tab next and scroll down to the GitHub deployment method.
Search for the suitable repository and then connect to it by selecting the “Connect” button.
Scroll down to the bottom of the “Deploy” Page and select the type of deployment you want to conduct. If you opt to “Automatically Deploy”, it will deploy every time you push new code to your repository. Otherwise, you will have to manually deploy, by selecting the button at the bottom of the page.
The application is now deployed!

  Back to Top
 

Credits
For Code Help and Advice
Harry Dhillon
Rich Wells
 
Helpful Resources
On using .tff fonts
Model field details
SVG tips when creating the track schematic
For turning .png to .svg
Error page handling
 
For Content and Code
Footer from the “South Kerry Greenway” project
404 page template
CSS Flags for tickets
Pagination from “I Think, Therefore I Blog” project
Checkered flag image

  Back to Top