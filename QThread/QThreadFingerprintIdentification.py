import requests
from PyQt5.QtCore import QThread, pyqtSignal
from bs4 import BeautifulSoup


class FingerprintIdentification(QThread):
    result_fingerprint_identification = pyqtSignal(str, int)

    def __init__(self, target, parent=None):
        super(FingerprintIdentification, self).__init__(parent)
        self.target = target
        self.is_running = True

    def run(self):
        try:
            url = f"http://{self.target}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            server = response.headers.get("Server", "无法识别")
            x_powered_by = response.headers.get("X-Powered-By", "无法识别")
            cms = "无法识别"

            if soup.find("meta", {"name": "generator"}):
                cms = soup.find("meta", {"name": "generator"})["content"]

            self.result_fingerprint_identification.emit(f"服务器: {server}", 2)
            self.result_fingerprint_identification.emit(f"X-Powered-By: {x_powered_by}", 2)
            self.result_fingerprint_identification.emit(f"内容管理系统 (CMS): {cms}", 2)

        except Exception as e:
            self.result_fingerprint_identification.emit(f"指纹识别出错: {str(e)}", 1)

    def stop(self):
        self.is_running = False
        print('stopping thread...FingerprintIdentification')
        self.terminate()




