#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
这里就是主代码
功能分别是前台的显示，还款，取款，转账，登出，查账，和客人的交互
其中一些功能还是要调用他的文件的方式来实现
这样比较好维护
'''
#首先要进行操作就需要登陆，但是登陆验证的方式有很多种，现在就不写在main中免得太乱，main只需要一个被认证后的状态。
#那么首先就是先需要一个被初始化的用户状态，例如ID,余额，是否已经认证，这里就写成一个字典，比较好维护
user_data = {
    'account_id':None, #用户ID暂时为空的
    'is_authenticated':False,#是否被认证初始的时候的否的~等到登陆认证传来认证成功才会被修改为True。
    'account_data':None#用户的详细信息，例如用户的账号、密码、限额、余额、开户时间、过期时间、还款日期、还有就是账户的状态，
                       #账户的状态分为，可用，锁定，不可用
}

#定义还款
def repay():
    pass
#定义取款
def withdraw():
    pass
#定义转账
def transfer():
    pass
#定义登出
def logout():
    pass
#定义查账
def pay_check():
    pass
#定义交互也就是前台显示
def interactive():




def run():
    print('in the core.main')
