from flask import Flask

app = Flask(__name__)
@app.route('/hello/<name>')
def hello(name):
    return '<h2>Hello %s</h2>' % name

# mendefinisikan paramater bertipe integer
@app.route('/nomor/<int:no>')
def nomor(no):
    return '<h2>Ini merupakan urutan ke-%d</h2>' % no

if __name__ == "__main__":
    app.run(debug=True)