import os
from flask import Flask, render_template, request
from flask_uploads import IMAGES, UploadSet, configure_uploads

app = Flask(__name__)
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'upload-photo/static/img'
app.config['SECRET_KEY'] = os.urandom(24)
configure_uploads(app, photos)

@app.route('/', methods=['GET','POST'])

def index():
    if request.method == 'POST' and 'photo' in request.files:
        try:
            photos.save(request.files['photo'])
            return render_template('sukses.html')
        except:
            return render_template('upload.html')
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)