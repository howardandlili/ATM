#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'

import os,sys,json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import setting


'''
这里主要是做和数据库交互的的操作
'''

#定义文件类型的数据库的操作并且返回用户的data
def file_db_handle(**kwargs):
    account = kwargs['account']
    file_path = '%s/%s'%(kwargs['conn_params']['path'],\
                         kwargs['conn_params']['tables'])
    account_file = '%s/%s.json'%(file_path,account)
    with open(account_file,'r') as f:
        account_data = json.load(f)
        return account_data #到了这里我们就可以已经可以找到客户的所有资料了
                            #然后我们就可以回去认证模块那里继续操作了




def mysql_db_handle(conn_params):
    pass


def db_handler(**kwargs):
    '定义数据库的操作，这里需要根据传过来的信息把信息分类成根据不同的数据库可以认识的语句'
    conn_params = setting.database #在这里就需要配置文件中定义了什么的数据库信息
    account = kwargs['account']
    sql = kwargs['sql']
    if conn_params['engine'] == 'file_storage' : #判断为文件类型的数据库
        return file_db_handle(account=account,conn_params=conn_params)
    elif conn_params['engine'] == 'mysql':
        return mysql_db_handle(account,conn_params)





