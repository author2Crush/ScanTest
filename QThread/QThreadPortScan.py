import re

from PyQt5.QtCore import QThread, pyqtSignal
import socket
import threading


class PortScan(QThread):
    result_port_scan = pyqtSignal(str, int)

    def __init__(self, target, parent=None):
        super(PortScan, self).__init__(parent)
        self.target = target
        self.is_running = True

    def run(self):
        try:
            ip = socket.gethostbyname(self.target)
            threads = []
            for port in range(1, 65536):
                t = threading.Thread(target=self.scan_port, args=(ip, port))
                threads.append(t)
                t.start()

            for t in threads:
                t.join()

        except Exception as e:
            self.result_port_scan.emit(f"端口扫描出错: {str(e)}", 1)

    def scan_port(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))
        if result == 0:
            self.result_port_scan.emit(f"端口 {port} 开放", 2)
        sock.close()

    def stop(self):
        self.is_running = False
        print('stopping thread...PortScan')
        self.terminate()
