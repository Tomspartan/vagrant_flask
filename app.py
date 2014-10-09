from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask is working within Vagrant. Continue"

if __name__ == "__main__":
    app.debug = True
    app.run()