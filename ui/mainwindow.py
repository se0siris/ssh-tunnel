import os
from functools import partial

from PyQt4.QtCore import QTimer, pyqtSignature
from PyQt4.QtGui import QMainWindow, QApplication, QSystemTrayIcon, QIcon, QFileDialog

from ui.Ui_mainwindow import Ui_MainWindow
from ui.custom_widgets import SystemTrayIcon
from ui.message_boxes import message_box_error
from ui.settings import Settings
from ui.ssh_tunnel import SSHTunnelThread

status_colours = {
    'red': '#7E2217',
    'green': '#347235'
}


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.app = QApplication.instance()
        self.setWindowTitle('{0:s} v{1:s}'.format(self.app.applicationName(), self.app.applicationVersion()))
        self.lbl_version.setText('Version {0:s}'.format(unicode(self.app.applicationVersion())))

        self.settings = Settings()
        self.load_settings()

        for spin_box in (self.sb_local_port, self.sb_ssh_port, self.sb_remote_port):
            spin_box.valueChanged.connect(self.save_settings)

        for line_edit in (self.le_ssh_host, self.le_ssh_username, self.le_ssh_password, self.le_ssh_private_key,
                          self.le_remote_host):
            line_edit.textChanged.connect(self.save_settings)

        self.ssh_tunnel = SSHTunnelThread()
        self.ssh_tunnel.error.connect(self.ssh_error)
        self.ssh_tunnel.server_started.connect(self.server_started)
        self.ssh_tunnel.server_stopped.connect(self.server_stopped)

        self.system_tray_icon = SystemTrayIcon(self)
        self.system_tray_icon.activated.connect(self.system_tray_icon_activated)
        self.system_tray_icon.set_icon_state(QIcon.Disabled)
        self.system_tray_icon.show()

        self.set_status_label('DISABLED', status_colours['red'])

        if self.settings_valid():
            press_server_enabled = partial(self.button_server_enabled.setChecked, True)
            QTimer().singleShot(0, press_server_enabled)

    def closeEvent(self, event):
        """
        @type event: QEvent
        """
        if self.sender() is self.system_tray_icon.exit_action or not self.ssh_tunnel.isRunning():
            QMainWindow.closeEvent(self, event)
            if self.ssh_tunnel.isRunning():
                self.stop_tunnel()
                self.ssh_tunnel.quit()
                self.ssh_tunnel.wait()
            self.app.quit()
        else:
            event.ignore()
            self.setVisible(False)

    def settings_valid(self):
        if not all((self.settings.local_port, self.settings.ssh_host, self.settings.ssh_port, self.settings.username,
                    self.settings.remote_host, self.settings.remote_port)):
            return False
        return True

    def load_settings(self):
        self.sb_local_port.setValue(self.settings.local_port)

        self.le_ssh_host.setText(self.settings.ssh_host)
        self.sb_ssh_port.setValue(self.settings.ssh_port)
        self.le_ssh_username.setText(self.settings.username)
        self.le_ssh_password.setText(self.settings.password)
        self.le_ssh_private_key.setText(self.settings.key_path)

        self.le_remote_host.setText(self.settings.remote_host)
        self.sb_remote_port.setValue(self.settings.remote_port)

    def save_settings(self):
        self.settings.local_port = self.sb_local_port.value()

        self.settings.ssh_host = self.le_ssh_host.text()
        self.settings.ssh_port = self.sb_ssh_port.value()
        self.settings.username = self.le_ssh_username.text()
        self.settings.password = self.le_ssh_password.text()
        self.settings.key_path = self.le_ssh_private_key.text()

        self.settings.remote_host = self.le_remote_host.text()
        self.settings.remote_port = self.sb_remote_port.value()

    def enable_settings(self, enabled=True):
        for widget in (self.grid_layout.itemAt(x).widget() for x in xrange(self.grid_layout.count())):
            widget.setEnabled(enabled)

    def server_started(self):
        self.set_status_label('CONNECTED', status_colours['green'])
        status = 'SSH Tunnel\nForwarding port {0:d} to {1:s}:{2:d} via {3:s}'.format(self.ssh_tunnel.local_port,
                                                                                     self.ssh_tunnel.remote_host,
                                                                                     self.ssh_tunnel.remote_port,
                                                                                     self.ssh_tunnel.ssh_host)
        self.system_tray_icon.setToolTip(status)
        self.system_tray_icon.set_icon_state(QIcon.Normal)
        self.enable_settings(False)
        self.system_tray_icon.showMessage('SSH Tunnel',
                                          'Server started',
                                          QSystemTrayIcon.Information,
                                          1000)

    def server_stopped(self):
        self.button_server_enabled.setChecked(False)
        self.set_status_label('DISCONNECTED', status_colours['red'])
        self.system_tray_icon.setToolTip('SSH Tunnel\nDisconnected')
        self.system_tray_icon.set_icon_state(QIcon.Disabled)
        self.enable_settings(True)
        self.system_tray_icon.showMessage('SSH Tunnel',
                                          'Server stopped',
                                          QSystemTrayIcon.Critical,
                                          1000)

    def set_status_label(self, text, colour='black'):
        self.lbl_status.setText('<font color="{0:s}">{1:s}</font>'.format(colour, text))

    def system_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.show()
            self.raise_()

    def start_tunnel(self):
        if self.ssh_tunnel.isRunning():
            message_box_error('Server already running',
                              'Cannot start SSH tunnel when it is already running.')
            return False
        self.set_status_label('Connecting...')
        self.enable_settings(False)
        self.system_tray_icon.setToolTip('SSH Tunnel\nConnecting...')
        self.ssh_tunnel.set_config()
        self.ssh_tunnel.start()

    def stop_tunnel(self):
        if not self.ssh_tunnel.isRunning():
            self.server_stopped()
            return False
        self.system_tray_icon.setToolTip('SSH Tunnel\nStopping...')
        self.set_status_label('Stopping...')

        self.ssh_tunnel.shutdown()

    def ssh_error(self, error_message):
        self.server_stopped()
        message_box_error('SSH Error', error_message)
        return

    @pyqtSignature('bool')
    def on_button_server_enabled_toggled(self, enabled):
        if enabled:
            self.start_tunnel()
        else:
            self.stop_tunnel()

    @pyqtSignature('')
    def on_button_browse_private_key_released(self):
        key_path = QFileDialog().getOpenFileName(self, 'Select private key file')
        if not key_path:
            return
        self.le_ssh_private_key.setText(os.path.normpath(unicode(key_path)))
