import requests
from PyQt5.QtCore import QThread, pyqtSignal


class SubdirScan(QThread):
    result_subdir_scan = pyqtSignal(str, int)

    def __init__(self, target, parent=None):
        super(SubdirScan, self).__init__(parent)
        self.target = target
        self.is_running = True

    def run(self):
        try:
            with open("subdomains.txt", "r") as file:
                subdomains = file.readlines()
            found_subdomain = False
            for subdomain in subdomains:
                subdomain = subdomain.strip()
                try:
                    full_url = f"{subdomain}.{self.target}"
                    print(f"full_url:{full_url}")
                    requests.get(f"http://{full_url}", timeout=3)
                    self.result_subdir_scan.emit(f"找到子域名: {full_url}", 2)
                    found_subdomain = True
                except requests.exceptions.RequestException:
                    pass
            if not found_subdomain:
                self.result_subdir_scan.emit("没有相关信息", 1)
        except Exception as e:
            self.result_subdir_scan.emit(f"子域名扫描出错: {str(e)}", 1)

    def stop(self):
        self.is_running = False
        print('stopping thread...SubdirScan')
        self.terminate()


