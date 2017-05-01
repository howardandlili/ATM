#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
这里其实就是整个python的一个入口，他可以调用core（也就是所有代码的目录）下面的方法。
'''
#首先要把环境变量弄好，让他可以跨目录调用方法
import sys,os
file_path = os.path.abspath(__file__)#这里可以找到当前文件的路径
dir_path = os.path.dirname(file_path)#这里可以找到当前文件架的路径可以看作是向上跳一层
dir_base = os.path.dirname(dir_path) #这里可以找到父目录的路径，可以看见又是向上跳了一层，一般到这里就是根目录了
#已经找了更目录了就把根目录添加到sys的环境变量中去
sys.path.append(dir_base)#到了这里就是已经可以导入父目录的包了。
#开始导入代码包中的主方法
from core import main

#这里主要是为了给别的函数调用，而且不会执行两次用的
if __name__ == '__main__':
    main.run()