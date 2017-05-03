#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from conf import setting
'''
这是一个交易的模块
主要是计算还款、取款、转款的交易
'''
def make_transaction(**kwargs):
    amount = kwargs['amount']
    tran_type = kwargs.get('tran_type')
    old_balance = (kwargs.get('acc_data')).get('balance')
    interest = setting.tran_type[tran_type]['interest']
    amount = amount*(1+interest)
    interest = amount*interest
    print('变动金额为：',amount,'利息为：',interest)
    #由于交易类型都加或者减，不过还是需要计算利息那么这个就是conf那里配置好就可以了
    if tran_type in setting.tran_type:
        action = setting.tran_type[tran_type]['action']
        if action == 'plus':
            new_balance = old_balance + amount
        else:
            new_balance = old_balance - amount
        return new_balance