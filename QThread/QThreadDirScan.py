import requests
from PyQt5.QtCore import QThread, pyqtSignal
from bs4 import BeautifulSoup


class DirScan(QThread):
    result_dir_scan = pyqtSignal(str, int)

    def __init__(self, target, parent=None):
        super(DirScan, self).__init__(parent)
        self.target = target
        self.is_running = True
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/51.0.2704.63 Safari/537.36', 'Accept-Language': 'zh-CN,zh;q=0.9'}

    def run(self):
        try:
            url = f"http://{self.target}"
            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                self.result_dir_scan.emit(f"无法访问 {url}", 1)
                return
            soup = BeautifulSoup(response.text, 'html.parser')
            links = []
            for link in soup.find_all('a'):
                href = link.get('href')
                if href and href not in links:
                    links.append(href)
            if not links:
                self.result_dir_scan.emit(f"未找到相关信息", 1)
                return
            for link in links:
                self.result_dir_scan.emit(f"{self.target} 目录：{link}", 2)
        except Exception as e:
            self.result_dir_scan.emit(f"目录扫描出错: {str(e)}", 1)

    def stop(self):
        self.is_running = False
        print('stopping thread...DirScan')
        self.terminate()
