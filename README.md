![Alt text](https://ak4.picdn.net/shutterstock/videos/16982824/thumb/1.jpg?i10c=img.resize(height:160))

### IQ Question Game
A game that asks player/s to input the answer to IQ text based questions.

### Game Instructions
1. Player/s are presented with text that contains the question.
2. Player/s enter their answer into a text area and submit their answer using a form.
3. If a player guesses correctly, they are redirected to the next riddle.
4. If a player guesses incorrectly, their incorrect guess is stored and printed below the riddle. The text area is cleared so they can guess again.
5. Multiple players can play an instance of the game at the same time. Players are identified by a unique username.

### Technologies

* Cloud 9: `Integrated Development Environment` used to build end to end.
* Cloud 9 Linux Terminal: Backup project via incremental `Git Commit` commands.
* Bootstrap CSS: Static folder is Bootstrap, base body/contact form was copied from Bootstrap. All other code is project owners, freehand and retrieved from online forums. Maintain clear separation between the library code and your code. Explain what code was kept and how it was changed to fit your need.
* Flask: Use to run game.
* Python: Use to write the logic of the game, including TDD (Test Driven Development).
* Main HTML: Use to enhance look and feel of the game.
* Custom CSS: Use to enhance look and feel of the game.
* Custom JavaScript: Use to enhance look and feel of the game.
* Chrome Dev Tools: Ongoing inspection of elements and to perform final UAT.
* Heroku: Final Project Deployment.
* Commentary: Check code clearly commented and update where required.
* Riddle Question Source/s: 

### Build Deployment
* Spellcheck

### Testing
* TDD (Test Driven Development): 
    - Automated Testing. Summarise and provide pseudocode you have written to develop your tests.
    - Python Unittest module. Ensures program runs correctly, if not, unittest will show you where code is not working. 'python3 -m unittest', to run tests
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

### Final Deployment
* Heroku: Deploy final version of code. Provide instructions on how project was deployed to Heroku.

1. Blank `Cloud 9` workspace created. Folders set up and files uploaded/created in line with wireframe.
2. `index.html`, `graph.js` and `style.css` updated in parallel. HTML, CSS, and JavaScript code written for each section. See code commentary for detailed guidance.
3. UAT: Final web design inspected via `Cloud 9`, `Run`. Responsive web design tested via `Chrome Dev Tools`, `Toggle Device Toolbar`. ``` D3 data visualisation is non-responsive and built for large screens``` therefore, `Bootstrap` containers ONLY are responsive.
4. Staged Project Backup: Pushed to `GitHub` repo via `Linux` terminal in incremental stages.

Final Project Backup: Pushed to `GitHub` repo via `Linux` terminal.
Deployed via GitHub Pages: [insert heroku link to view app]


### Developer 'To Do' Notes

* Current iteration = i1.
* Subsequent iterations:

    1. Run code through validator/s.
    2. Review E2E (incl. clarity of code by refactoring and code commentary). Apply improvements.
    3. Increase number of riddles, add automated TDD (Test Driven Development) if drives beneficial.
    4. Add numercal scoring system and leaderboard ranking all historic players by highest to lowest scores.
    5. Remove brackets around player name on incorrect answer list, streamline to align styling with players list.
    