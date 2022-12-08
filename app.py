from flask import Flask, render_template, request, url_for
from model import load, model_predict
import sklearn

app = Flask(__name__)

# laod model & scaler
load()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/services_manual")
def services_manual():
    return render_template("services_manual.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/portfolio_app")
def portfolio_app():
    return render_template("portfolio-app.html")

@app.route("/portfolio_data")
def portfolio_data():
    return render_template("portfolio-data.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/predictor')
def predictor():
    return render_template('predictor.html')

@app.route('/predictor_manual')
def predictor_manual():
    return render_template('predictor_manual.html')

@app.route("/predict", methods=["POST"])
def predict():
    duration = int(request.form['duration'])
    pdays = int(request.form['pdays'])
    day = int(request.form['day'])
    poutcome = int(request.form['poutcome'])
    month = int(request.form['month'])
    contact = int(request.form['contact'])
    balance = int(request.form['balance'])/16200
    previous = int(request.form['previous'])

    data = [[duration, pdays, day, poutcome, month, contact, balance, previous]]
    pred_result, pred_score = model_predict(data)

    return render_template('predictor.html', pred_result=pred_result, pred_score=pred_score)

if __name__ == "__main__":
    app.run(debug=True)