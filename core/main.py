#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
这里就是主代码
功能分别是前台的显示，还款，取款，转账，登出，查账，和客人的交互
其中一些功能还是要调用他的文件的方式来实现
这样比较好维护
=====================================================================================================
首先要进行操作就需要登陆，但是登陆验证的方式有很多种，现在就不写在main中免得太乱，main只需要一个被认证后的状态。
那么首先就是先需要一个被初始化的用户状态，例如ID,余额，是否已经认证，这里就写成一个字典，比较好维护
由于这个字典是一个临时的内存暂时使用所以不需要写盘，当用户信息的字典已经做好了~那么我们需要有别的方法来传递信息过来修改
这个字典使它变成当前用户的信息。首先整改修改操作都必须是已认证的，我们开始做认证模块。
'''
from core import auth #导入认证模块
from core.auth import login_required #导入装饰器来验证是否登陆
from core import transaction
from core import accounts

user_data = {
    'account_id':None, #用户ID暂时为空的
    'is_authenticated':False,#是否被认证初始的时候的否的~等到登陆认证传来认证成功才会被修改为True。
    'account_data':None#用户的详细信息，例如用户的账号、密码、限额、余额、开户时间、过期时间、还款日期、还有就是账户的状态，
                       #账户的状态分为，可用，锁定，不可用
}
# 做一个退出标记方便循环的跳出和判断
#定义用户信息
def user_info(user_data):
    print('''
    --------%s的信息是--------
    您的余额为：%s
    您的额度为：%s
    您的还款日期为：每月%s号
    '''%(user_data['account_id'],\
         user_data['account_data']['balance'],\
         user_data['account_data']['credit'],\
         (user_data['account_data']['pay_day'])))
    exit_flag = 0
    return exit_flag


#定义还款
@login_required #这里放一个装饰器是用来验证这次操作是不是已经登陆的
def repay(user_data):
    print('开始还钱了')
    acc_data = user_data['account_data']
    print('''
    --------您的余额信息--------
    额度为：%s
    余额为：%s
    '''%(acc_data['credit'],acc_data['balance']))
    back_flag = False
    old_balance = acc_data['balance'] # 现在的余额
    while not  back_flag:
        repay_amount = input('输入您要还的金额或者按b返回上一层，金额数必须\033[31m大于0\33[1m:')
        if len(repay_amount) >0 and repay_amount.isdigit():#这里是判断是否有输入金额~因为input是字符串来的不能直接比较
            amount = int(repay_amount)
            tran_type = 'repay'
            '''这里最好交给另外一个方法来做~
            因为很多需求是要用到计算的#而且需要写盘并且刷新用户信息，
            那么就需要另外一个方法了
            '''
            new_balance = transaction.make_transaction(acc_data=acc_data,\
                                                       amount=amount,\
                                                       tran_type=tran_type)
            #交易已经做完了那么就该把修改的用户信息存到数据库中去了，
            #现在把要和数据库交互的操作丢给专门的accounts模块去做
#            acc_data['balance'] = new_balance #更新用户信息
            if accounts.upda_current_balance(user_data,new_balance):
                print('您现在的余额是：', new_balance)
            else:
                print('交易失败')
        elif repay_amount == 'b':
            print('返回上一层')
            back_flag = True
            continue
        else:
            print('这个不是一个数字请输入正确的数字')


    exit_flag = 0
    return exit_flag
#定义取款
def withdraw(user_data):
    pass
#定义转账
def transfer(user_data):
    pass
#定义登出
def logout(user_data):
    print('\t\033[32m退出系统,希望您下次再来\033[0m')
    exit_flag = 1
    return exit_flag


#定义查账
def pay_check(user_data):
    pass
#定义交互也就是前台显示
def interactive(user_data):
    #这里主要的菜单目录
    menu = '''
    ------欢迎来到黄家银行------
    \033[33m1.账户信息
    2.还款
    3.取款
    4.转账（还没有做）
    5.账单（还没有做）
    6.退出
    \033[1m
    '''
    #做一个单独对应的字典这样就可以根据key来调用相应的方法了
    menu_dict = {
        '1':user_info,
        '2':repay,
        '3':withdraw,
        '4':transfer,
        '5':pay_check,
        '6':logout
    }
    exit_flag = 0
    while exit_flag == 0:
        print(menu)
        user_option = input('请输入您的需要：').strip() #要求用户输入选择
        '这里如果一个个的去判断的话太长了那么我们就需要一个可以一一对应的字典了'
        if user_option in menu_dict: #判断用户的选择是不是在字典key中
        #这样就可以根据key来调用相应的方法了,同时有了返回退出标记所以可以判断是不是退出循环
            exit_flag = menu_dict[user_option](user_data) #这样一句就可以完成了判断了并且开始了执行

        else:
            print('\033[31m您的输入不在菜单中！！\033[0m')









'''
这里定义了客人打开首页的时候看见的登录界面,这里是需要客人输入账号密码或者是其他的认证方式（这个需要不一定需要在这个函数
上面做完可以把输入交给别的函数来做）。我们要做的是要把客户输入的信息传出去
只有这里是通过的时候才有后续的一系列的操作。很简单~都不能登录谁让你转钱啊
'''
def run():
    acc_data = auth.acc_login(user_data) #这样我们就可以把用户字典传给了登陆方法了，并且接收认证模块返回的结果
    if user_data['is_authenticated']:   #接收到返回结果的时候用户的临时信息已经修改好了，这里判断是不是已经被认证
        user_data['account_data'] = acc_data #这里是把用户信息做一个完整的信息,这样我们就可以开始交互了
        interactive(user_data)
