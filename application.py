from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello_world():
    return "Please subscribe to my webpage"


if __name__ == "__main__":
    application.run(debug=True)