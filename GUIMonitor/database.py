# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 15:09:22 2018

@author: adiel
"""
import sqlite3
from sqlite3 import Error

def create_database():
    try:
        conn = sqlite3.connect('processList.db')
        cursor = conn.cursor()
        
        # Create table
        cursor.execute('''CREATE TABLE IF NOT EXISTS process (date text, pid int, name text, username text)''')
        conn.commit()
        conn.close()
    except Error as e:
        conn.close()
        create_database()
        print(e + "\nSome one maybe delete your database, it's could be malicous\n")
    return None

def create_database_stop():
    try:
        conn = sqlite3.connect('processList.db')
        cursor = conn.cursor()
        
        # Create table
        cursor.execute('''CREATE TABLE IF NOT EXISTS process_stop (date text, pid int, name text, username text)''')
        conn.commit()
        conn.close()
    except Error as e:
        conn.close()
        create_database()
        print(e + "\nSome one maybe delete your database, it's could be malicous\n")
    return None

def create_database_start():
    try:
        conn = sqlite3.connect('processList.db')
        cursor = conn.cursor()
        
        # Create table
        cursor.execute('''CREATE TABLE IF NOT EXISTS process_start (date text, pid int, name text, username text)''')
        conn.commit()
        conn.close()
    except Error as e:
        conn.close()
        create_database()
        print(e + "\nSome one maybe delete your database, it's could be malicous\n")
    return None

def insert_data(data):
    try:
        conn = sqlite3.connect('processList.db')
        c = conn.cursor()
        
        c.executemany('INSERT INTO process VALUES (?,?,?,?)', data)
        conn.commit()
        conn.close()
        return True
    except Error as e:
        conn.close()
        create_database()
        print(e + "\nSome one maybe delete your database, it's could be malicous\n")
    return False

def insert_data_start(data):
    try:
        if len(data) > 3:
            conn = sqlite3.connect('processList.db')
            c = conn.cursor()
            parse_data = []
            
            for proc in data[4:-2]:
                proc = proc.split('-')
                if proc:
                    if len(proc) > 3: parse_data.append((proc[0] , proc[1], proc[2], proc[3] + '-' + proc[4]))
                    else: parse_data.append((proc[0] , proc[1], proc[2], proc[3]))
                    
            c.executemany('INSERT INTO process_start VALUES (?,?,?,?)', parse_data)
            conn.commit()
            conn.close()
            return True
    except Error as e:
        conn.close()
        create_database_start()
        print(e + "\nSome one maybe delete your database, it's could be malicous\n")
    return False

def insert_data_stop(data):
    try:
        if len(data) > 2:
            conn = sqlite3.connect('processList.db')
            c = conn.cursor()
            parse_data = []
            
            for proc in data[1:-2]:
                proc = proc.split('-')
                if proc:
                    if len(proc) > 3: parse_data.append((proc[0] , proc[1], proc[2], proc[3] + '-' + proc[4]))
                    else: parse_data.append((proc[0] , proc[1], proc[2], proc[3]))
                    
            c.executemany('INSERT INTO process_stop VALUES (?,?,?,?)', parse_data)
            conn.commit()
            conn.close()
            return True
    except Error as e:
        conn.close()
        create_database_start()
        print(e + "\nSome one maybe delete your database, it's could be malicous\n")
    return False
    
def load_data_by_date(date):
    plist = []
    try:
        conn = sqlite3.connect('processList.db')
        cursor = conn.cursor()
        cursor = conn.execute("SELECT * from process WHERE date==? ORDER BY pid ASC", (date,))
        for row in cursor:
            plist.append((row[0], row[1], row[2] ,row[3]))
        
        conn.close()
    except Error as e:
        conn.close()
        create_database_stop()
        print(e + "\nSome one maybe delete your database, it's could be malicous\n")
    return plist

def delete():
    try:
        conn = sqlite3.connect('processList.db')
        cursor = conn.cursor()
        # Delete table
        cursor.execute('''DROP TABLE process''')
        conn.close()
    except Error as e:
        conn.close()
        print(e)
    return None

def is_empty():
    try:
        conn = sqlite3.connect('processList.db')
        cursor = conn.cursor()
        # Delete table
        cursor = conn.execute("SELECT COUNT() FROM process")
        row = (cursor.fetchall()[0][0])
        if row: return True
        conn.close()
    except Error as e:
        conn.close()
        create_database()
        print(e + "\nSome one maybe delete your database, it's could be malicous\n")
    return False

def date_list():
    plist = []
    try:
        conn = sqlite3.connect('processList.db')
        cursor = conn.cursor()
        cursor = conn.execute("SELECT distinct date FROM process order by date")
        for row in cursor:
            plist.append(row[0])
        
        conn.close()
    except Error as e:
        conn.close()
        create_database()
        print(e + "\nSome one maybe delete your database, it's could be malicous\n")
    return plist