from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return '<h2>Hello World!</h2>'

if __name__ == "__main__":
    application.run(debug=True, port=80)