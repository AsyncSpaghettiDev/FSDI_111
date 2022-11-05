from flask import Flask, render_template                    # From the flask package import the Flask class

app = Flask(__name__)                                       # Instantiate Flask into app (object)

@app.get('/')                                               # Flask decorator that maps routes to view functions
def index():                                                # A view function in a function mapped to a route (flask)
    me = {                                                  # A python dictionary containing keys and values
        'first_name': 'Jonathan',
        'last_name': 'Mojica',
        'hobbies': ['Programming', 'Reading', 'Soccer'],
        'active': True
    }
    return me                                               # Return statement (required)

@app.get('/about')
def about_me():
    return render_template('index.html')                    # Render a template (html file)