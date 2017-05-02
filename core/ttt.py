#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'

def user_info():
    print('in the user_info')


menu_dict = {
    '1': user_info,
    # '2': repay,
    # '3': withdraw,
    # '4': transfer,
    # '5': pay_check,
    # '6': logout
}



nb = input('>>')
if nb in menu_dict:
    menu_dict[nb]()