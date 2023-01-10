#JUST SOME DEFAULT TESTING THING, CALLED IN etl-flask-dockerfile
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__, template_folder="templates", static_folder='static_files')

@app.route('/')
def base():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home_page.html")

@app.route("/connections")
def connections():
    return "connections"

@app.route("/tags")
def tags():
    return "tags"

@app.route("/metadata")
def metadata():
    return "metadata"

@app.route("/loader")
def loader():
    return "loader"

@app.route("/index")
def index():
    return "index"

@app.route("/about")
def about():
    sites = ['twitter', 'facebook', 'instagram', 'whatsapp']
    return render_template("about.html", sites=sites)

@app.route("/dropdown")
def dropdown():
    colors = ['Red', 'Blue', 'Black', 'Orange']
    return render_template('dropdown.html', colors=colors)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)