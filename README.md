# Riddle Game
This website is a riddle game, built using **Flask**, which is a python microframework. The target audience for this website is any user who wants to play a riddle game for entertainment. The game asks players to enter a player name and answer a number of text based riddles correctly to complete the game.

## UX
The following section describes the UX process for this project.

#### UX Process
1. **Layout** - Reviewed the Code Institute learnings to date and Bootstrap themes to extract design ideas.
2. **User Stories** - Walked through user stories.
    1. **Header Call-to-action** - As a user, I want to understand the purpose of this website and intuitively understand how to use it.
    2. **Navbar - Contact** - As a user, I want to be able to contact the developers to offer feedback and suggestions.
    3. **Navbar - Riddle Game** - As a user, I want to be able to select the landing page, and be presented with a blank player name textarea.
    4. **Navbar - Game** - As a user, I want to be able to restart the game, and be presented with a blank player name textarea.
    5. **Enter Player Name** - As a user, I want to be able to enter a unique player name into a textarea, and start the game.
    6. **Start Game** - As a user, once I select start game, I want to be greeted with my player name, to be presented with the first riddle and my player name to be displayed in a list.
    6. **Answer Riddles** - As a user, I want to be able to enter an answer into a textarea, submit an answer and if I provide the correct answer, be redirected to the next riddle.
    7. **Enter Incorrect Answer** - As a user, I want to be able to enter an answer into a textarea, submit an answer and if I provide an incorrect answer, the textarea is cleared, redirecting me to a blank textarea to guess again.
    8. **List Incorrect Answer** - As a user, I want to be able to view incorrect answers, displayed in a list.
    9. **Answer all Riddles Correctly ** - As a user, when I have answered all riddles correctly, I want to be redirected to an end of game message.
3. **Wireframe** - Sketched the wireframe on paper, to include the features for each user story, meeting the users needs by presenting the data on a dashboard charting web application.

## Features

### Existing Features
The following section describes all the front-end features in this project.

1. **Header Call-to-action** - Provides users with a website title and description of what to do next.
2. **Navbar - Contact** - Provides users with a navbar menu, bringing users to a form, to contact developers.
3. **Navbar - Riddle Game** - Provides users with a navbar menu to go to the landing page.
4. **Navbar - Game** - Provides users with a navbar menu to restart the game at any stage.
5. **Enter Player Name** - Provides users with a blank text area to input a player name.
6. **Start Game** - Provides users with a new page, which greets them by their player name, displays a riddle one by one, and displays their player name in a list of player names.
7. **Answer Riddles** - Provides users with a blank text area, to enter their answer and select submit to be redirected to the next riddle if the answer is correct.
8. **Enter Incorrect Answer** - Provides users with a blank text area, to enter their answer and select submit to be reidrected to answer this riddle again if the answer is incorrect.
9. **List Incorrect Answer** - Provides users with a list of incorrect answers.
10. **Answer all Riddles Correctly ** - Provides users with a end of game message when they have answered all riddles correctly.

### Features to Implement
1. **Leaderboard** - Add a feature to include a scoring system that ranks all players.
2. **Incorrect Answers - Show Riddle or Riddle Number** - Consider adding a feature to indicate which incorrect answer is related to which riddle, but ensure not to make the game too simple for players e.g. by storing prior players incorrect answers. Improve how incorrect answers are displayed with the player name.

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

