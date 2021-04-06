from flask import *
from models import *

app = Flask(__name__)
@app.route('/')

def index():
    model = HelloModel()
    
    return render_template('hello.html', model=model)

if __name__ == "__main__":
    app.run(debug=True)