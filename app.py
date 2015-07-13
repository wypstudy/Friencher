# -*- coding : UTF-8 -*-
# Author : Banehallow
# Email  : 1140664142@qq.com
from flask import Flask, request, render_template
from flask import jsonify
import dao

app = Flask(__name__)

@app.before_request
def before_request():
  dao.db.connect()

@app.teardown_request
def teardown_request(exc):
  dao.db.close()

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'GET':
    return render_template('register.html')
  if request.method == 'POST':
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('login.html')
  if request.method == 'POST':
    pass

if __name__ == '__main__':
  app.debug = True
  app.run()

