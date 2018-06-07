import os
import json

from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, jsonify

app = Flask(__name__)
app.secret_key = 'a_secret'

data = []

def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.writelines(data)

def add_users(username):
    write_to_file("data/players.txt","({0})-{1}\n".format(username.title()))
    
def get_all_users():
    users = []
    with open("data/players.txt", "r") as user_messages:
        users = user_messages.readlines()
    return users    
    
def add_messages(username, message):
    write_to_file("data/incorrect_answers.txt", "({0}) - {1}\n".format(
            username.title(),
            message))

def get_all_messages():
    messages = []
    with open("data/incorrect_answers.txt", "r") as chat_messages:
        messages = [row for row in chat_messages if len(row.strip()) > 0]
    return messages
    
@app.route('/users/online', methods=["GET"])
def online_users():
    online_users_file = open("data/game_players.txt")
    online_users = [row for row in online_users_file if len(row.strip()) > 0]
    online_users_file.close()

    return jsonify(online_users)    
    

@app.route('/', methods=["GET", "POST"])
def index():
    '''Routing view to render/call index.html in browser'''
    # POST request
    if request.method == "POST":
        write_to_file("data/players.txt", request.form["username"] + "\n")
        write_to_file("data/game_players.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
        
    return render_template("index.html", page_heading="Play Game")
    
    
    
@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    """Display chat messages"""
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)

    riddle_index = 0

    if request.method == "POST":
        # Add user to online users file because he is removed when he attempts to post his answer
        # as page considers him unloading the page
        write_to_file("data/game_players.txt", username + "\n")

        # Get riddle index from hidden field passed in form
        riddle_index = int(request.form["riddle_index"])

        # Get the user response from input field filled by user
        # We turn the answer to lower case because all answers are in lower case
        # so that SNOWBALLS can be as correct as snowballs
        user_response = request.form["message"].lower()

        # Compare the user's answer to the correct answer of the riddle
        if data[riddle_index]["answer"] == user_response:
            # Correct answer
            # Go to next riddle
            riddle_index += 1
        else:
            # Incorrect answer
            add_messages(username, user_response + "\n")

    if request.method == "POST":
        if user_response == "blueberry" and riddle_index > 10:
            return render_template("gameover.html")

    messages = get_all_messages()

    online_users_file = open("data/game_players.txt")
    online_users = [row for row in online_users_file if len(row.strip()) > 0]
    online_users_file.close()

    return render_template("startgame.html",
                            username=username, chat_messages=messages, company_data=data, online_users=online_users, riddle_index=riddle_index)

@app.route('/players', methods=["GET", "POST"])
def players(username):
    """Display chat historical of players"""

    if request.method == "POST":
        add_users(username, request.form["user"] + "\n")
    users = get_all_users()
    return render_template("game.html",
                            username=username)

@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect(username)

@app.route('/<username>/log_off', methods=["POST"])
def log_user_off(username):
    online_users_file = open("data/game_players.txt")
    online_users = [row for row in online_users_file if len(row.strip()) > 0 and row.strip() != username]
    online_users_file.close()

    with open("data/game_players.txt", "w") as online_users_file:
        for user in online_users:
            online_users_file.write('%s\n' % user)

    return;    
    
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        '''Routing view to render/call contact.html in browser'''
        flash("Thank you {} for your message, we will respond soon.".format(
            request.form["name"]))
            
    return render_template("contact.html")

if __name__== '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            #If debug=True not included, changes will not render in the browser.
            debug=True)
