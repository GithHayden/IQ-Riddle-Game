import os
import json

from flask import Flask, render_template, request, flash, redirect, jsonify

app = Flask(__name__)
app.secret_key = 'a_secret'

data = []

def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.writelines(data)

def add_users(username):
    write_to_file("data/players.txt","({0})-{1}\n".format(username.title()))
    
@app.route('/', methods=["GET", "POST"])
def index():
    '''Routing view to render/call index.html in browser'''
    # POST request
    if request.method == "POST":
        write_to_file("data/players.txt", request.form["username"] + "\n")
    return render_template("index.html", page_heading="Play Game")
    
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        '''Routing view to render/call contact.html in browser'''
        flash("Thank you {} for your message, we will respond soon.".format(
            request.form["name"]
        ))
    return render_template("contact.html")

if __name__== '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            #If debug=True not included, changes will not render in the browser.
            debug=True)
