from flask import g
import pymongo
import db

<<<<<<< HEAD
def add(userInfo):
  if g.db['account'].find_one({'name' : userInfo.userName}) != NULL:
    return {'result' : 'fail'}
  else:
    g.db.['account'].insert(userInfo)
    return {'result': 'success'}
=======
def add(database):
    posts = database.posts
    post = {"username":"", 
            "sid":"",
            "password":25,
            "email":"",
            "grad":"",
            "school":"",
            "major":""
    }
    post_id = posts.insert(post)
    print post_id
  pass
>>>>>>> master

def query(userName):
  user = g.db['account'].find_one({'name' : userName})
  if user == NULL:
    return {'result' : 'fail'}
  else:
    return {'result' : 'success', 'msg' : user}

def update(userInfo):
<<<<<<< HEAD
  pass
=======
<<<<<<< HEAD
  if g.db['account'].find_one({'name' : userInfo.userName}) != NULL:
    return {'result' : 'fail'}
  else:
    g.db.['account'].update({'name' : userInfo.userName}, {'$set' : userInfo})
    return {'result': 'success'}
=======
  pass
>>>>>>> master
>>>>>>> tianzh
