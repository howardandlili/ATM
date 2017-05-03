#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
这里是项目的配置文件
主要是配置数据库信息、
'''
import os,sys,json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#这里配置数据库的信息
database = {
    'engine':'file_storage', #这里是用文件存储的方式
    'tables':'accounts',#这里是表的名字
    'path':'%s/db'%BASE_DIR#这里是路径已经根据上面的相对路径找到了
}
tran_type = {
    'repay':{'action':'plus','interest':0},
    'withdraw':{'action':'minus','interest':0.05},
    'transfer':{'action':'minus','interest':0.05},
    'consume':{'action':'minus','interest':0}
}