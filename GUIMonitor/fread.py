# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 15:28:58 2018

@author: adiel
"""
import os
def read_list(filepath):
    proc_list = []
    if not os.path.isfile(filepath):
       print("The file has been removed./n\
             Someone delet your file, insure it's not maliciuos")
       return proc_list
    with open (filepath , "rb") as read:
        proc_list = read.readlines()
    return proc_list