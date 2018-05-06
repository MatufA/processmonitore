# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 04:55:30 2018

@author: adiel
"""
import time

def compare_process (list_to_compar, old_list):
    status_log_new = []
    status_log_old = []
    status_log_new.clear()
    status_log_old.clear()
    status_log_new.append(time.asctime(time.localtime(time.time())))
    status_log_new.append("Status Log")
    status_log_new.append("Process started:")
    status_log_old.append("Process stopped:")
    status_log_new.append("pid - name - username")
    
    if not old_list: return status_log_new.clear() ,status_log_old.clear()
    
#    if list_to_compar[0] == old_list[0]: return status_log_new.clear() ,status_log_old.clear()
    
    for line_new in list_to_compar[:]:
        new_pid = line_new[1]  
        for line_old in old_list[:]:
            old_pid = line_old[1]

            if new_pid == old_pid:
                old_list.pop(0)
                break

            else:
                if new_pid > old_pid: 
                    status_log_old.append(str(line_old[0]) + "-" + str(line_old[1]) + "-" \
                            + str(line_old[2])  + "-" + str(line_old[3]))
                    old_list.pop(0)
                    continue

                elif new_pid < old_pid: 
                    status_log_new.append(str(line_new[0]) + "-" + str(line_new[1]) + "-" \
                            + str(line_new[2])  + "-" + str(line_new[3]))
                    break
            
    status_log_new.extend(["Status_Log.txt" , False])
    status_log_old.extend(["Status_Log.txt" , False])
    return status_log_new ,status_log_old
    
    
    