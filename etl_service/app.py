#JUST SOME DEFAULT TESTING THING, CALLED IN etl-flask-dockerfile
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def hello():
    return 'Hello World'

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    return "index"

@app.route("/about")
def about():
    sites = ['twitter', 'facebook', 'instagram', 'whatsapp']
    return render_template("about.html", sites=sites)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)