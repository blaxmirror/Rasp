#!/usr/bin/env python3

# all the import
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from flask_script import Shell, Manager
from flask_mail import Mail, Message
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from threading import Thread
import os
from flask_pymongo import PyMongo
from getstats import getstats

app = Flask(__name__)
manager = Manager(app)
mongo = PyMongo(app)
moment = Moment(app)
mail = Mail(app)
bootstrap = Bootstrap(app)

def make_shell_context():
    pass

def send_async_email(app, msg):
    pass

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', stats=getstats())

if __name__ == "__main__":
    app.run(host='0.0.0.0')
