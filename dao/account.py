from flask import g
import pymongo
import db

def add(userInfo):
  if g.db['account'].find_one({'name' : userInfo.userName}) != NULL:
    return {'result' : 'fail'}
  else:
    userInfo['courses'] = {}
    g.db.['account'].insert(userInfo)
    return {'result': 'success'}

def query(userName):
  user = g.db['account'].find_one({'name' : userName})
  if user == NULL:
    return {'result' : 'fail'}
  else:
    return {'result' : 'success', 'msg' : user}

def update(userInfo):
  if g.db['account'].find_one({'name' : userInfo.userName}) != NULL:
    return {'result' : 'fail'}
  else:
    g.db.['account'].update({'name' : userInfo.userName}, {'$set' : userInfo})
    return {'result': 'success'}