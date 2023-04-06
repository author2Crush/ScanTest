import requests
from PyQt5.QtCore import QThread, pyqtSignal


class ServerInfo(QThread):
    result_server_info = pyqtSignal(str, int)

    def __init__(self, target, parent=None):
        super(ServerInfo, self).__init__(parent)
        self.target = target
        self.is_running = True

    def run(self):
        try:
            response = requests.get(f"http://{self.target}")
            server = response.headers.get("Server", "无法识别")
            self.result_server_info.emit(f"服务器信息: {server}", 2)
        except Exception as e:
            self.result_server_info.emit(f"服务器信息收集出错: {str(e)}", 1)

    def stop(self):
        self.is_running = False
        print('stopping thread...ServerInfo')
        self.terminate()





