# -*- coding : UTF-8 -*-
# Author : Banehallow
# Email  : 1140664142@qq.com
from flask import Flask, request, render_template, send_from_directory
app = Flask(__name__, static_url_path='')

#page route
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/register')
def register():
  return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.methods == 'GET':
    return render_template('login.html')
  if request.methods == 'POST':
    pass

if __name__ == '__main__':
  app.debug = True
  app.run()

