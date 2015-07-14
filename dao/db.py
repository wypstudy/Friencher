from flask import g
import pymongo

def connect():
  g.connect = pymongo.Connection('localhost', 27017)
  g.db = g.connect['friencher']

def close():
  g.db.close()
