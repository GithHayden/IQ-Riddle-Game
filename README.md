![Alt text](https://ak4.picdn.net/shutterstock/videos/16982824/thumb/1.jpg?i10c=img.resize(height:160))

### IQ Riddle Game
A game that asks player/s to input answer/s to IQ text based riddles.

### Game Instructions
1. Player/s enter a unique player name using a form and select start game.
2. Player/s are then presented with a riddle to answer.
3. Player/s enter an answer using a form and select submit.
4. If a player answers correctly, they are redirected to the next riddle.
5. If a player answers incorrectly, their incorrect answer is stored and printed in an incorrect answers lists. The text area/form is then cleared so the player can guess again.
6. If a player answers all riddles correctly, they are redirected to an end of game message.

### Technologies
1. Cloud 9: IDE `Integrated Development Environment` used to build project end to end.
2. Cloud 9 Linux Terminal: Used to backup project via incremental `git status, git add <file/s> (staging area), git commit -m "<commentary>"` commands.
3. Bootstrap: [Bootstrap Clean Blog Template](https://startbootstrap.com/template-overviews/clean-blog/) used as boilerplate design.
    * Static folder: Contains Bootstrap files (no other files stored within this folder).
    * `base.html` and `contact.html` - most of the html code was copied from the bootstrap `index.html` and `contact.html` files.
    * All other code: Compiled by developer from knoweldge and online researching - frequently using stackoverflow, W3 Schools and YouTube videos.
4. Flask: A python microframework used to build and run the application. Flask offers benficial functionality such as template logic, which allows the `base.html` file to be inherited on other html files via `{% extends 'base.html' %} {% block content %}` code.
5. Python: Written within `run.py`. Used to write the logic of the game.
6. HTML files: Used to build the structure of each application page.
7. JSON file: Used as a database to point to. Contains the riddle questions and answers.
8. Text files: Used to write and read data via python back end code e.g. write player name to `players.txt` when player inputs name on form.
9. Chrome Dev Tools: Used to execute inspection of application in browser and to perform final UAT, including responsive testing.
10. GitHub: Used to deploy a backup of project.
11. Heroku: Used to deploy and host final project.

### Build Deployment
1. Workpsace: Blank `Cloud 9` workspace created.
2. README.md: Created with outline of project.
3. Folders and blank files: Created blank files in line with wireframe. Changed and updated as project progressed.
4. Bootstrap: [Bootstrap Clean Blog Template](https://startbootstrap.com/template-overviews/clean-blog/) files uploaded to use as boilerplate for design.
5. HTML files: Developed with own coding/commentary on top of bootstrap template code e.g. adding own photo, renaming nav bar to align with this project design. 
6. Run.py file: Flask and python back end code developed to execute commands and render application in web browser. Developer used own knowledge and coniderable time researching online predominantly for python assistance.
7. Commenatry: See throughout files for code guidance.
8. README.md: Updating perpetually as project progressed and finalised post iteration 1 tested end to end in browser.

### Testing
* Manual Testing: 
    - Describe the process by which you made sure that the functionality all works as intended.
            Flask Build - Ongoing checking via 'Run'.
            Resposive Testing.
            Executing code via Linux Terminal.
    - Structure around the list of scenarios - e.g. I clicked on the Videos link in the navbar, then clicked play to verify that the video plays correctly and clicked download to verify that I could download it to my computer.
    - Ensure site is as responsive as possible, test on different size devices.
* Bugs:
    - Describe any interesting bugs (tests not running as expected/failing). Describe expected output, why testing may be failing, how you addressed them, and whether there were any issues that you didn't/couldn't fix.
    
    * Bugs
    Unable to get code working in browser - spelled end block, which should have been one word i.e. endblock.
    'Contact Developer' missing: Typo in page_heading, fixed by correcting/aligning wording conventions.
    Forgot 'secret_key' leading to error code, fixed by adding to run.py.
    Design issues getting appropriately sized photo to align with app.
    Enter Player Name = Error 'Method Not Allowed. The method is not allowed for the requested URL'. Python write to files not within run.py.
    ValueError - json data not reading/throwing up error. Fixed jason code, remove comma at end of last closing curly bracket.
    duplicated data writing to player names and incorrect answers. Fixed by...
    Spacing/data hugging too closely between divs.
    Updated commentary to state that code within {{ }} is flask code. Error running app. Fied by changing {{ }} to 'curley brackets'.
    Player name writing to list with every answer submitted, duplicated data rendering. Fix.
    Startgame.html not responsive and skewed on smaller screens.
    socket.error: [Errno 98] Address already in use [closed] - fixed via stackoverflow solution. Ran 'lsof -i :8080' to locate port ID. Then ran sudo kill -9 <process_id> to kill process.

### Final Deployment
README: Finalised & spellchecked.
* Heroku: Deploy final version of code. Provide instructions on how project was deployed to Heroku.
Blank `Cloud 9` workspace created. Folders set up and files uploaded/created in line with wireframe.
`index.html`, `graph.js` and `style.css` updated in parallel. HTML, CSS, and JavaScript code written for each section. See code commentary for detailed guidance.
UAT: Final web design inspected via `Cloud 9`, `Run`. Responsive web design tested via `Chrome Dev Tools`, `Toggle Device Toolbar`. ``` D3 data visualisation is non-responsive and built for large screens``` therefore, `Bootstrap` containers ONLY are responsive.
Staged Project Backup: Pushed to `GitHub` repo via `Linux` terminal in incremental stages.

UAT: Final application inspected via `Cloud 9`, `Run`. Responsive web design tested via `Chrome Dev Tools`, `Toggle Device Toolbar`. ``` D3 data visualisation is non-responsive and built for large screens``` therefore, `Bootstrap` containers ONLY are responsive.
Staged Project Backup: Pushed to `GitHub` repo via `Linux` terminal in incremental stages.
Final Project Backup: Pushed to `GitHub` repo via `Linux` terminal.

### Developer 'To Do' Notes

* Current iteration = i1.
* Subsequent iterations:

    1. Review E2E (incl. clarity of code by refactoring and code commentary). Apply improvements.
    2. Revise startgame.html to be responsive on all screen sizes.
    3. Revise startgame.html player/s list to not include duplicated name with every correct answer.
    2. Increase number of riddles, add automated TDD (Test Driven Development) if drives beneficial.
    3. Add numercal scoring system and leaderboard ranking all historic players by highest to lowest scores.
    4. Remove brackets around player name on incorrect answer list, streamline to align styling with players list.
    