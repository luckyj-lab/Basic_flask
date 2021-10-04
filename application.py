from flask import Flask
application = Flask(__name__)

app = application
@application.route("/")
def hello_world():
    return "Please subscribe to my webpage where ever you are"


if __name__ == "__main__":
    application.run(debug=False)