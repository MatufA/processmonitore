# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 14:58:39 2018

@author: adiel
"""

def print_list(to_print):
    try:
        print_list = to_print 
        filename = to_print[-2]
        mode = bool(to_print[-1])
    except:
        return False
    
    
    if mode:
        with open(filename, "w") as plist:
            for line in print_list[:-2]:
                plist.write(str(line) + "\n")
            

    else:
        with open(filename, "a") as plist:        
            for line in print_list[:-2]:
                plist.write(str(line) + "\n")
                print(line)

    return True