# -*- coding : UTF-8 -*-
# Author : Banehallow
# Email  : 1140664142@qq.com
from flask import Flask, request, render_template
from flask import jsonify
import util
import g
import pymongo
import controller

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'GET':
    return render_template('register.html')
  if request.method == 'POST':
    data = request.form.to_dict(flat=True)
    ctrl = controller.accountController
    return jsonify(ctrl.register(data))

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('login.html')
  if request.method == 'POST':
    pass

if __name__ == '__main__':
  app.debug = True
  g.client = pymongo.MongoClient('localhost', 27017)
  g.db = g.client['friencher']
  g.err = {
    'arg'  : 'not enough arguments',
    'dbe'  : 'object already in the database',
    'dbne' : 'object is not in the database'
  }
  app.run()
