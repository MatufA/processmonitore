# -*- coding: utf-8 -*-
"""
Created on Sat May  5 16:03:41 2018

@author: adiel
"""
import compare as co
import sys
import database as db

def manual_UI(start, end):
   try:
        clist_start =[]
        clist_stop =[]
        date_start = start
        date_end = end

        comp = db.is_empty
        if comp:
            clist_start = db.load_data_by_date(date_start)
            clist_stop = db.load_data_by_date(date_end)
            clist_start, clist_stop = co.compare_process(clist_start, clist_stop)
            
   except KeyboardInterrupt:
        print("Software is shuting down by the user...")
        sys.exit(0)
   return clist_start, clist_stop
    
def shut_down():
    print("Software is shuting down...")
    with open("Status_Log.txt", "a") as plist:        
        plist.write("Software is DOWN!!...")
    sys.exit(1)