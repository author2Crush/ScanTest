import re
import socket
from PyQt5.QtCore import QThread, pyqtSignal


class EmailCollect(QThread):
    result_email_collect = pyqtSignal(str, int)

    def __init__(self, target, parent=None):
        super(EmailCollect, self).__init__(parent)
        self.target = target
        self.is_running = True

    def run(self):
        try:
            ip = socket.gethostbyname(self.target)
            # 端口列表，限制扫描端口
            ports = [25, 465, 587, 2525]
            # 执行正则表达式匹配邮箱
            pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            for port in ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    # 匹配邮箱地址
                    resp = sock.recv(1024)
                    match = re.findall(pattern, resp.decode())
                    if match:
                        for email in match:
                            self.result_email_collect.emit(f"找到邮箱: {email}", 2)
                    sock.close()
        except Exception as e:
            self.result_email_collect.emit(f"邮箱收集出错: {str(e)}", 2)

    def stop(self):
        self.is_running = False
        print('stopping thread...EmailCollect')
        self.terminate()
