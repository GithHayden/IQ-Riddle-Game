![Alt text](https://ak4.picdn.net/shutterstock/videos/16982824/thumb/1.jpg?i10c=img.resize(height:160))

### IQ Riddle Game
A game that asks player/s to input answer/s to IQ text based riddles.

### Game Instructions
1. Player/s enter a unique player name using a form and select start game.
2. Player/s are then presented with a riddle.
3. Player/s enter an answer using the form and select submit.
4. If a player answers correctly, they are redirected to the next riddle.
5. If a player answers incorrectly, their incorrect answer is stored and printed in an incorrect answers lists. The text area/form is then cleared so the player can guess again.
6. If a player answers all riddles correctly, they are redirected to an end of game message.

### Technologies
1. Cloud 9: IDE `Integrated Development Environment` used to build project end to end.
2. Bootstrap: [Bootstrap Clean Blog Template](https://startbootstrap.com/template-overviews/clean-blog/) used as boilerplate design.
    * Static folder: Contains Bootstrap files (no other files stored within this folder).
    * `base.html` and `contact.html` - most of the html code was copied from the bootstrap `index.html` and `contact.html` files.
    * All other code: Compiled by developer from knoweldge and online researching - frequently using stackoverflow, W3 Schools and YouTube videos.
3. Flask: A python microframework used to build and run the application. Flask offers benficial functionality such as template logic, which allows the `base.html` file to be inherited on other html files via `{% extends 'base.html' %} {% block content %}` code.
4. Python: Written within `run.py`. Used to write the logic of the game.
5. HTML files: Used to build the structure of each application page.
6. JSON file: Used as a database to point to. Contains the riddle questions and answers.
7. Text files: Used to write and read data via python back end code e.g. write player name to `players.txt` when player inputs name on form.
8. Chrome Dev Tools: Used to execute inspection of application in browser and to perform final UAT, including responsive testing.
9. GitHub: Used to deploy a backup of project.
10. Heroku: Used to deploy and host final project.

### Build Deployment
1. Workpsace: Blank `Cloud 9` workspace created.
2. README.md: Created with outline of project.
3. Folders and files: Created in line with wireframe and developed as project progressed.
4. Bootstrap: [Clean Blog Template](https://startbootstrap.com/template-overviews/clean-blog/) files uploaded to use as boilerplate for design.
5. HTML files: Developed with own code/commentary on top of bootstrap template code, e.g. overwriting photo and renaming nav bar to align with this project design. 
6. Run.py file: Flask and python back end code developed to execute commands and render application in web browser.
7. Commenatry: Developed throughout files for code guidance.
8. README.md: Developed as project progressed.
9. Cloud 9 Linux Terminal: Used to backup project via incremental `git status, git add <file/s> (staging area), git commit -m "<commentary>"` commands.

### Testing
1. Manual testing, ongoing via `Cloud 9`, `Run`. After all changes, big or small, checked applciation and all functionality running correctly in browser. 

    1. Index.html: Selected all nav bar menus to verify that all menus operate as intended.
        1. Bug/Expected Output - code not rendering in browser. Issue - At end of html files spelled {% end block %}. Fix - Scanned code and researched online. Updated with no space i.e. {% endblock %}.
        2. Bug/Expected Output - contact page missing 'Contact Developer' heading. Issue - Typo in {{ page_heading }} on contact.html and code not reading from run.py. Fix - Checked relevant code and updated typo to ensure {{ page_heading }} spelled the same as code on run.py.
        3. Bug/Expected Output - header photo skewe/poor look. Issue - pixel sizing not in line with bootstrap design. Fix - Researched online until located appropriatly sized photo to fit bootstrap template.
        4. Bug/Expected Output - after inputing player name and selecting Start Game, browser error 'Method Not Allowed'. Issue - run.py not updated with code to write player name to players.txt. Fix - Developed run.py to include relevant code to write to players.txt.
        5. Bug/Expected Output - form and button hugging each other too closely. Issue - Bootstrap grid system not implemented. Fix - Added divs and html style code to create spacing.
        6. Bug/Expected Output - terminal displaying error 'socket.error: [Errno 98] Address already in use [closed]'. Issue - didn't select ctrl+c and stop run.py prior to closing workspace, following morning encountered this error. Fix - researched solutions online, used stackoverflow. Ran 'lsof -i :8080' to locate port ID. Then ran sudo kill -9 <process_id> to kill process.
    2. Game: Input a test player name and selected Start Game to verify player is redirected to start the game. Answered questions incorrectly to verify incorrect answers are being stored within the appropriate list. Answered all riddles correctly to verify that the form is cleared, that the player is redirected to the next riddle and when all riddles are answered correctly the player is redirected to the end of game message.
        1. Bug/Expected Output - after inputting answer, browser error 'ValueError'. Issue - json data not reading, throwing up this error. Fix - Scanned json file for irregularities/try to identify issue. Removed comma at end of last closing curly bracket which fixed this bug.
        2. Bug/Expected Output - during inputting all correct answers, player name is being duplicated within player name list. Issue - [OPEN BUG, NOTED WITHIN TO DO NOTES TO FIX]
        3. Bug/Expected Output - form and button hugging each other too closely. Issue - Bootstrap grid system not implemented. Fix - Added divs and html style code to create spacing.
        4. Bug/Expected Output - after updating commentary, error in browser pointing to {{ curley brackets. Issue - updated commentary to state that the code within {{ }} is flask code. The browser is trying to read this as code. Fix - updated {{ }} to the words, curley brackets.
    3. Contact: Input required data on relevant lines in form and selected send to verify that each line of the form works as expected.
    4. Responsive Testing: Used Chrome Dev tools to inspect application on various device sizes.
        1. Bug/Expected Output - Startgame.html not responsive and skewed on all but a large screen. Issue - Issue - [OPEN BUG, NOTED WITHIN TO DO NOTES TO FIX]

### Final Deployment
1. README.md: Finalised and spell checked.
2. Backup deployed via Github: [GitHub Backup](https://github.com/GithHayden/IQ-Riddle-Game).
3. Website Deployed via Heroku: [IQ Riddle Game]()

```
DEPLOY TO HEROKU INSTRUCTIONS
1.
2.
3.
4.
5.
6.


```   

### Developer To Do Notes
1. Review E2E (incl. clarity of code by refactoring and code commentary). Apply improvements.
2. Revise startgame.html to be responsive on all screen sizes.
3. Revise startgame.html player/s list to not include duplicated name with every correct answer input.
4. Remove brackets around player name on incorrect answer list, streamline to align styling with players list.
5. Increase number of riddles, add automated TDD (Test Driven Development) if beneficial.
6. Add numercal scoring system and leaderboard ranking all historic players by highest to lowest scores.