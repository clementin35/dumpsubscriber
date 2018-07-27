# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtRemoveInputHook
import sys, time
import paramiko_shell as pr

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    app = QtGui.QApplication(sys.argv)
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(501, 278)
        self.formLayout = QtGui.QFormLayout(Form)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.splitter_4 = QtGui.QSplitter(Form)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.splitter_3 = QtGui.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.splitter = QtGui.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.splitter_2 = QtGui.QSplitter(self.splitter)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.widget = QtGui.QWidget(self.splitter_2)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ipEdit = QtGui.QLineEdit(self.widget)
        self.ipEdit.setObjectName(_fromUtf8("ipEdit"))
        self.verticalLayout.addWidget(self.ipEdit)
        self.passwordEdit = QtGui.QLineEdit(self.widget)
        self.passwordEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))
        self.verticalLayout.addWidget(self.passwordEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.pushButton = QtGui.QPushButton(self.splitter_2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.widget1 = QtGui.QWidget(self.splitter_3)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_3 = QtGui.QLabel(self.widget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.widget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lcdNumber = QtGui.QLCDNumber(self.widget1)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.verticalLayout_4.addWidget(self.lcdNumber)
        self.lcdNumber_2 = QtGui.QLCDNumber(self.widget1)
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.verticalLayout_4.addWidget(self.lcdNumber_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.tabWidget = QtGui.QTabWidget(self.splitter_4)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.columnView = QtGui.QColumnView(self.tab)
        self.columnView.setObjectName(_fromUtf8("columnView"))
        self.verticalLayout_3.addWidget(self.columnView)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listWidget_2 = QtGui.QListWidget(self.tab_2)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.gridLayout.addWidget(self.listWidget_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.splitter_4)
        self.label.raise_()
        self.label_2.raise_()
        self.ipEdit.raise_()
        self.passwordEdit.raise_()
        self.pushButton.raise_()
        self.tabWidget.raise_()
        self.lcdNumber.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lcdNumber_2.raise_()
        self.splitter_3.raise_()

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "IP Address", None))
        self.label_2.setText(_translate("Form", "Password", None))
        self.pushButton.setText(_translate("Form", "Connect", None))
        self.label_3.setText(_translate("Form", "Registered Subscriber", None))
        self.label_4.setText(_translate("Form", "Total Device Number", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Registered Subscribers", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "All Subscribers", None))
        self.pushButton.clicked.connect(self.createConnection)

    def sendEstablismentCommands(self, connection):
        connection.sendShell("telnet localhost 21000")
        time.sleep(5)
        connection.sendShell("admin")
        time.sleep(2)
        connection.sendShell("admin")
        time.sleep(2)
        connection.sendShell("cd imdb")
        time.sleep(2)
        connection.sendShell("dump subscriber")

        command = input('$ ')

    def createConnection(self):
        username = "ntappadm"
        ipAddress = self.ipEdit.text()
        password = self.passwordEdit.text()

        connection = pr.ssh(ipAddress, username, password)
        connection.openShell()
        pyqtRemoveInputHook() # For remove unnecessary items

        self.sendEstablismentCommands(connection) # Recursive
        self.isDone()

    def isDone(self):
        input("Enter your answer: ")
        QApplication.quit()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Ui_Form()
    window.show()
    sys.exit(app.exec_())
