#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'

successful_trade = False

import os,sys,json
from core import db_handler


def load_current_balance(account):
    #这个是读取最新的余额,并且返回用户信息
    sql = "select * from accounts where account=%s" % account
    action = 'read'
    data = db_handler.db_handler(sql=sql, account=account, action=action)
    return data


def upda_current_balance(*args,**kwargs):
    #这里定义更新用户信息的操作
#    print('acc>>>>args',args)
    new_balance = args[1]
    account_id = args[0]['account_id']
    args[0]['account_data']['balance'] = new_balance #这个是更新用户余额
    data = args[0]['account_data']
    action = 'write'
    #已经完成了内存上面的修改就要开始写盘了
    #到了这里我们就把参数丢给数据库模块做吧
    if db_handler.db_handler(data=data,account=account_id,action=action):
        return True
