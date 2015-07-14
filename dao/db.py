from flask import g
import pymongo

def connect():
  conn = MongoClient('localhost', 5000)
  database = conn.test
  return database

def close():
  pass
