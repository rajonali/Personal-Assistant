#TODO: run this file and check network dev tools and see the errors. Something wrong with the rss feed parser in index.html



import argparse, sys, string
import os, re, time, signal, copy, pickle
from flask import Flask, request, render_template, redirect, url_for, request
from time import localtime, strftime
import sqlite3
from functools import wraps

import flask.ext.login as flask_login
from flask.ext.login import LoginManager, UserMixin


import os.path
from flask.ext.autoindex import AutoIndex


import urllib
import json

sys.path.append("C:/Users/ta044/Documents/Tasnim Projects/PersonalAssistant")

from common.formatting import colors
from common.sql import conn_db, execute_query

app = Flask(__name__)
login_manager = LoginManager()




#app = Flask(__name__)
app.secret_key = 'key'

login_manager.init_app(app)

users = {'admin':{'pw':'password'}, 'test':{'pw':'password'}}



ROUTINE  = [
'my schedule goes here'
]


def getWords():
  file_locate = "C:/Users/ta044/Documents/Tasnim Projects/PersonalAssistant/static/vocab.txt"
  text = open(file_locate, 'r').read()
  words = text.split("\n")
  return words

def getTemp():
  weather_url = "http://api.openweathermap.org/data/2.5/forecast?id=IDGOESHERE&APPID=APIKEYGOESHERE"
  r = urllib.request.urlopen(weather_url)
  data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
  num = data['list'][0]['main']['temp']
  ftemp =  9/5 * (float(num) - 273) + 32
  ftemp = str(round(float(ftemp)))
  return ftemp

temp = getTemp()




class User(UserMixin):
  pass


@login_manager.user_loader
def user_loader(username):
  if username not in users:
    return

  user = User()
  user.id = username
  return user

@login_manager.request_loader
def request_loader(request):
  username = request.form.get('username')
  if username not in users:
    return

  user = User()
  user.id = username

  user.is_authenticated = request.form['pw'] == users[username]['pw']

  return user




@app.route('/')
@flask_login.login_required
def home():
    return render_template("index.html", reference=ROUTINE, words = getWords())


idx = AutoIndex(app, './static/media', add_url_rules=False)

@app.route('/reports')
@app.route('/reports/<path:path>')
def autoindex(path='.'):
    return idx.render_autoindex(path)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if request.form.get('password') == users[username]['pw']:
            user = User()
            user.id = username
            flask_login.login_user(user) 
            return redirect(url_for('home'))
    return render_template('login.html')





@app.route('/news')
@flask_login.login_required
def news():
    return render_template("news.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error = e), 404

@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html', error = e), 403



if __name__ == "__main__":
	app.run(host='0.0.0.0', port=69)