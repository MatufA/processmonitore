# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 03:45:58 2018

@author: adiel
Write list of running process 
"""

import psutil
import time

plist = []
def proc_list():
    plist.clear()
    plist.append(time.asctime(time.localtime(time.time())))

    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
        except psutil.NoSuchProcess:
            pass
        else:
            plist.append (str(pinfo['pid']) + '-' \
                + str(pinfo['name']) +'-' +str(pinfo['username']))
    plist.extend(["processList.txt" , True])
    return plist 