# Riddle Game
This website is a **Flask application**, a python microframework. The target audience is any user who wants to play a guessing-riddle game for entertainment. The game asks players to input a player name and answer a number of text based riddles.

## UX
The following section describes the UX process for this project.

#### UX Process
1. **Layout** - Reviewed the Code Institute learnings to date and Bootstrap themes to extract design ideas.
2. **User Stories** - Walked through user stories.
    1. **Header Call-to-action** - As a user, I want to understand the purpose of this website and intuitively understand how to use it.
    2. **Navbar - Contact** - As a user, I want to be able to contact the developers to offer feedback and suggestions.
    3. **Navbar - Riddle Game** - As a user, I want to be able to select the homepage, and be presented with a blank player name textarea.
    4. **Navbar - Game** - As a user, I want to be able to restart the game, and be presented with a blank player name textarea.
    5. **Enter Player Name** - As a user, I want to be able to enter a unique player name into a textarea, and start the game.
    6. **Start Game** - As a user, once I select start game, I want to be greeted with my player name, to be presented with the first riddle and my player name to be displayed in a list.
    6. **Answer Riddles** - As a user, I want to be able to enter an answer into a textarea, submit an answer and if I provide the correct answer, be redirected to the next riddle.
    7. **Enter Incorrect Answer** - As a user, I want to be able to enter an answer into a textarea, submit an answer and if I provide an incorrect answer, the textarea is cleared, redirecting me to a blank textarea to guess again.
    8. **List Incorrect Answer** - As a user, I want to be able to view incorrect answers, displayed in a list.
    9. **Answered all Riddles Correctly ** - As a user, when I have answered all riddles correctly, I want to be redirected to an end of game message.
3. **Wireframe** - Sketched the wireframe on paper, to include the features for each user story, meeting the users needs by presenting the data on a dashboard charting web application.

## Features

### Existing Features
The following section describes all the front-end features in this project.

1. **Header Call-to-action** - Provides users with a website title and description of what to do next.
2. **Navbar - Contact** - Provides users with a navbar menu, bringing users to a form, to contact developers.
3. **Navbar - Riddle Game** - Provides users with a navbar menu to go to the homepage.
4. **Navbar - Game** - Provides users with a navbar menu to restart the game at any stage.
5. **Enter Player Name** - Provides users with a blank text area to input a player name.
6. **Start Game** - Provides users with a new page, which greets them by their player name, displays a riddle one by one, and displays their player name in a list of player names.
6. **Answer Riddles** - Provides users with a blank text area, to enter their answer and select submit to be redirected to the next riddle if the answer is correct.
7. **Enter Incorrect Answer** - Provides users with a blank text area, to enter their answer and select submit to be reidrected to answer this riddle again if the answer is incorrect.
8. **List Incorrect Answer** - Provides users with a list of incorrect answers.
9. **Answered all Riddles Correctly ** - Provides users with a end of game message when they have answered all riddles correctly.

### Features to Implement
1. **Leaderboard** - Add a feature to include a scoring system that ranks all players.
2. **Incorrect Answers - Show Riddle or Riddle Number** - Consider adding a feature to indicate which incorrect answer is related to which riddle, but ensure not to make the game too simple for players e.g. by storing prior players incorrect answers.

## Technologies Used
The following section describes all technologies and tools used to construct this project.

