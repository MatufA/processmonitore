# -*- coding: utf-8 -*-
"""
Created on Sat May  5 19:22:02 2018

@author: adiel
"""

# -*- coding: utf-8 -*-
#!/usr/bin/env python
#!/bin/bash
"""
Created on Sat Apr  7 04:12:40 2018

@author: adiel
"""
import proc as pr
import compare as co
import fprint as fp
import sys, time
import database as db

def monitoring_UI(sec):
   try:
        db.create_database();
        comp = False
        clist_start =[]
        clist_stop =[]
        prev_date = 0
        while True:
            proclist,date = pr.proc_list()
            
            if comp:
                #Compare amd analyze
                prev_list = db.load_data_by_date(prev_date)
                clist_start, clist_stop = co.compare_process(proclist, prev_list)
                
                #Print Status Log
                if clist_start: fp.print_list(clist_start)
                if clist_stop: fp.print_list(clist_stop)

                if not clist_start: comp = False
                
            else: 
                comp = True
            #Print All Running Process
            db.insert_data(proclist)
            prev_date =date
            time.sleep(sec)
            
   except KeyboardInterrupt:
        sys.exit(0)
