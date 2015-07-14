from flask import g
import pymongo
import db

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

def query(userName):
  pass

def update(userInfo):
  pass
