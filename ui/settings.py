from PyQt4.QtCore import QSettings, QVariant


class Settings(object):

    def __init__(self):
        self.settings = QSettings('settings.ini', QSettings.IniFormat)

    @property
    def local_port(self):
        return self.settings.value('SSH/local_port', QVariant(4000)).toInt()[0]

    @local_port.setter
    def local_port(self, value):
        self.settings.setValue('SSH/local_port', value)

    @property
    def username(self):
        return unicode(self.settings.value('SSH/username', QVariant()).toString())

    @username.setter
    def username(self, value):
        self.settings.setValue('SSH/username', value)

    @property
    def password(self):
        return unicode(self.settings.value('SSH/password', QVariant()).toString())

    @password.setter
    def password(self, value):
        self.settings.setValue('SSH/password', value)

    @property
    def key_path(self):
        return unicode(self.settings.value('SSH/key_path', QVariant()).toString())

    @key_path.setter
    def key_path(self, value):
        self.settings.setValue('SSH/key_path', value)

    @property
    def remote_host(self):
        return unicode(self.settings.value('SSH/remote_host', QVariant()).toString())

    @remote_host.setter
    def remote_host(self, value):
        self.settings.setValue('SSH/remote_host', value)

    @property
    def remote_port(self):
        return self.settings.value('SSH/remote_port', QVariant()).toInt()[0]

    @remote_port.setter
    def remote_port(self, value):
        self.settings.setValue('SSH/remote_port', value)

    @property
    def ssh_host(self):
        return unicode(self.settings.value('SSH/ssh_host', QVariant()).toString())

    @ssh_host.setter
    def ssh_host(self, value):
        self.settings.setValue('SSH/ssh_host', value)

    @property
    def ssh_port(self):
        return self.settings.value('SSH/ssh_port', QVariant(22)).toInt()[0]

    @ssh_port.setter
    def ssh_port(self, value):
        self.settings.setValue('SSH/ssh_port', value)
