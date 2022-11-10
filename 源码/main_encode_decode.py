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

import tkinter as tk
from tkinter import ttk
from tkinter import *


def GetString(n=32):
    """
    make a string with length n
    can be used with encoding process
    """
    a = ''.join(random.sample(string.ascii_letters + string.digits, n))
    b = ''.join(random.sample(string.ascii_letters + string.digits, n))
    return a,b

def Encode():
    """
    encoded result = a + base64 code + b
    """
    a,b = GetString(32)
    input_text = Main_input_text.get("1.0",END)
    b64_name = base64.b64encode(input_text.encode())
    b64_name_str = str(b64_name).split('\'')[1]
    result = a + b64_name_str + b
    print(result)
    

def Decode():
    input_code = Main_input_text.get("1.0",END)
    b64_name_str = input_code[32:-33]
    # print(b64_name_str)
    print(base64.b64decode(b64_name_str).decode())
    
    
def clearTextInput():
    Main_input_text.delete("1.0", END)
    
"""
UI code are as below
"""


root = tk.Tk()

# font
ft = ('Times', 20, 'italic')
ft1 = ('Times', 18, 'bold')
# root.title('Fuck CCP&Wechat censorship')
root.title('学术论文查找')

# this is the text input 
Main_input_text = tk.Text(root, height=3, width=40)
# this label will appear as instruction
input_instruction = Label(root, text="Input MSG here:", font = ft)

# the buttons
recode_button = Button(root, text="ENCODE", font = ft1,command=lambda : Encode())
decode_button = Button(root, text="DECODE", font = ft1,command=lambda : Decode())
clear_button = Button(root, text="CLEAR", font = ft1, command=lambda : clearTextInput())


"""
UI elements layout
"""
input_instruction.grid(row=0, column=0)
Main_input_text.grid(row=0, column=1)
recode_button.grid(row=1, column=0)
decode_button.grid(row=2, column=0)
clear_button.grid(row=3, column=0)
tk.mainloop()
























