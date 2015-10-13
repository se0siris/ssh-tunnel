import socket
import select
import SocketServer
from PyQt4.QtCore import QThread, pyqtSignal, QMutex, QString, QMutexLocker
import paramiko

from ui.settings import Settings


class SSHTunnelThread(QThread):
    # Signals.
    server_started = pyqtSignal()
    server_stopped = pyqtSignal()
    error = pyqtSignal(QString)

    mutex = QMutex()
    local_port = username = password = key_path = remote_host = remote_port = ssh_host = ssh_port = None

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.settings = Settings()
        self.tunnel = None
        self.set_config()

    def set_config(self):
        self.local_port = self.settings.local_port
        self.username = self.settings.username
        self.password = self.settings.password
        if self.settings.key_path:
            self.key_path = self.settings.key_path
        self.remote_host = self.settings.remote_host
        if self.settings.remote_port:
            self.remote_port = self.settings.remote_port
        self.ssh_host = self.settings.ssh_host
        self.ssh_port = self.settings.ssh_port

    def shutdown(self):
        with QMutexLocker(self.mutex):
            if self.tunnel:
                self.tunnel.shutdown()

    def run(self):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())

        print 'Connecting to SSH host {0:s}:{1:d}'.format(self.ssh_host, self.ssh_port)
        try:
            client.connect(self.ssh_host,
                           self.ssh_port,
                           self.username,
                           key_filename=self.key_path,
                           look_for_keys=False,
                           password=self.password)
        except Exception, e:
            error_message = 'Failed to connect to {0:s}:{1:d}: {2:s}'.format(self.ssh_host, self.ssh_port, e)
            print error_message
            self.error.emit(error_message)
            return

        transport = client.get_transport()
        transport.window_size = 3 * 1024 * 1024
        transport.set_keepalive(2.5 * 60)  # Set keep-alive to two and a half minutes.

        print 'Now forwarding port {0:d} to {1:s}:{2:d}...'.format(self.local_port, self.remote_host, self.remote_port)

        with QMutexLocker(self.mutex):
            try:
                self.tunnel = forward_tunnel(self.local_port,
                                             self.remote_host,
                                             self.remote_port,
                                             transport)
            except socket.error, e:
                self.error.emit(e.strerror)
                self.server_stopped.emit()
                return
        self.server_started.emit()
        self.tunnel.serve_forever()
        self.tunnel.server_close()
        self.server_stopped.emit()
        print 'Port forwarding stopped.'


class ForwardServer(SocketServer.ThreadingTCPServer):
    daemon_threads = True
    allow_reuse_address = False


class Handler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            chan = self.ssh_transport.open_channel('direct-tcpip',
                                                   (self.chain_host, self.chain_port),
                                                   self.request.getpeername())
        except Exception, e:
            print 'Incoming request to {0:s}:{1:d} failed: {2:s}'.format(self.chain_host,
                                                                         self.chain_port,
                                                                         repr(e))
            return
        if chan is None:
            print 'Incoming request to {0:s}:{1:d} was rejected by the SSH server.'.format(self.chain_host,
                                                                                           self.chain_port)
            return

        try:
            print 'Connected!  Tunnel open {0!r:s} -> {1!r:s} -> {2!r:s}'.format(self.request.getpeername(),
                                                                                 chan.getpeername(),
                                                                                 (self.chain_host, self.chain_port))
        except socket.error:
            pass

        while True:
            r, w, x = select.select([self.request, chan], [], [])
            if self.request in r:
                data = self.request.recv(1024)
                if len(data) == 0:
                    break
                chan.send(data)
            if chan in r:
                data = chan.recv(1024)
                if len(data) == 0:
                    break
                self.request.send(data)
        chan.close()
        self.request.close()
        try:
            print 'Tunnel closed from {0!r:s}'.format(self.request.getpeername(), )
        except socket.error:
            pass


def forward_tunnel(local_port, remote_host, remote_port, transport):
    # this is a little convoluted, but lets me configure things for the Handler
    # object.  (SocketServer doesn't give Handlers any way to access the outer
    # server normally.)
    class SubHandler(Handler):
        chain_host = remote_host
        chain_port = remote_port
        ssh_transport = transport

    return ForwardServer(('', local_port), SubHandler)
