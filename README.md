![Alt text](https://ak4.picdn.net/shutterstock/videos/16982824/thumb/1.jpg?i10c=img.resize(height:160))





# US Equity Markets 2017

This website is a **SPA** (Single Page Application) **Data Visualisation Dashboard Interface** which harnesses, the power of [D3.js](https://d3js.org/), a Javascript library for charting, created by Mike Bostock. The primary target audience is any user who wants to gain a comparable analysis of all NASDAQ and NYSE equities priced under USD$50, at 2017 year end.

This SPA site provides users with a drop-down selector, pie charts, bar charts and a scatter plot chart. Providing data visualisation across a number of dimensions i.e. by sector, by industry, number of equities, market capitalisation, domiciled by country, volume and price.

## UX

The following section describes the UX process for this project.

#### UX Process
1. **US Equity Markets** - Using my own knowledge, sketched out potential sets of data to include within a dashboard.
2. **Layout** - Reviewed the Code Institute learnings to date, Bootswatch themes and D3.js documentation to extract design ideas.
3. **User Stories** - Walked through user stories.
    1. **About** - As a user, I want to clearly understand the purpose of this dashboard and the data included.
    2. **User Guidance** - As a user, I want to to clearly understand how to use this dashboard.
    3. **Select Industry** - As a user, I want to be able to drill into each sector by industry type.
    4. **Number of Equities by Sector** - As a user, I want to be able to view the number of equities by sector and drill into each sector by industry type.
    5. **Market Capitalisation by Sector** - As a user, I want to be able to view the market capitalisation by sector and drill into each sector by industry type.
    6. **Market Capitalisation by Domiciled Country** - As a user, I want to be able to view the market capitalisation by domiciled country and drill into each sector by industry type.
    7. **Average Daily Volume by Sector** - As a user, I want to be able to view the average daily volume by sector and drill into each sector by industry type.
    8. **Average Daily Volume by Domiciled Country** - As a user, I want to be able to view the average daily volume by domicilied country, by sector and drill into each sector by industry type.
    9. **Average Daily Volume per Equity by Sector** - As a user, I want to be able to view the average daily volume per equity, by sector and drill into each sector by industry type.
    10. **Average Daily Volume per Equity Vs. Price per Equity** - As a user, I want to be able to view the average daily volume per equity Vs. price per equity, by sector and drill into each sector by industry type.
4. **Wireframe** - Sketched the wireframe on paper, to include the features for each user story, meeting the users needs by presenting the data on a dashboard charting web application.

## Features
 
### Existing Features

The following section describes all the front-end features in this project.

1. **About** - Provides users with a description of the dashboards purpose and what data is included.
2. **User Guidance** - Provides users with guidance on how to use the dashboard.
3. **Select Industry** - A drop-down selector, allowing users to select all or a specific industry. When a selection is made, each chart is automatically upated with the relevant industry data. Allows users to reset all charts by selecting 'Select all'.
4. **Number of Equities by Sector** - A bar chart displaying 'Number of Equities by Sector', which is updated by industry when a user makes a selection, using the 'Select Industry' drop-down selector. When a selection is made, each chart is automatically upated with the relevant industry data. The bar chart provides an X and Y axis, visualisation of relevant data, and is useful for understanding comparisons.
5. **Market Capitalisation by Sector** - A pie chart displaying 'Market Capitalisation by Sector', which is updated by industry when a user makes a selection, using the 'Select Industry' drop-down selector. When a selection is made, each chart is automatically upated with the relevant industry data. Provides subset visualisation of all parts and is useful for understanding the whole picture.
6. **Market Capitalisation by Domiciled Country** - A pie chart displaying 'Market Capitalisation by Domiciled Country', which is updated by industry when a user makes a selection, using the 'Select Industry' drop-down selector. When a selection is made, each chart is automatically upated with the relevant industry data. Provides subset visualisation of all parts and is useful for understanding the whole picture.
7. **Average Daily Volume by Sector** - A pie chart displaying 'Average Daily Volume by Sector', which is updated by industry when a user makes a selection, using the 'Select Industry' drop-down selector. When a selection is made, each chart is automatically upated with the relevant industry data. Provides subset visualisation of all parts and is useful for understanding the whole picture.
8. **Average Daily Volume by Domiciled Country** - A pie chart displaying 'Average Daily Volume by Domiciled Country', which is updated by industry when a user makes a selection, using the 'Select Industry' drop-down selector. When a selection is made, each chart is automatically upated with the relevant industry data. Provides subset visualisation of all parts and is useful for understanding the whole picture.
9. **Average Daily Volume per Equity by Sector** - A bar chart displaying 'Average Daily Volume per Equity by Sector', which is updated by industry when a user makes a selection, using the 'Select Industry' drop-down selector. When a selection is made, each chart is automatically upated with the relevant industry data. The bar chart provides an X and Y axis, visualisation of relevant data, and is useful for understanding comparisons.
10. **Average Daily Volume per Equity Vs. Price per Equity** - A scatter plot chart displaying 'Average Daily Volume per Equity Vs. Price per Equity', which is updated by industry when a user makes a selection, using the 'Select Industry' drop-down selector. When a selection is made, each chart is automatically upated with the relevant industry data. Provides an X and Y axis, visualisation of relevant data, and is useful for understanding correlation/distribution.

### Features to Implement
1. **Interactive Tutorial** - Add a feature to include an interactive tutorial.
2. **Comma Seperator** - Update hoover metrics to include a comma seperator.
3. **X and Y axis** - Update to implement improved ways to style both axis's.
4. **Icons** - Add icons where more streamlined design can be achieved.

## Technologies Used

The following section describes all technologies and tools used to construct this project.

- [Cloud 9 IDE](https://aws.amazon.com/cloud9/)
    - The project used **Cloud 9**, online integrated development environment, to construct the code end to end.
- [Comma-separated values file](https://en.wikipedia.org/wiki/Comma-separated_values)
    - This project uses a .csv file, which stores tabular data (numbers and text) in plain text. The `Equities.csv` file contains the dataset that populates the front-end charts for this project.
- [Bootswatch](https://bootswatch.com)
    - This project uses **Bootswatch**, a library of Bootstrap themes. The `flatly theme`, `bootstrap.min.css` file was used for this project.
- [DC](https://dc-js.github.io/dc.js/)
    - This project uses **DC.js**, a javascript charting library with native crossfilter support, allowing highly efficient exploration on large multi-dimensional datasets. It leverages D3 to render charts in CSS-friendly SVG format.
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - This project uses **CSS**, a style sheet language, used to add styling to a website. The `style.css` file was added to this project, to build additional styling on top of the Bootswatch theme.
- [Crossfilter](http://square.github.io/crossfilter/)
    - This project uses **Crossfilter**, a JavaScript library for exploring large multivariate datasets in the browser. 
- [D3](https://d3js.org/)
    - This project uses **D3.js**, a JavaScript library for manipulating documents based on data. D3 helps you bring data to life using HTML, SVG, and CSS, producing interactive data visualizations.
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
    - This project uses **Javascript**, an object-oriented programming language used to create interactive effects within web browsers.
- [D3-Queue](https://github.com/d3/d3-queue)
    - This project uses **D3-Queue**, which assists with loading files and defers calling function, until the data is ready.
- [HTML](https://en.wikipedia.org/wiki/HTML)
    - This project uses **HTML**, the standard mark-up language used to build website layout, which was written in this project within the `index.html` file.
- [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools/)
    - This project uses **Chrome Dev Tools**, a set of web developer tools, to continuously test and inspect that the web pages are rendering as expected within the browser.
- [GitHub](https://github.com/)
    - This project uses **GitHub**, a web hosting service, for version control and final project deployment.

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