from flask import Flask, render_template

Apps = Flask(__name__)
@Apps.route('/')

def index():
    return render_template('hello.html')

if __name__ == "__main__":
    Apps.run(debug=True)