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
        print(e)
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
        print(e)
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
        print(e)
    return plist

def delete():
    try:
        conn = sqlite3.connect('processList.db')
        cursor = conn.cursor()
        # Delete table
        cursor.execute('''DROP TABLE process''')
        conn.close()
    except Error as e:
        print(e)
    return None