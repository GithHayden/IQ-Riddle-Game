import os
import json

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'a_secret'

@app.route('/')
def index():
    '''Routing view to render/call index.html in browser'''
    return render_template("index.html", page_heading="Game")
    
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        '''Routing view to render/call contact.html in browser'''
        flash("Thank you {} for your message, we will respond soon.".format(
            request.form["name"]
        ))
    return render_template("contact.html", page_heading="Contact Developer")

if __name__== '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            #If 'debug=True' not included, changes will not render in the browser.
            debug=True)