from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! Welcome to Devops!"

# run the app.
if __name__ == "__main__":
    application.run()
