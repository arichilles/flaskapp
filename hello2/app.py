from flask import Flask
from models import HelloModel

application = Flask(__name__)
@application.route('/')
def index():
    # membuat onjek dari kelas HelloModel
    model = HelloModel()
    # mengembalikan nilai yang diambil dari model
    return model.getText()

if __name__ == "__main__":
    application.run(debug=True)