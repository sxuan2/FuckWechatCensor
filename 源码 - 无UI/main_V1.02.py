# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 16:31:51 2022

@author: sijian
"""

version_name = "V1.02"
note = """

This version includes:
1. UI redesign, one program, 2 buttons for encode and decode
2. button to clear input
"""


import string
import random
import base64


# testmsg = "Fuck CCP&Wechat censorship"

msg = input("input your msg:")
choice = input("input your choice(0:encode,1:decode)")

def GetString(n=32):
    """
    make a string with length n
    can be used with encoding process
    """
    a = ''.join(random.sample(string.ascii_letters + string.digits, n))
    b = ''.join(random.sample(string.ascii_letters + string.digits, n))
    return a,b

def Encode(input_text):
    """
    encoded result = a + base64 code + b
    """
    a,b = GetString(32)
    b64_name = base64.b64encode(input_text.encode())
    b64_name_str = str(b64_name).split('\'')[1]
    result = a + b64_name_str + b
    print(result)
    return result


def Decode(input_code):
    b64_name_str = input_code[32:-32]
    # print(b64_name_str)
    print(base64.b64decode(b64_name_str).decode())
    

# process

if str(choice) == '0':
    Encode(input_text=msg)
elif str(choice) == '1':
    Decode(input_code=msg)
else:
    print('wrong value, please try again')









