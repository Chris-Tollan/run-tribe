<h1 align="center">RunTribe</h1>

[Link to the live project](https://run-tribe-cd76c944e137.herokuapp.com/)

## Introduction

Welcome to RunTribe - the ultimate online platform for runners of all fitness levels located within the town of Motherwell, Scotland. Our website brings together a passionate community of runners, providing them with the opportunity to connect, explore, and enhance their running experience.

At RunTribe, we believe that running should be a shared adventure, where like-minded individuals can motivate and inspire each other. Whether you're a beginner looking to take your first strides or a seasoned marathon runner, our platform offers various features designed to cater to your specific needs.

One of the highlights of RunTribe is our group run feature. We understand that running alone can sometimes be daunting or lack motivation. That's why we provide a simple and hassle-free booking system for runners to schedule a place in a group run. By joining a group, you'll not only have the opportunity to meet fellow runners in your area but also benefit from the support and camaraderie that comes with running together.

Our website also hosts an interactive blog area, where a diverse range of articles relating to running and its associated topics are posted regularly. From training tips and techniques to nutrition advice and gear reviews, our blog aims to provide valuable insights and information that can benefit runners at every stage of their journey. Moreover, we encourage our users to actively engage with the blog by leaving comments, sharing their experiences, and sparking meaningful discussions. It's the perfect space to strengthen connections within the RunTribe community and learn from others with similar interests.

To join the RunTribe community and unlock all the benefits it offers, simply sign up on our website. Once you're registered, you can book your spot on group runs and start connecting with fellow runners. Don't forget to participate in our blog area, share your thoughts, and contribute to the vibrant discussions taking place.

Whether you're seeking new challenges, training partners, or simply looking to immerse yourself in a supportive community of runners, RunTribe is here to help you achieve your goals. So lace up your shoes, because a world of running adventures awaits you at RunTribe!

## User Experience (UX)
-   ### User stories

    - #### Homepage and Site Navigation (Epic 1)
        -  As a user, I want to easily understand the main purpose of the site and learn more about the organisation.
        -  As a user, I want to be able to easily navigate the site using the navbar to access the specific page I am interested in.

    - #### Using Member Accounts (Epic 2)
        -  As a user, I can create an account for the website in a straightforward manner so that I can access all features of the site.
        -  As a user, I can log in to the website so that I have the ability to book a place on a run and/or comment on an article/blog post.
        -  As a user, I can easily see if I am logged in/registered.
        -  As a user, I can easily log out from the website whenever I feel like it.
        -  As a user, I can contact the site admin to request my account details be updated/deleted.

    - #### Contact (Epic 3)
        - As a user, I want to be able to contact the website admins in order to provide feedback, suggest content and review runs and site content.
        - As an admin, I can access feedback and reviews from users in order to enhance the site and its content.

    -  #### Bookings/Runs (Epic 4)
        - As a user, I can read information about each run so including times, dates, locations and experience level that the run is aimed at and if logged in book a place on a run of my choosing.
        - As a user, I can log in and easily cancel my booking if I am going to be unable to attend or make an update to the details I provided for the booking.
        - As an admin, I can add and manage Group Runs in order to keep the timetable relevant and up to date.
        - As an admin, I can authorise bookings in order to ensure runs are kept to a manageable and safe number of runners.

    -   #### Articles/Blog Posts and Comments (Epic 5)
        -  As a user, I can click on an blog post so that I can access the content in its entirety.
        -  As a user, I can log in and comment on the blog posts in order to engage with the other users of the site.
        - As an admin, I can authorise comments users make to blog posts in order to ensure the sites content does not become irrelevant or become of an abusive, inappropriate nature.
        - As an admin, I can create, read, update and delete blog posts in order to manage the sites content.

-   ### Design
  
    -   #### Colour Scheme
        -   The colour scheme for this site is displayed in the following image
        -   ![ColourPalette](https://github.com/Chris-Tollan/run-tribe/assets/134441833/bef11059-026d-4208-ac75-af4f275fbfc7)
        -   The header and footer will be Davy's gray (605E62)
        -   The nav bar and footer content will be Orange Web (FFB139) as will any buttons throughout the site which I feel pops and adds a feeling of enthusiasm and energy
        -   The background colour throughout the site will be Anti-flash white (EFEFF0) which I feel compliments the other colours chosen. This will also be used as an outline for the orange used for the navbar and footer content.

    -   #### Typography
        -   For the Header content the font Bebas Neue from google fonts will be used
             ![BebasNeusFontExample](https://github.com/Chris-Tollan/run-tribe/assets/134441833/8fa43602-38cc-4e58-847b-b2e21e652814)
        -   For all other text content throught the site the font Roboto Condensed from google fonts will be used
             ![RobotoCondensedFontExample](https://github.com/Chris-Tollan/run-tribe/assets/134441833/40b3d476-be8d-4d2d-b94a-be5a4fc46e7a)           

-   ### Wireframes

    -   For this project Balsamiq Wireframes was used to produce wireframes for each page of the site and how it is intended to be displayed across mobile and tablet tablet devices as well as desktop computers.

    -  #### Mobile Devices 
    -   ![RunTribeMobileDeviceWireframe](https://github.com/Chris-Tollan/run-tribe/assets/134441833/ef388937-4c40-4316-9efb-acea964b22c0)

    -  #### Tablet Devices
    -   ![RunTribeTabletDeviceWireframe](https://github.com/Chris-Tollan/run-tribe/assets/134441833/c667a8cc-485e-4035-b378-3aa06dfbe75e)

    -  #### Desktop
    -   ![RunTribeDesktopWireframe](https://github.com/Chris-Tollan/run-tribe/assets/134441833/d6d5bc8d-94f7-4cc5-9914-36be4945f391)

-   ### Entity Relationship Diagrams
  
    -  #### Booking ERD
    -   ![LucidChartERDforBooking](https://github.com/Chris-Tollan/run-tribe/assets/134441833/89285125-e7ce-4e71-b038-c353eb1d4534)

    -  #### Post and Comment ERD 
    -   ![LucidChartERDforPost](https://github.com/Chris-Tollan/run-tribe/assets/134441833/77f2c0d6-a570-46a9-85ef-c38b92caf146)

## Features

-   ### Home Page
    -  The homepage will feature a navbar at the top of the screen containing a Logo to the left and menu options to the right. On smaller screens the menu options will collapse into a clickable "burger" menu and on larger screens the menu options will display in a horrizontal list within the navbar. A hero image with a message welcoming the user to the site followed by a brief about us section and a contact us form will then follow. Fixed  at the bottom of the screen will be the footer which will contain social media links.
 
-   ### Runs
    -  The Runs page will contain details about an upcoming group run. Logged in users will be able to select a run to book a place. If a user who is not logged in attempts to select a displayed run they will be asked to sign in/register.
 
-   ### My Bookings
    - The my bookings page can only be accessed by a logged in user. This will display a list of all the runs the user has booked and provide them with an option to update/cancel. If cancelling the user will be asked to confirm they wish to cancel.
 
-   ### Posts
    - Within the posts page a list of the title, author and date posted of approved posts will be displayed. If clicked the post in its entirety will be displayed as well as any approved comments made by users. Loggied in users will have the option to comment on posts as well as to edit and delete their comments.

-   ### Update Details
    - This page will contain instructions for the user to uodate/delete their account and a form for them to submit in respect of this.
 
-   ### Register
    - This can be accessed via the navbar and users will have the option to create an account. Users will be asked to created a username, add their email address, enter and re-enter a password in order to sign up.
 
- ### Login
    - This is where users can enter their username and password in order to login to their account. There will be a "Remember Me" checkbox here that the user can select to remain logged in.
 
- ### Logout
    - The logout option can be selected from the navbar. The logout screen will ask the user if they are sure they want to log out before then logging them out.

## Agile Methodology

- ### Overview
  Agile methodologies and principles were used when planning and creating this project. For the initital planning of this project I identified a number of features and split them into Epics with each epic then containing user stories of what user would look to be able to achieve when using each feature. During the development process I focussed on a specific Epic and then the user stories within that epic which I had recorded as GitHub issues and arranged on a kanBan board. When I felt the acceptance criteria of each user story was met I marked them as complete on the board. This assisted with prioritising and the continuous management of the workload related to this project.

## Technologies Used

### Languages Used

-   HTML
-   CSS
-   Python
-   JavaScript

### Frameworks, Libraries & Programs Used

- [Balsamiq](https://balsamiq.com/) was used to create the Wireframes
- [Lucid](https://lucid.app/) was used to create the ER Diagrams
- [Coolors](https://coolors.co/) was used to create the colour palette.
- Github was used as the repository for the projects code after being pushed from Git
- CodeAnywhere was used for version control, allowing me to commit changes and push them to GitHub directly from the CodeAnywhere terminal. It was the primary tool used for creating and editing all the code.
- [Google Fonts](https://fonts.google.com/) used for the fonts
- [Font Awesome](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes
- [Bootstrap](https://getbootstrap.com/) was used to build a responsive website quicker
- [Django](https://www.djangoproject.com/) was used as the framework of the application
- [Gunicorn](https://gunicorn.org/) was used as the Web Server to run Django on Heroku
- Django allauth used for account registration and authentication
- Django crispy forms used for form rendering
- Summernote used to to enable "WYSIWYG" (What You See Is What You Get) editing functionality to provide an intuitive and user-friendly interface when creating new posts and runs
- [Cloudinary](https://cloudinary.com/) used to store all of static files and images
- [FavIcon](https://favicon.io/) was used to create a FavIcon for this project
- [Heroku](https://heroku.com/) was used to deploy the application and provides an enviroment in which the code can execute
- [ElephantSQL](https://www.elephantsql.com/) used as the cloud based database for this project
- Bootstrap was used to assist in creating a responsive design for this project
- Git - version control software used to commit code and push to GitHub
- GitHub - a web-based hosting service used for storing and managing the repository and project board
- Gitpod - the IDE used for development
- CodeAnywhere - Another IDE initially used during development before changing to Gitpod
- Code Institute Python Linter - code validation tool used for Python.
- JSHint - code validation tool used for JavaScript.
- W3C Validator - code validation tool used for HTML and CSS.
- Developer Tools - used during testing, debugging and styling.
- [Python Debugger](https://docs.python.org/3/library/pdb.html) - Python debugger used to fix bug when implemented booking form

## Testing



### Testing User Stories from User Experience (UX) Section


### Further Testing


### Known Bugs
-   During development a number of small issues were encountered and overcome
    -    During the implemention of the booking form the when the user would submit the form to book a place on a run the booking would fail due to the booking title not being automatically included in the form. By running the Python Debugger [Python Debugger](https://docs.python.org/3/library/pdb.html) within the terminal I was able to see that the form was looking for booking.instance.title instead of booking.title that I was originally trying to submit with the form which when corrected as shown below resolved the issue
    
    ![booking_form_bug](https://github.com/Chris-Tollan/run-tribe/assets/134441833/006e0707-95fa-4b57-9692-6e2bee00a38a)

    -    The debugger is used by including 'import pdb; pdb.set_trace()' within the code being tested. This then breaks the code form the line inserted and allowed me to command the debugger from the terminal.

    -    Another issue which arose when updated my models was that tit caused conflicting information in the database. To fix this I followed the following steps to reset the database
        -    Delete all your migration files that start with numbers (don't delete the __init__.py)
        -    Go to the ElephantSQL Database Dashboard and click the reset button to reset the database
        -    Confirm the reset in the confirmation prompt shown
        -    Run the makemigrations and migrate commands in the workspace again as normal and this resolved the issue.


## Deployment

## Future Development
-   The future development of this project will include:-
    -    User profile section to further enhance the feeling of the website being an online community for local runners to interact.
    -    The ability for selected users to have 'moderator' permissions allowing them to assist in the maintenance of selected aspects of the site.
    -    The ability to leave comments on runs so that other users can read feedback and user experiences about the different running groups.

## Credits/Acknowleldgements/Code
-   I obtained code directly from the following which was either implemented more or less the same of used and then adapted for the purpose of meeting the needs of this project:-
    -    For the initial set up of this project and then the creation the blog and comments section I followed the steps of the Code Institure 'I think therefore I blog' walkthrough project. Boilerplate code, NavBar and footer code was then adapted from the walkthrough project to meet the design aspect of this project
    -    When creating the views for Updating and Deleting Bookings I found the following guidance which I used and adapted to meet the need of this project [www.geeksforgeeks.org/deleteview-class-based-views-django](https://www.geeksforgeeks.org/deleteview-class-based-views-django/) and [www.geeksforgeeks.org/updateview-class-based-views-django](https://www.geeksforgeeks.org/updateview-class-based-views-django/)


### Content

-   All content used within the blog posts and run details was written by the developer.

### Media

-   The images used in this project were obtain from Google Images with care taken to ensure advanced search options were implemented to make sure only images permitted to be used were obtain.

### Acknowledgements

-   My Mentor, Narender for continuous helpful feedback, guidance and encouragement.

-   Tutor support at Code Institute for their support and guidance.

-   My fellow users of Code Institute Slack Channel for their support, feeback and help.
