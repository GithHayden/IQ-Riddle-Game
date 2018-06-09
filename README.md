![Alt text](https://ak4.picdn.net/shutterstock/videos/16982824/thumb/1.jpg?i10c=img.resize(height:160))

### IQ Riddle Game
A game that asks player/s to input answer/s to IQ text based riddles.

### Game Instructions
1. Player/s enter a unique player name using a form and select start game.
2. Player/s are then presented with a riddle.
3. Player/s enter their answer using a form and select submit.
4. If a player answers correctly, they are redirected to the next riddle.
5. If a player answers incorrectly, their incorrect answer is stored and printed in an incorrect answers lists. The text area/form is then cleared so the player can guess again.
6. If a player answers all riddles correctly, they are redirected to an end of game message.

### Technologies
1. Cloud 9: IDE `Integrated Development Environment` used to build project end to end.
2. Cloud 9 Linux Terminal: Used to backup project via incremental `git status, git add (staging area), git commit` commands.
3. Bootstrap: [Bootstrap Clean Blog Template](https://startbootstrap.com/template-overviews/clean-blog/) used to build design upon.
    * Static folder contains Bootstrap files (no other files stored within this folder).
    * base.html and contact.html - most of the html code was copied from the bootstrap index.html and contact.html files.
    * All other project code was compiled by developer from knoweldge and online researching - frequently using stackoverflow.
4. Flask: A python microframework used to run the application.
5. Python: Written on run.py and used to write the logic of the game.
6. HTML files: Used to build the structure of each web application page.
7. JSON file: Used as a database containing riddle questions and answers.
8. Text files: Used to write and read data e.g. write player name to players.txt when user inputs name on front end.
9. Chrome Dev Tools: Used to execute ongoing inspection of application in browser and to perform final UAT, including responsive testing.
10. GitHub: Used to deploy a backup of project.
11. Heroku: Used to deploy final project.

### Build Deployment
1. Workpsace: Blank `Cloud 9` workspace created.
2. README.md: Created with rough brief on project.
3. Folders and blank files: Created in line with wireframe. 
4. Bootstrap: [Bootstrap Clean Blog Template](https://startbootstrap.com/template-overviews/clean-blog/) files uploaded as base design.
5. HTML files: Developed with own coding on top of bootstrap template code e.g. adding own photo, renaming nav bar to suit this project design. 
6. Run.py file: Flask and python back end code created to execute commands and render application in web browser.
7. Code commenatry: See throughout files for code guidance.
8. Spellcheck: All non code data spellchecked.
9. UAT: Final application inspected via `Cloud 9`, `Run`. Responsive web design tested via `Chrome Dev Tools`, `Toggle Device Toolbar`. ``` D3 data visualisation is non-responsive and built for large screens``` therefore, `Bootstrap` containers ONLY are responsive.
10. Staged Project Backup: Pushed to `GitHub` repo via `Linux` terminal in incremental stages.
11. Final Project Backup: Pushed to `GitHub` repo via `Linux` terminal.
12. Deployed via Heroku: 
13. Test live project end to end including responsive.

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

### Final Deployment
* Heroku: Deploy final version of code. Provide instructions on how project was deployed to Heroku.

1. Blank `Cloud 9` workspace created. Folders set up and files uploaded/created in line with wireframe.
2. `index.html`, `graph.js` and `style.css` updated in parallel. HTML, CSS, and JavaScript code written for each section. See code commentary for detailed guidance.
3. UAT: Final web design inspected via `Cloud 9`, `Run`. Responsive web design tested via `Chrome Dev Tools`, `Toggle Device Toolbar`. ``` D3 data visualisation is non-responsive and built for large screens``` therefore, `Bootstrap` containers ONLY are responsive.
4. Staged Project Backup: Pushed to `GitHub` repo via `Linux` terminal in incremental stages.

### Developer 'To Do' Notes

* Current iteration = i1.
* Subsequent iterations:

    1. Review E2E (incl. clarity of code by refactoring and code commentary). Apply improvements.
    2. Increase number of riddles, add automated TDD (Test Driven Development) if drives beneficial.
    3. Add numercal scoring system and leaderboard ranking all historic players by highest to lowest scores.
    4. Remove brackets around player name on incorrect answer list, streamline to align styling with players list.
    