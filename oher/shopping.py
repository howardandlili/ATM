#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'

import os,sys,json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
from core import auth
from core import transaction
from core import accounts
user_data= {}


'''
购物车模块
'''
product_list = [        #商品列表做成列表可以动态
    ('Iphone', 5000),
    ('Ipad', 2000),
    ('Bike', 500),
    ('Watch', 10000),
    ('Coffee', 31),
    ('MImu', 2400)
]

shop_data = {
    'total':0,
    'shoplist':[]
}


shoplist = []
def shoping(shop_data):
    exit_flag = False
    total = 0
    while not exit_flag:
        for k,v in enumerate(product_list,1) or not exit_flag:
            print(k,v)
        number = input('请输入您的选择：')
        if len(number) and number.isdigit():
            if int(number) <= len(product_list) and int(number) > 0:
                goods = product_list[(int(number) - 1)]
                price = goods[1]
                name = goods[0]
                shoplist.append(goods)
                total = total+price
                shop_data['total'] = total
                shop_data['shoplist'] = shoplist

            else:
                print('您输入的数值不在菜单内')
        elif number == 'b':
            exit_flag = True
    return (shop_data)

def checkout(shop_data):
    print('结账咯')
    #做到这里的时候就是和认证模块做交互
    acc_data = auth.acc_login(user_data)
    balance = acc_data['balance']
    total = float(shop_data['total'])
    if total > balance :
        print('太贵了您买不起')
    else:

        tran_type = 'consume'
        #做到这里的就可以和数据库交互了
        new_balance = transaction.make_transaction(acc_data=acc_data, \
                                                   amount=total, \
                                                   tran_type=tran_type)

        account = user_data['account_id']
        data = accounts.load_current_balance(account)
        if accounts.upda_current_balance(data, new_balance):
            print('''您的余额是：%s
        您消费了：%s'''%(new_balance,total))
        else:
            print('\033[31m交易失败\033[0m')


def run(shop_data):
    exit_flag = False
    while not exit_flag:
        print('''
        1:购物
        2:确认购物车
        3:结账 
        ''')
        choice = input('您的选择是：')
        if len(choice)>0 and choice.isdigit():
            choice = int(choice)
            if choice == 1:
                shop_data = shoping(shop_data)
            elif choice == 2:
                total = shop_data['total']
                shoplist = shop_data['shoplist']
                for k, v in enumerate(shoplist, 1):
                    print(k, v)
                print('总价钱为：',total)
            elif choice == 3:
                if shop_data['total'] == 0:
                    print('您还没有买东西')

                else:
                    checkout(shop_data)
        elif choice == 'b':
            exit_flag = True







if __name__ == '__main__':
    run(shop_data)