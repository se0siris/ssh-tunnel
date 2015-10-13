from PyQt4.QtGui import QSystemTrayIcon, QApplication, QMenu, QIcon


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super(SystemTrayIcon, self).__init__(parent)
        self.set_icon_state(QIcon.Disabled)
        menu = QMenu(parent)
        self.exit_action = menu.addAction('E&xit')

        self.exit_action.triggered.connect(self.close_application)
        self.setContextMenu(menu)
        self.setToolTip(QApplication.instance().applicationName())

    def close_application(self):
        self.parent().close()

    def set_icon_state(self, state):
        pixmap = QApplication.instance().windowIcon().pixmap(256, 256, state)
        self.setIcon(QIcon(pixmap))
