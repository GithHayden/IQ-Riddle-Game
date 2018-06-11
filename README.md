![Alt text](https://ak4.picdn.net/shutterstock/videos/16982824/thumb/1.jpg?i10c=img.resize(height:160))

### IQ Riddle Game
A game that asks player/s to input answer/s to IQ text based riddles.

### Game Instructions
1. Player enters a unique player name, using a form and selects start game.
2. Players name is stored and displayed in a list. Player is then presented with a riddle.
3. Player enters an answer to the riddle, using the form and selects submit.
4. If a player answers correctly, the player is redirected to the next riddle.
5. If a player answers incorrectly, the incorrect answer is stored and displayed in a list. The answer form is then cleared so the player can enter an answer again.
6. If a player answers all riddles correctly, they are redirected to an end of game message.

### Technologies
1. **Cloud 9**: IDE `Integrated Development Environment` used to build project end to end.
2. **Bootstrap**: [Bootstrap Clean Blog Template](https://startbootstrap.com/template-overviews/clean-blog/) used as boilerplate design.
    * **Static folder**: Contains Bootstrap files (no other files stored within this folder).
    * **`base.html` and `contact.html`** - most of this html code was copied from the bootstrap `index.html` and `contact.html` files, then amended to suit this project.
    * **All other code**: Compiled by developer from knoweldge gained and online researching - frequently using stackoverflow, W3 Schools and YouTube videos.
3. **Flask**: A python microframework used to build and run the application. Flask offers benficial functionality such as template logic, which allows the `base.html` file to be inherited on other html files via `{% extends 'base.html' %} {% block content %} {% endblock %}` code.
4. **Python code**: Written within `run.py`. Used to write the logic of the game.
5. **HTML files**: Used to build the structure of each application page.
6. **JSON file**: Used as a database to retrieve riddle question and answers.
7. **Text files**: Used to write to and read from via python back end code e.g. write player name to `players.txt` when player inputs name on form and selects start game.
8. **Chrome Dev Tools**: Used to execute inspection of application in browser and to perform UAT, including responsive testing.
9. **Git and GitHub**: Used for version control and to deploy a backup of the project.
10. **Heroku**: Used to deploy and host final project.

### Build Deployment
1. **Workpsace**: Blank `Cloud 9` workspace created.
2. **README.md**: Created with outline of the project and developed as project progressed.
3. **Folders and files**: Created in line with wireframe and developed as project progressed.
4. **Bootstrap**: [Clean Blog Template](https://startbootstrap.com/template-overviews/clean-blog/) files uploaded to static folder and used as boilerplate for design.
5. **HTML files**: Developed with own code/commentary on top of bootstrap template code, e.g. overwriting photo and renaming nav bar to align with this project design. 
6. **Run.py**: Flask and python back end code developed to render application in web browser and execute functionality.
7. **Commenatry**: Developed throughout files to provide code guidance.
8. **Cloud 9 Linux Terminal**: Used to backup project via incremental `git status, git add <file/s> (staging area), git commit -m "<commentary>"` commands.

### Testing
**Manual testing**, ongoing via `Cloud 9`, `Run`. Once each functionality coded, checked application operating as expected in web browser by walking through each functionality. Testing included the following:

1. **Index.html**: Selected all nav bar menus to verify that all menus operated as intended. The following bugs were encountered.
    1. **Bug/Expected Output** - code not rendering in browser. **Issue** - At end of html files spelled {% end block %}. **Fix** - Scanned code. Updated with no space i.e. {% endblock %}.
    2. **Bug/Expected Output** - contact page missing 'Contact Developer' heading. **Issue** - Typo in {{ page_heading }} on contact.html and code not reading from run.py. **Fix** - Checked relevant code and updated typo to ensure {{ page_heading }} spelled the same as code on run.py.
    3. **Bug/Expected Output** - header photo skewed/not looking good. **Issue** - pixel sizing not in line with bootstrap design. **Fix** - Researched online until located appropriately sized photo to fit bootstrap template.
    4. **Bug/Expected Output** - after inputing player name and selecting start game, browser error 'Method Not Allowed'. **Issue** - run.py not updated with code to write player name to players.txt. **Fix** - Developed run.py to include relevant code to write to players.txt.
    5. **Bug/Expected Output** - form and button hugging each other too closely. **Issue** - Bootstrap grid system not implemented. **Fix** - Added divs and html style code to create spacing.
    6. **Bug/Expected Output** - terminal displaying error 'socket.error: [Errno 98] Address already in use [closed]'. **Issue** - didn't select ctrl+c to stop run.py running prior to closing workspace, the following morning encountered this error. **Fix** - researched solutions online, used stackoverflow. In terminal, ran 'lsof -i :8080' to locate port ID. Then ran sudo kill -9 <process_id> to kill process.
2. **Game**: Input a test player name and selected start game. Verifying player is redirected to a riddle and player name is being stored within the appropriate list. Answered riddles incorrectly to verify incorrect answers are being stored within the appropriate list. Answered all riddles correctly to verify that the form is cleared, that the player is redirected to the next riddle and when all riddles are answered correctly the player is redirected to the end of game message.
    1. **Bug/Expected Output** - after inputting correct answer, browser error 'ValueError'. **Issue** - json data not reading, throwing up this error. **Fix** - scanned json file for irregularities/to try and identify the issue. Removed comma at the end of last closing curley bracket.
    2. **Bug/Expected Output** - during inputting all correct answers, player name is being duplicated within player name list. **Issue** - THIS BUG IS LOGGED UNDER TO DO NOTES TO FIX.
    3. **Bug/Expected Output** - form and button hugging each other too closely. **Issue** - Bootstrap grid system not implemented. **Fix** - Added divs and html style code to create spacing.
    4. **Bug/Expected Output** - after updating commentary, error in browser pointing to {{ curley brackets. **Issue** - updated commentary to state that the code within {{ }} is flask code. The browser tried to read this as code. **Fix** - updated {{ }} to the words, curley brackets.
3. **Contact**: Input required data on relevant lines in form and selected send to verify that each line of the form operates as expected.
4. **Responsive Testing**: Used Chrome Dev tools to inspect application on various device sizes.
    1. **Bug/Expected Output** - Startgame.html not responsive and skewed on all but a large screen. **Issue** - THIS BUG IS LOGGED UNDER TO DO NOTES TO FIX.

### Final Deployment
1. **Backup deployed via Github**: [GitHub Backup](https://github.com/GithHayden/IQ-Riddle-Game).
2. **Website deployed via Heroku**: [IQ Riddle Game](https://iq-riddle-game.herokuapp.com/).
3. **README.md**: Finalised and spell checked. Push to GitHub/Heroku to capture updates.

```
HOW TO DEPLOY APPLICATION TO HEROKU
1. Via Linux Terminal, login to Heroku, using 'heroku login' command. Input Heroku login details.
2. Create new Heroku app, using 'heroku apps:create appname' command.
3. Push project to Heroku, using 'push -u heroku master' command.
4. Create scale, using 'heroku ps:scale web=1' command.
5. Login to Heroku and select newly created app.
6. Select settings. Select'Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
7. From 'More' menu on the top right, select 'Restart all dynos'.
8. View app: In settings, select Domain URL, NOT Git URL to view your hosted app.

```   

### Developer To Do Notes
1. **Bug** - Revise startgame.html to be responsive on all screen sizes.
2. **Bug** - Revise startgame.html player/s list to not include duplicated name with every correct answer input.
3. **Development** - Review end to end (incl. clarity of code by refactoring and code commentary). Apply improvements.
4. **Development** - Remove brackets around player name on incorrect answer list, streamline to align styling with players list.
5. **Development** - Increase number of riddles. If benefical, add automated TDD (Test Driven Development).
6. **Development** - Add numercal scoring system and leaderboard ranking all historic players by highest to lowest scores.