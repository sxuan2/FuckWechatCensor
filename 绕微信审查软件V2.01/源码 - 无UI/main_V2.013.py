# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 16:31:51 2022

@author: sijian
"""

version_name = "V2.01"
note = """

This version includes:
1. UI redesign, one program, 2 buttons for encode and decode
2. button to clear input
"""

import string
import random
import base64

import tkinter as tk
from tkinter import ttk
from tkinter import *

msg = input("input your msg:")

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
    a,b = GetString()
    b64_name = base64.b64encode(input_text.encode())
    b64_name_str = str(b64_name).split('\'')[1]
    result = a + b64_name_str[::-1] + b
    print('base64:{}'.format(b64_name))
    print(result)
    

def Decode(input_code):
    b64_name_str = input_code[32:-32][::-1]
    print('base64:{}'.format(b64_name_str))
    result = base64.b64decode(b64_name_str).decode()
    
    print(result)
    
# process

i=0
while True:
    choice = input("input your choice(0:encode,1:decode)")

    if str(choice) == '0':
        Encode(input_text=msg)
        break
    elif str(choice) == '1':
        Decode(input_code=msg)
        break
    else:
        i+=1
        print('wrong value, please try again')
        if i >=4:
            print('too many wrong entries, quitting....')
            break

