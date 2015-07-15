# -*- coding : UTF-8 -*-
# Author : Banehallow
# Email  : 1140664142@qq.com

from baseService import BaseService
import dao
import g

class AccountService(BaseService):
  def __init__(self):
    BaseService.__init__(self, 'account')