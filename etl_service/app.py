#JUST SOME DEFAULT TESTING THING, CALLED IN etl-flask-dockerfile
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)