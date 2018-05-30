![Alt text](https://udemy-images.udemy.com/course/750x422/913448_e6e2.jpg)
### Flask-Python Game *** Update Photo/Name ***
A **Multi-Player Guessing Game** that asks player/s to guess the answer to a pictorial or text-based riddle.

### Functionalities
1. Player/s are presented with an image or text that contains the riddle.
2. Player/s enter their answer into a text area and submit their answer using a form.
3. If a player guesses correctly, they are redirected to the next riddle.
4. If a player guesses incorrectly, their incorrect guess is stored and printed below the riddle. The text area is cleared so they can guess again.
5. Multiple players can play an instance of the game at the same time. Players are identified by a unique username.
6. A leader board displays ranks and top scores for all users.

### Technologies

* Cloud 9: `Integrated Development Environment` used to build end to end.
* Cloud 9 Linux Terminal: Backup project via incremental `Git Commit` commands.
* Bootstrap CSS: Maintain clear separation between the library code and your code. Explain what code was kept and how it was changed to fit your need.
* Flask: Use to run game.
* Python: Use to write the logic of the game, including TDD (Test Driven Development).
* Main HTML: Use to enhance look and feel of the game.
* Custom CSS: Use to enhance look and feel of the game.
* Custom JavaScript: Use to enhance look and feel of the game.
* Chrome Dev Tools: Ongoing inspection of elements and to perform final UAT.
* Heroku: Final Project Deployment.
* Commentary: Check code clearly commented and update where required.

### Build Deployment
* Spellcheck

### Testing
* TDD (Test Driven Development): 
    - Automated Testing. Summarise and provide pseudocode you have written to develop your tests.
    - Python Unittest module. Ensures program runs correctly, if not, unittest will show you where code is not working. 'python3 -m unittest', to run tests
* Manual Testing: 
    - Describe the process by which you made sure that the functionality all works as intended.
            Flask Build - Ongoing checking via 'Run'.
            Executing code via Linux Terminal.
    - Structure around the list of scenarios - e.g. I clicked on the Videos link in the navbar, then clicked play to verify that the video plays correctly and clicked download to verify that I could download it to my computer.
    - Ensure site is as responsive as possible, test on different size devices.
* Bugs:
    - Describe any interesting bugs (tests not running as expected/failing). Describe expected output, why testing may be failing, how you addressed them, and whether there were any issues that you didn't/couldn't fix.
    

    * Bugs
    Unable to get code working in browser - spelled end block, which should have been one word i.e. endblock.
    'Contact Developer' missing: Typo in page_heading, fixed by correcting/aligning wording conventions.
    Forgot 'secret_key' leading to error code, fixed by adding to run.py.

### Final Deployment
* Heroku: Deploy final version of code. Provide instructions on how project was deployed to Heroku.

### Developer 'To Do' Notes

* Current iteration = i1.
* Subsequent iterations:

    1. Run code through validator/s.
    2. Review E2E (incl. code commentary). Apply improvements.
    