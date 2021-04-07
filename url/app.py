from flask import *

application = Flask(__name__)
@application.route('/')
def index():
    return render_template('home.html')

@application.route('/product')
def product():
    return render_template('/product.html')

@application.route('/contact')
def contact():
    return render_template('/contact.html')

if __name__ == "__main__":
    application.run(debug=True)