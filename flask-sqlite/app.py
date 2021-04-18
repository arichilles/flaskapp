import sqlite3, os
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

conn = cursor = None
  
# cara I mengatasi qlite3.OperationalError: no such table    
# def openDB():
#     global conn, cursor
#     BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#     db_path = os.path.join(BASE_DIR, 'database.db')
#     with sqlite3.connect(db_path) as conn:
#         cursor = conn.cursor()
    
# cara II mengatasi qlite3.OperationalError: no such table 
def openDB():
    global conn, cursor
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

# # cara tanpa subfolder
# def openDB():
#     global conn, cursor
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
    
def colseDB():
    global conn, cursor
    cursor.close()
    conn.close()
    
@app.route('/')
def index():
    openDB()
    container = []
    for kode,judul,penulis in cursor.execute("SELECT * FROM buku"):
        container.append((kode,judul,penulis))
    colseDB()
    return render_template('index.html', container=container)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        kode = request.form['kode']
        judul = request.form['judul']
        penulis = request.form['penulis']
        data = kode,judul,penulis
        openDB()
        cursor.execute('INSERT INTO buku VALUES(?,?,?)', data)
        conn.commit()
        colseDB()
        return redirect(url_for('index'))
    else:
        return render_template('add_form.html')
    
@app.route('/edit/<kode>', methods=['GET','POST'])
def edit(kode):
    openDB()
    result = cursor.execute('SELECT * FROM buku WHERE kode=?', (kode,))
    data = cursor.fetchone()
    if request.method == 'POST':
        kode = request.form['kode']
        judul = request.form['judul']
        penulis = request.form['penulis']
        cursor.execute('''
                       UPDATE buku SET judul=?, penulis=? WHERE kode=?
                       ''', (judul,penulis,kode))
        conn.commit()
        colseDB()
        return redirect(url_for('index'))
    else:
        colseDB()
        return render_template('edit.html', data=data)
    
@app.route('/delete/<kode>', methods=['GET','POST'])
def delete(kode):
    openDB()
    cursor.execute('DELETE FROM buku WHERE kode=?', (kode,))
    conn.commit()
    colseDB()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)