from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

access_key = "2e0bceb90f226f7e6e4a4534e549f722"
endpoint = 'convert'

@app.route('/')
def show_home_page():
    return render_template("base.html")