- [Cloud 9 IDE](https://aws.amazon.com/cloud9/)
    - The project used **Cloud 9**, online integrated development environment, to construct the code end to end.
- [Bootstrap](https://getbootstrap.com/)
    - This project uses **Bootswatch**, a library of Bootstrap themes. The [Clean Blog Template](https://startbootstrap.com/template-overviews/clean-blog/), was used for this project.
        - **Static folder**: Contains Bootstrap files (no other files stored within this folder).
        - **`base.html` and `contact.html`** - Most of this html code was copied from the bootstrap `index.html` and `contact.html` files as a boiler plate template, then amended to suit this project.
        - **All Other Code**: Compiled by the project developer.
- [Flask](http://flask.pocoo.org/)
    - This project uses **Flask**, a Python micro web framework. It is classified as a microframework because it does not require particular tools or libraries. Flask offers beneficial functionality such as template logic, which allows the `base.html` file to be inherited on other html files via `{% extends 'base.html' %}`, `{% block content %}`, and ` {% endblock %}` jinja code.
- [Jinga](http://jinja.pocoo.org/)
    - This project uses **Jinja**, a template engine for Python.
- [Python](https://www.python.org/)
    - This project uses **Python**, an interpreted high-level programming language for general-purpose programming and used to write the logic of this game.
- [HTML](https://en.wikipedia.org/wiki/HTML)
    - This project uses **HTML**, the standard mark-up language used to build website layout, which was written in this project within the `.html` files.
- [JSON](https://json.org/)
    - This project uses **JSON** (JavaScript Object Notation), which is a text-based data interchange format designed for transmitting structured data. It is most commonly used for transferring data between web applications and web servers. A JSON file was used as a database in this project to retreive the riddle information.
- [.txt files](https://en.wikipedia.org/wiki/Text_file)
    - This project uses **.txt files**, a file to store text and was used in this project to write to and read from, for exmaple when a player enters a player name and selects start game. 
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
    - This project uses **Javascript**, an object-oriented programming language used to create interactive effects within web browsers. Javascript within this project was part of the Bootstrap template.
- [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools/)
    - This project uses **Chrome Dev Tools**, a set of web developer tools, to continuously test and inspect that the web pages are rendering as expected within the browser.
- [GitHub](https://github.com/)
    - This project uses **GitHub**, a web hosting service, for version control and final project deployment.
- [All Other Technologies](https://startbootstrap.com/template-overviews/clean-blog/)
    - All other technologies within this project were included with the Bootstrap template.

## Testing
The following is an overview of testing to ensure all functionality works as intended in this project.

**Manual testing**, ongoing via `Cloud 9`, `Run`. Once each functionality coded, checked application operating as expected in web browser by walking through each functionality. Testing included the following:

1. **Index.html**: Selected all nav bar menus to verify that all menus operated as intended. The following bugs were encountered.
    1. **Bug/Expected Output** - code not rendering in browser. **Issue** - At end of html files spelled {% end block %}. **Fix** - Scanned code. Updated with no space i.e. {% endblock %}.
    2. **Bug/Expected Output** - contact page missing 'Contact Developer' heading. **Issue** - Typo in {{ page_heading }} on contact.html and code not reading from run.py. **Fix** - Checked relevant code and updated typo to ensure {{ page_heading }} spelled the same as code on run.py.
    3. **Bug/Expected Output** - header photo skewed/not looking good. **Issue** - pixel sizing not in line with bootstrap design. **Fix** - Researched online until located appropriately sized photo to fit bootstrap template.
    4. **Bug/Expected Output** - after inputting player name and selecting start game, browser error 'Method Not Allowed'. **Issue** - run.py not updated with code to write player name to players.txt. **Fix** - Developed run.py to include relevant code to write to players.txt.
    5. **Bug/Expected Output** - form and button hugging each other too closely. **Issue** - Bootstrap grid system not implemented. **Fix** - Added divs and html style code to create spacing.
    6. **Bug/Expected Output** - terminal displaying error 'socket.error: [Errno 98] Address already in use [closed]'. **Issue** - didn't select ctrl+c to stop run.py running prior to closing workspace, the following morning encountered this error. **Fix** - researched solutions online, used stack overflow. In terminal, ran 'lsof -i :8080' to locate port ID. Then ran sudo kill -9 <process_id> to kill process.
2. **Game**: Input a test player name and selected start game. Verifying player is redirected to a riddle and player name is being stored within the appropriate list. Answered riddles incorrectly to verify incorrect answers are being stored within the appropriate list. Answered all riddles correctly to verify that the form is cleared, that the player is redirected to the next riddle and when all riddles are answered correctly the player is redirected to the end of game message.
    1. **Bug/Expected Output** - after inputting correct answer, browser error 'ValueError'. **Issue** - json data not reading, throwing up this error. **Fix** - scanned json file for irregularities/to try and identify the issue. Removed comma at the end of last closing curly bracket.
    2. **Bug/Expected Output** - during inputting all correct answers, player name is being duplicated within player name list. **Issue** - OPEN TO DEBUG.
    3. **Bug/Expected Output** - form and button hugging each other too closely. **Issue** - Bootstrap grid system not implemented. **Fix** - Added divs and html style code to create spacing.
    4. **Bug/Expected Output** - after updating commentary, error in browser pointing to {{curly brackets. **Issue** - updated commentary to state that the code within {{ }} is flask code. The browser tried to read this as code. **Fix** - updated {{ }} to the words, curly brackets.
3. **Contact**: Input required data on relevant lines in form and selected send to verify that each line of the form operates as expected.
4. **Responsive Testing**: Used Chrome Dev tools to inspect application on various device sizes.
    1. **Bug/Expected Output** - Startgame.html not responsive and skewed on all but a large screen. **Issue** - OPEN TO DEBUG.




1. **Landing section and Subscribe to News**:
    1. Select the 'Contact' menu on the navbar and verify that the user is moved to the contact section and away from the landing page.
    2. Select 'The Beach Boys' menu on the navbar and verify that the user is moved to the landing page.
    3. Select the 'Sign Up' button and verify that a modal appears.
    4. Complete all user details within the modal and verify that all fields accept relevant inputs.
    5. Select 'Sign Up' to submit the user’s details and verify that the modal closes.
    
        - **Bug 1** - Call to action text not standing out for clean reading.
            - **Issue** - Background photo too bright and text size too small.
            - **Fix** - Adjusted photo coloring by reducing brightness and uploaded new photo. Increased text size use of html `<h1>` and `<strong>` tags.
        
        - **Bug 2** - Modal input field text alignment centred, rather than left aligned.
            - **Issue** - Additional `<div>` tags throwing out alignment.
            - **Fix** - Updated `<div>` tags to ensure alignment correct.

2. **About Section**:
    1. Select the 'About' menu on the navbar and verify that the user is moved to the about section.
    2. Select the hyperlink, 'To request a booking, please go to the contact section.', and verify that the user is moved to the contact section.

3. **Videos Section**:
    1. Select the 'Videos' menu on the navbar and verify that the user is moved to the videos section.
    2. On each video, select play, pause, time slider, volume icon, volume slider, full screen and download. Verify that all functionalities work as intended.

        - **Bug 1** - Custom `main.css`, not overriding Bootstrap CSS.
            - **Issue** - Website not rendering in browser until Chrome cache cleared.
            - **Fix** - Spent significant time, hours over several days researching this. Decided to try to clear the cache in Chrome and this fixed the issue. Also used CSS id classes in some areas of the `main.css` to override the Bootstrap CSS.

        - **Bug 2** - Bootstrap template grid not suitable for the video layout.
            - **Issue** - Bootstrap template grid only suitable for one column of data.
            - **Fix** - Updated `index.html` `<div>` tags around the videos to a bootstrap grid class of `col-sm-6`, to layout two videos side by side within each div row.

4. **Audio Section**:
    1. Select the 'Audio' menu on the navbar and verify that the user is moved to the audio section.
    2. On each audio track, select play, pause, time slider, volume icon, volume slider, and download. Verify that all functionalities work as intended.
    
        - **Bug** - Bootstrap template grid not suitable for audio layout.
            - **Issue** - Bootstrap template grid suitable for one column of data.
            - **Fix** - Updated `index.html` `<div>` tags around the audio to a bootstrap grid class of `col-sm-6`, to layout two audio tracks side by side on each div row.
        
        - **Bug** - Each audio track includes a video thumbnail above the controls.
            - **Issue** - Used `<video>` html tags, that should be `<audio>` html tags.
            - **Fix** - Updated relevant `<video>` html tags, that should be `<audio>` html tags.

5. **Contact Section**:
    1. Select the 'Contact' menu on the navbar and verify that the user is moved to the contact section.
    2. Complete all user details within the form and verify that all input fields accept the text as intended.

6. **Social Media Icons**:
    1. Scroll to the footer section.
    2. Select the Facebook, Twitter and YouTube icons, and verify that all icon hoover styling is as intended. Verify that all icons open each social media page, in a new browser window.

7. **Responsive Testing**:
    1. In Chrome, right click on the site and select 'inspect', to open the Chrome Dev tools.
    2. Select the toggle device icon at the top of the window, to open the responsive testing window.
    3. Test how the website is rendering on each device size from Galaxy S5 to iPad Pro.


## Deployment
The following section describes the process to deploy this project to GitHub Pages.

1. Create a new repository within GitHub.
2. Within GitHub, under the `<> Code` heading, copy `git remote add origin...` command, paste into the IDE terminal and execute.
3. Within GitHub, under `<> Code` heading, copy `git push -u origin master` command, paste into the IDE terminal and execute.
4. The project is now pushed to GitHub.
5. Within GitHub, under the `Settings` heading, go to the `GitHub Pages` section.
6. Select Master branch and save.
7. The project is now published to GitHub Pages and can be viewed in the browser.
8. GitHub Pages URL: [The Beach Boys](https://githhayden.github.io/The-Beach-Boys/).


### Deploy via Heroku
1. Via Linux Terminal, login to Heroku, using 'heroku login' command. Input Heroku login details.
2. Create new Heroku app, using 'heroku apps:create appname' command.
3. Push project to Heroku, using 'push -u heroku master' command.
4. Create scale, using 'heroku ps:scale web=1' command.
5. Login to Heroku and select newly created app.
6. Select settings. Select ‘Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
7. From 'More' menu on the top right, select 'Restart all dynos'.
8. View app: In settings, select Domain URL, NOT Git URL to view your hosted application.
9. Deployed via Heroku: [Riddle Game Website](https://iq-riddle-game.herokuapp.com/).


## Credits

### Content
- The text for the About section was copied from [Wikipedia](https://en.wikipedia.org/wiki/The_Beach_Boys).

### Media
- The photo used in this site was copied from [WWMT.com](https://wwmt.com/news/local/the-beach-boys-to-headline-tulip-time-2018-tickets-on-sale-nov-9).
- The videos and audio tracks in this site were copied from [YouTube](https://www.youtube.com/). They were then converted to MP4 and MP3 files.

### Acknowledgements
- I received inspiration for this project from The Beach Boys videos, music and website, from Bootstrap template designs, from ongoing research online and from Code Institute education.