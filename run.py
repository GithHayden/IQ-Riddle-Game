import os
import json

from flask import Flask, render_template, request, flash, redirect, jsonify

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'a_secret')

PLAYERS_FILE = "data/players.txt"
GAME_PLAYERS_FILE = "data/game_players.txt"
INCORRECT_ANSWERS_FILE = "data/incorrect_answers.txt"

data = []

def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)

def add_users(username):
    """Add player name to the `players` text file"""
    write_to_file(PLAYERS_FILE,"({0}) {1} - {2)\n".format
        (username.title()))

def get_all_users():
    """Get all of the players names from the 'players. text file"""
    users = []
    with open(PLAYERS_FILE, "r") as user_messages:
        users = user_messages.readlines()
    return users    
    
def add_messages(username, message):
    """Add incorrect answers to the `incorrect_answers` text file"""
    write_to_file(INCORRECT_ANSWERS_FILE, "({0}) - {1}\n".format(
            username.title(),
            message))

def get_all_messages():
    """Get all of the incorrect answers from the 'incorrect_answers' text file"""
    messages = []
    with open(INCORRECT_ANSWERS_FILE, "r") as incorrect_answers:
        messages = [row for row in incorrect_answers if len(row.strip()) > 0]
    return messages
    
@app.route('/users/online', methods=["GET", "POST"])
def game_players():
    '''Routing view for players after player name is input'''
    game_players_file = open(GAME_PLAYERS_FILE)
    game_players = [row for row in game_players_file if len(row.strip()) > 0]
    game_players_file.close()

    return jsonify(game_players)    

@app.route('/', methods=["GET", "POST"])
def index():
    '''Routing view to render/call index.html in the browser'''
    # POST request
    if request.method == "POST":
        write_to_file(PLAYERS_FILE, request.form["username"] + "\n")
        write_to_file(GAME_PLAYERS_FILE, request.form["username"] + "\n")
        return redirect(request.form["username"])
        
    return render_template("index.html", page_heading="Play Game")
    
@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    """Routing view to display the riddles, from the riddles.json file"""
    data = []
    with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)

    riddle_index = 0

    if request.method == "POST":

        # Get riddle index from hidden field passed in form.
        riddle_index = int(request.form["riddle_index"])

        # Retrieve player response from input field completed by player.
        # Convert answer to lowercase to accept uppercase as correct answer.
        user_response = request.form["message"].lower()

        # Compare players answer to the correct answer.
        if data[riddle_index]["answer"] == user_response:
            # Correct answer
            # Go to next riddle
            riddle_index += 1
        else:
            # Incorrect answer.
            add_messages(username, user_response + "\n")

    if request.method == "POST":
        if user_response == "river" and riddle_index > 10:
            return render_template("gameover.html")

    messages = get_all_messages()

    game_players_file = open(GAME_PLAYERS_FILE)
    game_players = [row for row in game_players_file if len(row.strip()) > 0]
    game_players_file.close()

    return render_template("startgame.html",
                            username=username, incorrect_answers=messages, riddles_data=data, game_players=game_players, riddle_index=riddle_index)

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        '''Routing view to render/call contact.html in browser'''
        flash("Thank you {} for your message, we will respond soon.".format(
            request.form["name"]))
            
    return render_template("contact.html", page_heading="Contact Developer")

if __name__== '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            #If debug=True not included, changes will not render in the browser.
            debug=True)
