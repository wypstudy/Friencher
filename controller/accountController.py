# -*- coding : UTF-8 -*-
# Author : Banehallow
# Email  : 1140664142@qq.com
import g
import service

def register(args):
  if args.has_key('username') and args.has_key('password'):
    condition = {
      'username' : args['username']
    }
    fields = args

    ser = service.accountService.AccountService()
    return ser.add(condition, fields)
  else:
    return {'result' : 'fail', 'msg' : g.err['arg']}

def login(args):
  if args.has_key('username') and args.has_key('password'):
    condition = {
      'username' : args['username'],
      'password' : args['password'],
    }
    ser = service.accountService.AccountService()
    re = ser.query(condition)
    if re['result'] == 'success':
      del re['msg']['password']
    return re
