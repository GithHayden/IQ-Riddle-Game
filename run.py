import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    '''Routing to render html template'''
    return render_template("index.html")
    
if __name__== '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            #If 'debug=True' not included, changes will not render in the browser.
            debug=True)