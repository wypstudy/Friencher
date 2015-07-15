# -*- coding : UTF-8 -*-
# Author : Banehallow
# Email  : 1140664142@qq.com

import dao
import g

class BaseService:
  __table = ''

  def __init__(self, table):
    self.table = table

  def add(self, condition, fields):
    info = dao.op.query(self.table, condition)
    if info.has_key('msg'):
      print g.err
      re = {}
      re['msg'] = g.err['dbe']
      re['result'] = 'fail'
      return re
    dao.op.insert(self.table, fields)
    re = {}
    re['result'] = 'success'
    return re

  def query(self, condition):
    re = dao.op.query(self.table, condition)
    if info.has_key('msg'):
      re['result'] = 'success'
    else:
      re['result'] = 'fail'
      re['msg'] = g.err['dbne'] 
    return re

  def list(self, condition):
    pass

  def update(self, condition, fields):
    pass

  def remove(self, condition):
    pass

