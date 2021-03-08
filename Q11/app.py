
import os
from flask import Flask, flash, render_template, url_for, request, redirect
from werkzeug.utils import secure_filename

import mysql.connector
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


def opendb():
    global mydb, cursor
    mydb = mysql.connector.connect(
        user='root',
        password='',
        database='upload',
        host='127.0.0.1'
    )
    cursor = mydb.cursor()


def closedb():
    global mydb, cursor
    cursor.close()
    mydb.close()


@app.route('/')
def hello():
    opendb()
    cursor.execute('SELECT * FROM img')
    result = []
    for id, name in cursor.fetchall():
        result.append((id, name))
    closedb()
    return render_template('index.html', result=result)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    upload_file = request.files.getlist("file[]")

    filename = []
    for x in upload_file:
        filename = secure_filename(x.filename)
        x.save(os.path.join(app.config['UPLOAD_FOLDER'],  filename))
        name = (filename)
        opendb()
        cursor.execute(
            '''insert into img(name) values('%s')''' % name
        )
        mydb.commit()
        closedb()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
