#!/usr/bin/env python3

from flask import Flask, request, redirect
import pymongo
from io import StringIO
import bson.binary

app = Flask(__name__)
db = pymongo.MongoClient('localhost', 27017).test

app.debug = True

def save_file(f):
    content = StringIO(f.read())
    db.files.save(dict(content=bson.binary.Binary(content.getvalue())))

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['uploaded_file']
    save_file(f)
    return redirect('/')

@app.route('/')
def index():
    return '''
    <!doctype html>
    <html>
    <body>
    <form action='/upload' method='post' enctype='multipart/form-data'>
        <input type='file' name='uploaded_file'>
        <input type='submit' value='Upload'>
    </form>
    '''

if __name__ == '__main__':
    app.run()