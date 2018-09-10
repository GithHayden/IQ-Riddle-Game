![Alt text](https://ak4.picdn.net/shutterstock/videos/16982824/thumb/1.jpg?i10c=img.resize(height:160))





# The Beach Boys

This website is a static (front-end only) application for The Beach Boys, 1960's rock band. The primary target audiences are fans, potential fans and customers. Users can sign up for news, read an overview about the band, watch and download videos, listen to and download audio tracks, contact the band, request a booking and follow the band on social media.

## UX

The following section describes the UX process for this project.

#### UX Process
1. **The Beach Boys** - Reviewed The Beach Boys videos, music and website to understand this genre, fans, potential fans and customers.
2. **Layout** - Reviewed Code Institute learnings to date, Bootstrap documentation and templates to extract design ideas.
3. **User Stories** - Walked through user stories.
    1. **Photo of the band** - As a fan, potential fan or customer, I want to view an up-to-date photo of the band to get a sense of their vibe.
    2. **Subscribe to News** - As a fan, potential fan or customer, I want to subscribe to The Beach Boys news, to receive updates on the bands members, their concerts and new music.
    3. **About** - As a fan, potential fan or customer, I want to read a summary about The Beach Boys, to understand their background to date.
    4. **Videos** - As a fan, potential fan or customer, I want to watch The Beach Boys videos, for entertainment, to download videos and to see their performances should I choose to book them for an event or a live concert.
    5. **Audio** - As a fan, potential fan or customer, I want to listen to The Beach Boys audio tracks, for entertainment, to download audio tracks and to listen to their music should I choose to book them for an event or a live concert.
    6. **Contact** - As a fan, potential fan or customer I want to be able to contact the band, to submit feedback or request to book the band for an event.
    7. **Social Media Icons** - As a fan, potential fan or customer I want to be able to follow the band on social media, to be a part of their journey and interact with them online.
4. **Wireframe** - Sketched the wireframe on paper, to include a section for each user story, delivering a clear design to connect the bands needs to the user’s needs.

## Features
 
### Existing Features

The following section describes all the front-end features in this project.

1. **The Beach Boys** - Landing page navbar menu item. When selected moves users to the landing page, which is a photo of the band with a call to action text. This section also has a Sign-Up button, when selected, a modal appears, where users can complete their details and submit, to sign up to news.
2. **About** - About navbar menu item. When selected moves users to view the about section, which contains a summary about The Beach Boys, to understand the bands background.
3. **Videos** - Video navbar item. When selected moves users to view the video section which showcases the bands videos, for entertainment, to download videos and to see their performances should a user choose to book them for an event or live gig.
4. **Audio** - Audio navbar item. When selected moves users to listen to audio tracks of the band which showcases audio tracks, for entertainment, to download and to listen to their music should a user choose to book them for an event or live gig.
5. **Contact** - Contact navbar item. When selected moves the users to the contact section, to be able to contact the band, to submit feedback or to book the band for an event.
6. **Social Media Icons** - Icons for Facebook, Twitter and Youtube, when selected moves users to each social media page. Allows users to be a part of the bands journey and interact with them online.

### Features to Implement
1. **Merchandise** - Add a feature to sell the bands merchandise.
2. **Book live concerts** - Add a feature to allow fans to purchase tickets via this website.
3. **Live concert schedule** - Add a feature to show a summary of the bands concert schedule.
4. **Videos** - Upgrade the video feature to a horizontal, automatic, video slider to enhance UX/UI.
5. **Audio Tracks** - Upgrade the video feature to a horizontal, automatic, video slider with track photo image, to enhance UX/UI.

## Technologies Used

The following section describes all technologies and tools used to construct this project.

- [Cloud 9 IDE](https://aws.amazon.com/cloud9/)
    - The project used **Cloud 9**, online integrated development environment, to construct the code end to end.
- [Bootstrap Template](https://github.com/BlackrockDigital/startbootstrap-scrolling-nav)
    - This project uses **Bootstrap Nav scrolling bar template**. A blank template with a main navigation and grid layout. This blank template was used as a starting block and tailored/built upon for this specific website. The `index.html` and `main.css` files are predominantly all, the developers code. All other code was included with the Bootstrap template.
- [Font Awesome](https://fontawesome.com/)
    - This project uses **Font Awesome**, a library of icons, to add the social media icons within the footer.
- [HTML](https://en.wikipedia.org/wiki/HTML)
    - This project uses **HTML**, the standard mark-up language used to build website layout, which was written within the `index.html` file.
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - This project uses **CSS**, a style sheet language, used to add styling to a website. The `main.css` file was added to this project, to add additional styling on top of the Bootstrap template.
- [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools/)
    - This project uses **Chrome Dev Tools**, a set of web developer tools, to continuously test and inspect that the web pages are rendering as expected within the browser.
- [GitHub](https://github.com/)
    - This project uses **GitHub**, a web hosting service, for version control and final project deployment.
- [All Other Technologies](https://github.com/BlackrockDigital/startbootstrap-scrolling-nav)
    - All other technologies within this project were included with the Bootstrap template.

## Testing

The following is an overview of testing to ensure all functionality works as intended in this project.

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

> **Note:** During development, a push to a new GitHub repo resulted in earlier git commits lost.

## Credits

### Content
- The text for the About section was copied from [Wikipedia](https://en.wikipedia.org/wiki/The_Beach_Boys).

### Media
- The photo used in this site was copied from [WWMT.com](https://wwmt.com/news/local/the-beach-boys-to-headline-tulip-time-2018-tickets-on-sale-nov-9).
- The videos and audio tracks in this site were copied from [YouTube](https://www.youtube.com/). They were then converted to MP4 and MP3 files.

### Acknowledgements

- I received inspiration for this project from The Beach Boys videos, music and website, from Bootstrap template designs, from ongoing research online and from Code Institute education.






























### Riddle Game
A game that asks players to input answers to text based riddles.

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
    * **All other code**: Compiled by developer from knowledge gained and online researching - frequently using stack overflow, W3 Schools and YouTube videos.
3. **Flask**: A python microframework used to build and run the application. Flask offers beneficial functionality such as template logic, which allows the `base.html` file to be inherited on other html files via `{% extends 'base.html' %} {% block content %} {% endblock %}` code.
4. **Python code**: Written within `run.py`. Used to write the logic of the game.
5. **HTML files**: Used to build the structure of each application page.
6. **JSON file**: Used as a database to retrieve riddle question and answers.
7. **Text files**: Used to write to and read from via python back end code e.g. write player name to `players.txt` when player inputs name on form and selects start game.
8. **Chrome Dev Tools**: Used to execute inspection of application in browser and to perform UAT, including responsive testing.
9. **Git and GitHub**: Used for version control and to deploy a backup of the project.
10. **Heroku**: Used to deploy and host final project.

### Development Process
1. **Workspace**: Blank `Cloud 9` workspace created.
2. **README.md**: Created with outline of the project and developed as project progressed.
3. **Folders and files**: Created in line with wireframe and developed as project progressed.
4. **Bootstrap**: [Clean Blog Template](https://startbootstrap.com/template-overviews/clean-blog/) files uploaded to static folder and used as boilerplate for design.
5. **HTML files**: Developed with own code/commentary on top of bootstrap template code, e.g. overwriting photo and renaming nav bar to align with this project design. 
6. **Run.py**: Flask and python back end code developed to render application in web browser and execute functionality.
7. **Commentary**: Developed throughout files to provide code guidance.
8. **Cloud 9 Linux Terminal**: Used to backup project via incremental `git status, git add <file/s> (staging area), git commit -m "<commentary>"` commands.

### Testing
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