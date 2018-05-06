# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:14:03 2018

@author: adiel
"""

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import database as db
import manual_UI as mui
import _thread as tr
from dialogFreq import Ui_ChooseFreq

class Ui_MainWindow(object):
    def load_all(self):
        #Load all MySql database
        try:
            conn = sqlite3.connect('processList.db')
            cursor = conn.cursor()
            cursor = conn.execute("SELECT * from process")
            self.showDB.setRowCount(0)
            for row_number, row_data in enumerate(cursor):
                self.showDB.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.showDB.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            
            conn.close()
        except db.Error as e:
            conn.close()
            db.create_database()
            print(e)
            
    def load_all_start(self):
        #Load all MySql database
        try:
            conn = sqlite3.connect('processList.db')
            cursor = conn.cursor()
            cursor = conn.execute("SELECT * from process_start")
            self.process_start_table.setRowCount(0)
            for row_number, row_data in enumerate(cursor):
                self.process_start_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.process_start_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            
            conn.close()
        except db.Error as e:
            conn.close()
            db.create_database_start()
            print(e)
            
    def load_all_stop(self):
        #Load all MySql database
        try:
            conn = sqlite3.connect('processList.db')
            cursor = conn.cursor()
            cursor = conn.execute("SELECT * from process_stop")
            self.process_stop_table.setRowCount(0)
            for row_number, row_data in enumerate(cursor):
                self.process_stop_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.process_stop_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            
            conn.close()
        except db.Error as e:
            conn.close()
            db.create_database_stop()
            print(e)
            
    def load_data_by_dateA(self, date):
        #Load all data of specipic date (left)
        try:
            conn = sqlite3.connect('processList.db')
            cursor = conn.cursor()
            cursor = conn.execute("SELECT * from process WHERE date==? ORDER BY pid ASC", (date,))
            self.listAwidget.setRowCount(0)
            for row_number, row_data in enumerate(cursor):
                self.listAwidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.listAwidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            
            conn.close()
        except db.Error as e:
            conn.close()
            db.create_database()
            print(e)
            
    def load_data_by_dateB(self, date):
        #Load all data of specipic date (right)
        try:
            conn = sqlite3.connect('processList.db')
            cursor = conn.cursor()
            cursor = conn.execute("SELECT * from process WHERE date==? ORDER BY pid ASC", (date,))
            self.listBwidget.setRowCount(0)
            for row_number, row_data in enumerate(cursor):
                self.listBwidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.listBwidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            
            conn.close()
        except db.Error as e:
            conn.close()
            db.create_database()
            print(e)
            
    def date(self):
        #List all exists datas from database
        listOfdate = db.date_list()
        self.firstBox.removeItem(0)
        self.secondBox.removeItem(0)
        for dt in listOfdate[:]:
            self.firstBox.addItem(str(dt))
            self.secondBox.addItem(str(dt))
            
    def comp(self):
        #Compare between spicipic dates ,show there data and show result - Button Actoin
        first = str(self.firstBox.currentText())
        second = str(self.secondBox.currentText())
        self.load_data_by_dateA(first)
        self.load_data_by_dateB(second)
        first_list, second_list = mui.manual_UI(first, second)
        for item in first_list[:-3]:
            self.compWidget.addItem(str(item))
        for item in second_list[:-3]:
            self.compWidget.addItem(str(item))
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(773, 573)
        #first tab - Monitor Mode
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StatusLog = QtWidgets.QTabWidget(self.centralwidget)
        self.StatusLog.setGeometry(QtCore.QRect(0, 0, 781, 581))
        self.StatusLog.setObjectName("StatusLog")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        #Show all of the database - table
        self.showDB = QtWidgets.QTableWidget(self.tab)
        self.showDB.setGeometry(QtCore.QRect(0, 0, 771, 491))
        self.showDB.setRowCount(20)
        self.showDB.setColumnCount(4)
        self.showDB.setObjectName("showDB")
        item = QtWidgets.QTableWidgetItem()
        self.showDB.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.showDB.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.showDB.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.showDB.setHorizontalHeaderItem(3, item)
        #Monitor button - start 
        self.monitor = QtWidgets.QPushButton(self.tab)
        self.monitor.setGeometry(QtCore.QRect(10, 500, 101, 41))
        self.monitor.setObjectName("monitor")
        self.monitor.clicked.connect(self.start_monitoring)
        #Show all the database button 
        self.ShowAll = QtWidgets.QPushButton(self.tab)
        self.ShowAll.setGeometry(QtCore.QRect(120, 500, 101, 41))
        self.ShowAll.setObjectName("ShowAll")
        self.ShowAll.clicked.connect(self.load_all)
        
        #second tab - StatusLog
        self.StatusLog.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        #Show resulte
        self.process_start_header = QtWidgets.QTextBrowser(self.tab_2)
        self.process_start_header.setGeometry(QtCore.QRect(10, 10, 181, 41))
        self.process_start_header.setObjectName("process_start_header")
        self.process_stop_header = QtWidgets.QTextBrowser(self.tab_2)
        self.process_stop_header.setGeometry(QtCore.QRect(390, 10, 181, 41))
        self.process_stop_header.setObjectName("process_stop_header")
        self.process_start_table = QtWidgets.QTableWidget(self.tab_2)
        self.process_start_table.setGeometry(QtCore.QRect(10, 60, 371, 481))
        self.process_start_table.setObjectName("process_start_table")
        self.process_start_table.setColumnCount(4)
        self.process_start_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.process_start_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.process_start_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.process_start_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.process_start_table.setHorizontalHeaderItem(3, item)
        self.process_stop_table = QtWidgets.QTableWidget(self.tab_2)
        self.process_stop_table.setGeometry(QtCore.QRect(390, 60, 371, 481))
        self.process_stop_table.setObjectName("process_stop_table")
        self.process_stop_table.setColumnCount(4)
        self.process_stop_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.process_stop_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.process_stop_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.process_stop_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.process_stop_table.setHorizontalHeaderItem(3, item)
        #Button Show All 
        #Show start
        self.show_bt_start = QtWidgets.QPushButton(self.tab_2)
        self.show_bt_start.setGeometry(QtCore.QRect(280, 10, 101, 41))
        self.show_bt_start.setObjectName("show_bt_start")
        self.show_bt_start.clicked.connect(self.load_all_start)
        #Show stop
        self.show_bt_stop = QtWidgets.QPushButton(self.tab_2)
        self.show_bt_stop.setGeometry(QtCore.QRect(660, 10, 101, 41))
        self.show_bt_stop.setObjectName("show_bt_stop")
        self.show_bt_stop.clicked.connect(self.load_all_stop)
        self.StatusLog.addTab(self.tab_2, "")
        
        #third tab - Manual Mode
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        #Show resulte
        self.compWidget = QtWidgets.QListWidget(self.tab_3)
        self.compWidget.setGeometry(QtCore.QRect(10, 210, 751, 291))
        self.compWidget.setObjectName("compWidget")
        #Pick a date - Left one
        self.firstBox = QtWidgets.QComboBox(self.tab_3)
        self.firstBox.setGeometry(QtCore.QRect(210, 510, 181, 21))
        self.firstBox.setEditable(False)
        self.firstBox.setCurrentText("Press refresh")
        self.firstBox.setObjectName("firstBox")
        self.firstBox.addItem("Press refresh")
        #Pick a date - Right one
        self.secondBox = QtWidgets.QComboBox(self.tab_3)
        self.secondBox.setGeometry(QtCore.QRect(480, 510, 181, 21))
        self.secondBox.setEditable(False)
        self.secondBox.setCurrentText("Press refresh")
        self.secondBox.addItem("Press refresh")
        self.secondBox.setObjectName("secondBox")
        #Refresh Button
        self.refreshComp = QtWidgets.QPushButton(self.tab_3)
        self.refreshComp.setGeometry(QtCore.QRect(680, 510, 75, 23))
        self.refreshComp.setObjectName("refreshComp")
        self.refreshComp.clicked.connect(self.date)
        #Compare Button
        self.compare = QtWidgets.QPushButton(self.tab_3)
        self.compare.setGeometry(QtCore.QRect(10, 500, 101, 41))
        self.compare.setObjectName("compare")
        self.compare.clicked.connect(self.comp)
        #Text pick a date
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(150, 510, 51, 20))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(400, 510, 71, 20))
        self.label_3.setObjectName("label_3")
        #Show a compare (left) data - table
        self.listAwidget = QtWidgets.QTableWidget(self.tab_3)
        self.listAwidget.setGeometry(QtCore.QRect(10, 10, 371, 192))
        self.listAwidget.setObjectName("listAwidget")
        self.listAwidget.setColumnCount(4)
        self.listAwidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.listAwidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listAwidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listAwidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.listAwidget.setHorizontalHeaderItem(3, item)
        #Show a compare (right) data - table
        self.listBwidget = QtWidgets.QTableWidget(self.tab_3)
        self.listBwidget.setGeometry(QtCore.QRect(390, 10, 371, 192))
        self.listBwidget.setObjectName("listBwidget")
        self.listBwidget.setColumnCount(4)
        self.listBwidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.listBwidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listBwidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listBwidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.listBwidget.setHorizontalHeaderItem(3, item)
        
        self.StatusLog.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        #Style and start up
        self.retranslateUi(MainWindow)
        self.StatusLog.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        #Style
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Process Monitor - By Adiel Matuf"))
        #MainWindow.setWindowIcon()
        item = self.showDB.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.showDB.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PID"))
        item = self.showDB.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Process Name"))
        item = self.showDB.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Owner"))
        self.monitor.setText(_translate("MainWindow", "Start  Monitor"))
        self.ShowAll.setText(_translate("MainWindow", "Show All"))
        self.StatusLog.setTabText(self.StatusLog.indexOf(self.tab), _translate("MainWindow", "Monitor"))
        self.process_start_header.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Process Start:</span></p></body></html>"))
        self.process_stop_header.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Process Stop:</span></p></body></html>"))
        item = self.process_start_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.process_start_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PID"))
        item = self.process_start_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Process Name"))
        item = self.process_start_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Owner"))
        item = self.process_stop_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.process_stop_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PID"))
        item = self.process_stop_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Process Name"))
        item = self.process_stop_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Owner"))
        self.show_bt_start.setText(_translate("MainWindow", "Show All Process"))
        self.show_bt_stop.setText(_translate("MainWindow", "Show All Process"))
        self.StatusLog.setTabText(self.StatusLog.indexOf(self.tab_2), _translate("MainWindow", "Status Log"))
        self.compare.setText(_translate("MainWindow", "Compare"))
        self.refreshComp.setText(_translate("MainWindow", "Refresh"))
        self.label.setText(_translate("MainWindow", "First Date:"))
        self.label_3.setText(_translate("MainWindow", "Second Date:"))
        item = self.listAwidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.listAwidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PID"))
        item = self.listAwidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Process Name"))
        item = self.listAwidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Owner"))
        item = self.listBwidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.listBwidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PID"))
        item = self.listBwidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Process Name"))
        item = self.listBwidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Owner"))
        self.StatusLog.setTabText(self.StatusLog.indexOf(self.tab_3), _translate("MainWindow", "Manual"))

    def start_monitoring(self):
            #Pop up a new window and retrive data (sec), start thread monitoring 
            ChooseFreq = QtWidgets.QDialog()
            ui = Ui_ChooseFreq()
            ui.setupUi(ChooseFreq)
            ChooseFreq.show()
            if ChooseFreq.exec_():
                seconds = ui.sec
                if(seconds > 0):
                    tr.start_new_thread(self.monitoring_UI, (seconds,))


    def monitoring_UI(self, sec):
        #Monitoring Function
        import proc as pr
        import compare as co
        import fprint as fp
        import time
        import database as db
        #Create MySql database if not exitsts
        db.create_database();
        db.create_database_start();
        db.create_database_stop();
        comp = False
        clist_start =[]
        clist_stop =[]
        prev_date = 0
        self.loop = True
        while self.loop:
            #List all running process
            proclist,date = pr.proc_list()
            
            if comp:
                #Compare amd analyze
                prev_list = db.load_data_by_date(prev_date)
                clist_start, clist_stop = co.compare_process(proclist, prev_list)
                
                #Print Status Log - to the screen and to StatusLog.txt
                if clist_start: 
                    fp.print_list(clist_start)
                    db.insert_data_start(clist_start)
                    '''for item in clist_start[:-2]:
                        self.status.addItem(str(item))'''
                    
                if clist_stop: 
                    fp.print_list(clist_stop)
                    db.insert_data_stop(clist_stop)
                    '''for item in clist_stop[:-2]:
                        self.status.addItem(str(item))'''

                if not clist_start: comp = False
                
            else: 
                comp = True
            # Insert All Running Process to database and sleep
            db.insert_data(proclist)
            prev_date =date
            time.sleep(sec)

#Starting up process
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