1. **Navbar - Contact**:
    1. Select 'Contact' on the navbar and verify that the user is moved to the contact section and away from the landing page.
    2. Complete all user details within the contact form and verify that all fields accept relevant inputs.
    3. Select 'Send' to submit the user’s details and verify that the user is brought to a thank you message and the form input fields are cleared.
        - **Bug 1** - Code not intially rendering in browser.
            - **Issue** - Jinja at end of html files spelled {% end block %}, in error.
            - **Fix** - Scanned all html code. Updated with relevant jinja code, with no space i.e. {% endblock %}.
        - **Bug 2** - 'Contact Developer' heading missing.
            - **Issue** - Jinja typo in {{ page_heading }} on `contact.html` and code not reading from `run.py` file.
            - **Fix** - Checked relevant code and updated typo to ensure {{ page_heading }} spelled the same as code on `run.py` file.
        - **Bug 3** - After updating commentary within html files, error in browser pointing to {{curly brackets.
            - **Issue** - Updated commentary to state that the code within 'curley brackets', is flask code. The browser tried to read this as code.
            - **Fix** - Updated {{ }} to the words, curly brackets.
2. **Navbar - Riddle Game**
    1. Select 'Riddle Game' on the navbar and verify that the user is moved to the landing page.
    2. Verify that the landing page player name text area is blank and ready to start a new game.
3. **Navbar - Game**
    1. Select 'Game' on the navbar and verify that the user is moved to the landing page.
    2. Verify that the landing page player name text area is blank and ready to start a new game.
4. **Enter Player Name and Start Game**
    1. Enter a player name into the blank text area.
    2. Select 'Start Game' and verify that the user is moved to the start game page, is greeted by their player name with instructions on answering the riddle, is presented with the first riddle, displays their name in a list of player names and displays a list of blank incorrect answers.
    3. Verify scrolling bar appear on player name list once the list is longer than the box.
        - **Bug 1** - After entering player name and selecting start game, browser error 'Method Not Allowed'.
            - **Issue** - `run.py` not updated with code to write player name to `players.txt`.
            - **Fix** - Updated `run.py` to write to `players.txt`.
        - **Bug 2** - Player name is appearing duplicated on the list of player names.
            - **Issue** - Player name is being stored in the player name list, with every correct and incorrect answer that is entered.
            - **Fix** - `Run.py` contained duplicated coding with every riddle answered to write player name to the player name list. Removed this code.
5. **Answer Riddles**
    1. Enter an answer in the blank text area.
    2. Select 'Submit' to be redirected to the next riddle if the answer is correct.
        - **Bug 1** - After entering correct answer, brower error 'ValueError' appeared.
            - **Issue** - JSON data is not reading.
            - **Fix** - Scanned `riddles.json` for to identify the issue. Removed comma at the end of last closing curly bracket.
6. **Enter Incorrect Answer**
    1. Enter an answer in the blank text area.
    2. Select 'Submit' to be redirected to answer the riddle again if the answer is incorrect.
    3. Verify that incorrect answers are displayed with a list of incorrect answers.
    4. Verify scrolling bar appear on incorrect answer list once the list is longer than the box.
7. **Answer all Riddles Correctly**
    1. Enter the correct answer for all riddles.
    2. Verfiy that the user is brough to an end of game message and have the option to restart the game via the navbar menu.
8. **Responsive Testing**:
    1. In Chrome, right click on the site and select 'inspect', to open the Chrome Dev tools.
    2. Select the toggle device icon at the top of the window, to open the responsive testing window.
    3. Test/walk through how all features and pages are rendering on each device size from Galaxy S5 to iPad Pro.
        - **Bug 1** - Terminal displaying error 'socket.error: [Errno 98] Address already in use [closed]'.
            - **Issue** - Did not select ctrl+c to stop run.py running prior to closing workspace, the following morning encountered this error. 
            - **Fix** - Researched solutions online, used stack overflow. In terminal, ran `lsof -i :8080` to locate port ID. Then ran `sudo kill -9 <process_id>` to kill process.
        - **Bug 2** - Application not responsive on smaller devices.
            - **Issue** - Bootstrap grid layout require changing.
            - **Fix** - Updated boostrap `<div>` tags with various classes and styling within the html files and retested until appliction fully responsive on all device sizes.

## Deployment
The following section describes the process to deploy this project to Heroku.

1. Via the IDE Linux Terminal, login to Heroku, using 'heroku login' command. Input Heroku login details.
2. Create new Heroku app, using 'heroku apps:create appname' command.
3. Push project to Heroku, using 'push -u heroku master' command.
4. Create scale, using 'heroku ps:scale web=1' command.
5. Login to Heroku and select newly created app.
6. Select settings. Select ‘Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
7. From 'More' menu on the top right, select 'Restart all dynos'.
8. View app: In settings, select Domain URL, NOT Git URL to view your hosted application.
9. Deployed via Heroku: [Riddle Game](https://iq-riddle-game.herokuapp.com/).

## Credits

### Content
- The Riddles for this website were copied from [Riddles Website](https://www.riddles.com/riddles).

### Media
- The photo used in this site was copied from [Background Photo](https://ak4.picdn.net/shutterstock/videos/16982824/thumb/1.jpg?i10c=img.resize(height:160)).

### Acknowledgements
- I received inspiration for this project from my own interest in IQ tests, [Bootstrap](https://getbootstrap.com/) and ongoing research online. I also used knowledge gained from the [Code Institute](https://www.codeinstitute.net/), Diploma in Software Development. Stack Overflow, W3 Schools, YouTubers, 




