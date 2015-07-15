# -*- coding : UTF-8 -*-
# Author : Banehallow
# Email  : 1140664142@qq.com
import g

def insert(table, fields):
  g.db[table].insert(fields)

def remove(table, condition):
  g.db[table].remove(condition)

def query(table, condition):
  info = g.db[table].find_one(condition)
  if info == None:
    return {}
  else:
    info['_id'] = str(info['_id'])
    return {'msg' : info}

def update(table, condition, fields):
  g.db[table].update(condition, {'$set' : fields})