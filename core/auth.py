#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'

import os,sys,json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
#from core import main
from core import accounts

'''
认证模块：
这里主要是把客人在首页登陆的时候根据输入的账号，密码或者其他方式来认证是否能够登陆
这里主要是除了完成认证过程，还要把已通过认证的信息传出去
那么来到这里的时候我们发现我们需要用户的信息来验证账号密码，那么需要谁来给我呢？
用户字典，我们只需要把用户输入的信息和用户字典来做对比就可以了。
用户字典在数据库里面，那么我们就需要一个可以和数据库交互的方法了（这里是另外做一个模块）
'''
from core import db_handler


def login_required(func):
    def wrapper(*args,**kwargs):
        print('--wrapper--->',args[0]['is_authenticated'])
        if args[0]['is_authenticated']:
            return func(*args,**kwargs) #这里如果被装饰的的func是要求有返回的话这个一个要return一次要不就会变成过程而没有返回值
        print("您还没有登陆,请重新登陆谢谢")
#        main.run()
    return wrapper


#定义传过来的信息能不能被认证，在这里就需要用户字典了，认证成功就返回用户的认证信息


def acc_auth(account,password):
    #我们为了把适用大多数的数据库需要比这里标准化，
    #在这里我们需要根据用户输入的账号找到对应的认证方式看看是不是可以被匹配。
    #在这里我们就要等待数据库操作方法的返回结果
    # sql = "select * from accounts where account=%s" % account
    # action = 'read'
    # data = db_handler.db_handler(sql = sql,account=account,action=action)
    #这里做了一些优化把用户和数据库交互的丢给用户模块
    data = accounts.load_current_balance(account)
    if data['password'] == password:
        return data #到了这里的时候认证已经成功了，那么我们就需要去改变user_data了
    else:
        print('您的账号或者密码不对请重新输入')


#定义用户的登录，主要是用来传输输入的信息和接受认证成功的用户信息然后再把已经通过认证返回就可以了
def acc_login(user_data):
    account = input('输入您的账号：')
    password = input('输入您的密码：')
    auth = acc_auth(account,password) #把用户的输入的信息传给认证模块
    if auth:#这里表示auth有正确的返回值为True，简单来说就是已经通过认证了
        user_data['is_authenticated'] = True #修改临时的用户信息，这里代表已经通过认证
        user_data['account_id'] = account #这里代表把原来为空的用户ID改成现在的用户ID
#        print('欢迎用户%s登陆ATM系统'%account)
        return auth




