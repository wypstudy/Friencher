from flask import g
import pymongo

def connect():
<<<<<<< HEAD
  g.connect = pymongo.Connection('localhost', 27017)
  g.db = g.connect['friencher']

def close():
  g.db.close()
=======
  conn = MongoClient('localhost', 5000)
  database = conn.test
  return database

def close():
  pass
>>>>>>> master
