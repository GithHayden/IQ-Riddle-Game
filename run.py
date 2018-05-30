import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    '''Routing view to render/call index.html in browser'''
    return render_template("index.html", page_heading="Game")

@app.route('/contact')
def contact():
    '''Routing view to render/call contact.html in browser'''
    return render_template("contact.html", page_heading="Contact Developer")

if __name__== '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            #If 'debug=True' not included, changes will not render in the browser.
            debug=True)
            
