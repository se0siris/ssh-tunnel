"""
SSH Tunnel
Copyright (c) 2015 Gary Hughes
"""
import os
import traceback
from PyQt4 import QtGui
from PyQt4.QtCore import QLocale
from PyQt4.QtGui import QIcon, QPixmap
import time
from cStringIO import StringIO
from ui.mainwindow import MainWindow
import sys
from ui.message_boxes import message_box_error

VERSION = '1.0.1 (13/10/2015)'


def except_hook(exc_type, exc_value, traceback_obj):
    """
    Global function to catch unhandled exceptions.
    """
    separator = '-' * 80
    log_file = "error.log"
    notice = '''An unhandled exception occurred. Please report the problem
                via email to <a href="mailto:support@pearl-scan.co.uk">support@pearl-scan.co.uk</a>.<br>
                A log has been written to "<i>error.log</i>" in your application folder.<br><br>
                Error information:\n'''
    time_string = time.strftime("%Y-%m-%d, %H:%M:%S")
    machine_name = os.getenv('COMPUTERNAME')
    user_name = os.getenv('USERNAME')

    tb_info_file = StringIO()
    traceback.print_tb(traceback_obj, None, tb_info_file)
    tb_info_file.seek(0)
    tb_info = tb_info_file.read()
    error_message = '{0:s}: \n{1:s}'.format(str(exc_type), str(exc_value))
    sections = [separator, time_string,
                'Username: {0:s}'.format(user_name),
                'Machine: {0:s}'.format(machine_name),
                'Version: {0:s}'.format(VERSION),
                separator, error_message,
                separator, tb_info]
    msg = '\n'.join(sections)
    try:
        with open(log_file, 'w') as f:
            f.write(msg)
            f.write(VERSION)
    except IOError:
        pass
    message_box_error(notice, str(msg))


def startmain():
    """
    Initialise the application and display the main window.
    """
    app = QtGui.QApplication(sys.argv)

    icon = QIcon(QPixmap(':/icons/ssh_tunnel.svg'))
    app.setWindowIcon(icon)

    # If compiled as a one-file PyInstaller package look for Qt4 Plugins in the TEMP folder.
    try:
        extra_path = [os.path.join(sys._MEIPASS, 'qt4_plugins')]
        app.setLibraryPaths(app.libraryPaths() + extra_path)
    except AttributeError:
        pass

    # Error handling stuff.
    if hasattr(sys, 'frozen'):
        sys.excepthook = except_hook

    QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('CleanLooks'))
    QtGui.QApplication.setPalette(QtGui.QApplication.style().standardPalette())

    QtGui.QApplication.setApplicationName('SSH Tunnel')
    QtGui.QApplication.setApplicationVersion(VERSION)
    QtGui.QApplication.setOrganizationName('Pearl Scan Software')

    print 'AppName: %s' % QtGui.QApplication.applicationName()
    print 'AppVersion: %s' % QtGui.QApplication.applicationVersion()
    print 'Company Name: %s' % QtGui.QApplication.organizationName()

    QLocale.setDefault(QLocale(QLocale.English, QLocale.UnitedKingdom))

    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    startmain()

