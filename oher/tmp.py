#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
import os,sys,json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
from core import auth

user_data = {
    'account_id':None, #用户ID暂时为空的
    'is_authenticated':False,#是否被认证初始的时候的否的~等到登陆认证传来认证成功才会被修改为True。
    'account_data':None#用户的详细信息，例如用户的账号、密码、限额、余额、开户时间、过期时间、还款日期、还有就是账户的状态，
                       #账户的状态分为，可用，锁定，不可用
}
acc_data = auth.acc_login(user_data)#获得用户信息
balance = acc_data['balance']
