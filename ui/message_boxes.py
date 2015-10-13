from PyQt4.QtGui import QMessageBox, QSpacerItem, QSizePolicy

__author__ = 'Gary Hughes'


def message_box_ok_cancel(text, informative_text, title=None, icon=QMessageBox.Critical):
    msg_box = QMessageBox()
    msg_box.setText('<b>%s</b>' % text)
    if informative_text:
        msg_box.setInformativeText(informative_text)
    msg_box.setIcon(icon)
    if title:
        msg_box.setWindowTitle(title)
    else:
        msg_box.setWindowTitle('SSH Tunnel')
    msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg_box.setDefaultButton(QMessageBox.Ok)
    horizontal_spacer = QSpacerItem(400, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
    layout = msg_box.layout()
    layout.addItem(horizontal_spacer, layout.rowCount(), 0, 1, layout.columnCount())
    return msg_box.exec_()


def message_box_ok(text, informative_text, title=None, icon=QMessageBox.Information):
    msg_box = QMessageBox()
    msg_box.setText('<b>%s</b>' % text)
    if informative_text:
        msg_box.setInformativeText(informative_text)
    msg_box.setIcon(icon)
    if title:
        msg_box.setWindowTitle(title)
    else:
        msg_box.setWindowTitle('SSH Tunnel')
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.setDefaultButton(QMessageBox.Ok)
    horizontal_spacer = QSpacerItem(400, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
    layout = msg_box.layout()
    layout.addItem(horizontal_spacer, layout.rowCount(), 0, 1, layout.columnCount())
    return msg_box.exec_()


def message_box_error(text, informative_text, title=None, icon=QMessageBox.Critical):
    msg_box = QMessageBox()
    msg_box.setText('<b>%s</b>' % text)
    if informative_text:
        msg_box.setInformativeText(informative_text)
    msg_box.setIcon(icon)
    if title:
        msg_box.setWindowTitle(title)
    else:
        msg_box.setWindowTitle('SSH Tunnel')
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.setDefaultButton(QMessageBox.Ok)
    horizontal_spacer = QSpacerItem(400, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
    layout = msg_box.layout()
    layout.addItem(horizontal_spacer, layout.rowCount(), 0, 1, layout.columnCount())
    return msg_box.exec_()


def message_box_yes_no(text, informative_text, title=None, icon=QMessageBox.Question):
    msg_box = QMessageBox()
    msg_box.setText('<b>%s</b>' % text)
    if informative_text:
        msg_box.setInformativeText(informative_text)
    msg_box.setIcon(icon)
    if title:
        msg_box.setWindowTitle(title)
    else:
        msg_box.setWindowTitle('SSH Tunnel')
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg_box.setDefaultButton(QMessageBox.Yes)
    horizontal_spacer = QSpacerItem(400, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
    layout = msg_box.layout()
    layout.addItem(horizontal_spacer, layout.rowCount(), 0, 1, layout.columnCount())
    return msg_box.exec_()