# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogFreq.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChooseFreq(object):                
    def setupUi(self, ChooseFreq):
        ChooseFreq.setObjectName("ChooseFreq")
        ChooseFreq.resize(367, 172)
        self.sec = 0
        self.buttonBox = QtWidgets.QDialogButtonBox(ChooseFreq)
        self.buttonBox.setGeometry(QtCore.QRect(20, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frequency = QtWidgets.QSpinBox(ChooseFreq)
        self.frequency.setGeometry(QtCore.QRect(220, 60, 42, 22))
        self.frequency.setObjectName("frequency")
        self.label = QtWidgets.QLabel(ChooseFreq)
        self.label.setGeometry(QtCore.QRect(270, 60, 51, 20))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(ChooseFreq)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 351, 131))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.raise_()
        self.buttonBox.raise_()
        self.frequency.raise_()
        self.label.raise_()
        self.frequency.valueChanged.connect(self.valuechange)
        self.retranslateUi(ChooseFreq)
        self.buttonBox.accepted.connect(ChooseFreq.accept)
        self.buttonBox.rejected.connect(ChooseFreq.reject)
        QtCore.QMetaObject.connectSlotsByName(ChooseFreq)
        
    def valuechange(self):
      self.sec = self.frequency.value()

    def retranslateUi(self, ChooseFreq):
        _translate = QtCore.QCoreApplication.translate
        ChooseFreq.setWindowTitle(_translate("ChooseFreq", "Choose Frequency"))
        self.label.setText(_translate("ChooseFreq", "SEC"))
        self.textBrowser.setHtml(_translate("ChooseFreq", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hello and Welcome!</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> <br /> Please Choose frequency of monitoring:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChooseFreq = QtWidgets.QDialog()
    ui = Ui_ChooseFreq()
    ui.setupUi(ChooseFreq)
    ChooseFreq.show()
    sys.exit(app.exec_())

