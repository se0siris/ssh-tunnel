# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'S:\dev\Python\SSH Tunnel\ui\mainwindow.ui'
#
# Created: Tue Oct 13 10:34:36 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(487, 433)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/ssh_tunnel.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.lbl_version = QtGui.QLabel(self.centralwidget)
        self.lbl_version.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_version.setObjectName(_fromUtf8("lbl_version"))
        self.verticalLayout.addWidget(self.lbl_version)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(80, 80))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/ssh_tunnel.svg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.grid_layout = QtGui.QGridLayout()
        self.grid_layout.setObjectName(_fromUtf8("grid_layout"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.grid_layout.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.grid_layout.addWidget(self.label_3, 1, 1, 1, 1)
        self.sb_local_port = QtGui.QSpinBox(self.centralwidget)
        self.sb_local_port.setMaximum(9999)
        self.sb_local_port.setObjectName(_fromUtf8("sb_local_port"))
        self.grid_layout.addWidget(self.sb_local_port, 1, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.grid_layout.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.grid_layout.addWidget(self.label_6, 3, 1, 1, 1)
        self.le_ssh_host = QtGui.QLineEdit(self.centralwidget)
        self.le_ssh_host.setObjectName(_fromUtf8("le_ssh_host"))
        self.grid_layout.addWidget(self.le_ssh_host, 3, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.grid_layout.addWidget(self.label_5, 4, 1, 1, 1)
        self.sb_ssh_port = QtGui.QSpinBox(self.centralwidget)
        self.sb_ssh_port.setMaximum(9999)
        self.sb_ssh_port.setObjectName(_fromUtf8("sb_ssh_port"))
        self.grid_layout.addWidget(self.sb_ssh_port, 4, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.grid_layout.addWidget(self.label_7, 5, 1, 1, 1)
        self.le_ssh_username = QtGui.QLineEdit(self.centralwidget)
        self.le_ssh_username.setObjectName(_fromUtf8("le_ssh_username"))
        self.grid_layout.addWidget(self.le_ssh_username, 5, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.grid_layout.addWidget(self.label_8, 6, 1, 1, 1)
        self.le_ssh_password = QtGui.QLineEdit(self.centralwidget)
        self.le_ssh_password.setEchoMode(QtGui.QLineEdit.Password)
        self.le_ssh_password.setObjectName(_fromUtf8("le_ssh_password"))
        self.grid_layout.addWidget(self.le_ssh_password, 6, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.grid_layout.addWidget(self.label_11, 7, 1, 1, 1)
        self.le_ssh_private_key = QtGui.QLineEdit(self.centralwidget)
        self.le_ssh_private_key.setObjectName(_fromUtf8("le_ssh_private_key"))
        self.grid_layout.addWidget(self.le_ssh_private_key, 7, 2, 1, 1)
        self.button_browse_private_key = QtGui.QPushButton(self.centralwidget)
        self.button_browse_private_key.setObjectName(_fromUtf8("button_browse_private_key"))
        self.grid_layout.addWidget(self.button_browse_private_key, 7, 3, 1, 1)
        self.label_12 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.grid_layout.addWidget(self.label_12, 8, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.grid_layout.addWidget(self.label_13, 9, 1, 1, 1)
        self.le_remote_host = QtGui.QLineEdit(self.centralwidget)
        self.le_remote_host.setObjectName(_fromUtf8("le_remote_host"))
        self.grid_layout.addWidget(self.le_remote_host, 9, 2, 1, 1)
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.grid_layout.addWidget(self.label_14, 10, 1, 1, 1)
        self.sb_remote_port = QtGui.QSpinBox(self.centralwidget)
        self.sb_remote_port.setMaximum(9999)
        self.sb_remote_port.setObjectName(_fromUtf8("sb_remote_port"))
        self.grid_layout.addWidget(self.sb_remote_port, 10, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.grid_layout)
        spacerItem = QtGui.QSpacerItem(466, 23, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.lbl_status = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_status.sizePolicy().hasHeightForWidth())
        self.lbl_status.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_status.setFont(font)
        self.lbl_status.setObjectName(_fromUtf8("lbl_status"))
        self.horizontalLayout.addWidget(self.lbl_status)
        self.button_server_enabled = QtGui.QPushButton(self.centralwidget)
        self.button_server_enabled.setCheckable(True)
        self.button_server_enabled.setObjectName(_fromUtf8("button_server_enabled"))
        self.horizontalLayout.addWidget(self.button_server_enabled)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_3.setBuddy(self.sb_local_port)
        self.label_6.setBuddy(self.le_ssh_host)
        self.label_5.setBuddy(self.sb_ssh_port)
        self.label_7.setBuddy(self.le_ssh_username)
        self.label_8.setBuddy(self.le_ssh_password)
        self.label_11.setBuddy(self.le_ssh_private_key)
        self.label_13.setBuddy(self.le_remote_host)
        self.label_14.setBuddy(self.sb_remote_port)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SSH Tunnel", None))
        self.label_2.setText(_translate("MainWindow", "SSH Tunnel", None))
        self.lbl_version.setText(_translate("MainWindow", "Version", None))
        self.label_9.setText(_translate("MainWindow", "Local", None))
        self.label_3.setText(_translate("MainWindow", "Local port", None))
        self.label_10.setText(_translate("MainWindow", "SSH", None))
        self.label_6.setText(_translate("MainWindow", "SSH host", None))
        self.label_5.setText(_translate("MainWindow", "SSH port", None))
        self.label_7.setText(_translate("MainWindow", "Username", None))
        self.label_8.setText(_translate("MainWindow", "Password", None))
        self.label_11.setText(_translate("MainWindow", "Private key", None))
        self.button_browse_private_key.setText(_translate("MainWindow", "Browse", None))
        self.label_12.setText(_translate("MainWindow", "Remote", None))
        self.label_13.setText(_translate("MainWindow", "Remote host", None))
        self.label_14.setText(_translate("MainWindow", "Remote port", None))
        self.label_4.setText(_translate("MainWindow", "Status:", None))
        self.lbl_status.setText(_translate("MainWindow", "STATUS", None))
        self.button_server_enabled.setText(_translate("MainWindow", "Enabled", None))

import res_rc
