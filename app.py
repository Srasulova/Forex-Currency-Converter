from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

access_key = "b1a53257e5596240e73d3b7f"
base_url = 'https://v6.exchangerate-api.com/v6/b1a53257e5596240e73d3b7f/pair/'


@app.route("/")
def show_home_page():
    return render_template("base.html")

@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        from_currency = request.form['from']
        to_currency = request.form['to']
        amount = float(request.form['amount'])  # Convert amount to float

        # Make API call to get currency conversion
        response = requests.get(f"{base_url}{from_currency}/{to_currency}/{amount}")
        if response.status_code == 200:
            data = response.json()
            if data['result'] == 'success':
                conversion_rate = data['conversion_rate']
                conversion_result = data['conversion_result']
                return render_template("base.html", from_currency=from_currency, to_currency=to_currency,amount=amount, conversion_rate=conversion_rate, conversion_result=conversion_result)
            else:
                error_message = "Currency conversion failed. Please try again later."
                return render_template("base.html", error_message=error_message)
        else:
            error_message = f"Error {response.status_code}: Currency conversion request failed."
            return render_template("base.html", error_message=error_message)
    else:
        return render_template("base.html")




