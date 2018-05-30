import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    '''Routing to render index.html in browser'''
    return render_template("index.html")


@app.route('/contact')
def contact():
    '''Routing to render contact.html in browser'''
    return render_template("contact.html")


if __name__== '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            #If 'debug=True' not included, changes will not render in the browser.
            debug=True)