# -*- coding: utf-8 -*-
#!/usr/bin/python
#!/bin/bash
"""
Created on Sat Apr  7 04:12:40 2018

@author: adiel
"""
import proc as pr
import compare as co
import fprint as fp
import fread as fr
import crypt_decrypt as cd
import sys, time
import database as db

def task_schd():
   #time_loop = int(input ('Decide how long time between each sample,\
    #                \nenter in minute and for secont 0.*: '))
    try:
        db.create_database();
        comp = False
        clist_start =[]
        clist_stop =[]
        prev_date = 0
        #print_status = 0
        #key = b'eju9_YGR2s5y6Ph-AFe1W-T4eCfvIoLc1NU8AfYlW9I='
        print("Starting...\n")
        while True:
            print("Get All Running Process...\n")
            proclist,date = pr.proc_list()
            
            if comp:
                print("Compare amd analyze...\n")
                #prev_list = fr.read_list("processList.txt")
                #prev_list = cd.decrypt_list(prev_list, key)
                prev_list = db.load_data_by_date(prev_date)
                clist_start, clist_stop = co.compare_process(proclist, prev_list)
                
                print("Print Status Log...\n")
                if clist_start: fp.print_list(clist_start)
                if clist_stop: fp.print_list(clist_stop)

                if not clist_start: comp = False
                
            else: 
                comp = True
            print("Print All Running Process...\n")
            #proclist = cd.crypt_list(proclist, key)
            db.insert_data(proclist)
            print(proclist[0])
            prev_date =date
            #print_status = fp.print_list(proclist)
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("Software is shuting down by the user...")
        sys.exit(0)
    
def shut_down():
    print("Software is shuting down...")
    with open("Status_Log.txt", "a") as plist:        
        plist.write("Software is DOWN!!...")
    sys.exit(1)
   
if __name__ == '__main__':
    task_schd()