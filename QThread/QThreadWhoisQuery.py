import requests
import whois
from PyQt5.QtCore import QThread, pyqtSignal


class WhoisQuery(QThread):
    result_whois_query = pyqtSignal(str, int)

    def __init__(self, target, parent=None):
        super(WhoisQuery, self).__init__(parent)
        self.target = target
        self.is_running = True

    def run(self):
        try:
            domain_info = whois.whois(self.target)
            if not domain_info:
                # self.result_whois_query.emit(f"未找到 {self.target} 的Whois信息", 1)
                self.result_whois_query.emit(f"未找到相关信息", 1)
                return
            self.result_whois_query.emit(f"域名: {domain_info.domain_name}", 2)
            self.result_whois_query.emit(f"注册商: {domain_info.registrar}", 2)
            self.result_whois_query.emit(f"创建时间: {domain_info.creation_date}", 2)
            self.result_whois_query.emit(f"到期时间: {domain_info.expiration_date}", 2)
            self.result_whois_query.emit(f"最后更新时间: {domain_info.updated_date}", 2)
            self.result_whois_query.emit(f"Name服务器: {', '.join(domain_info.name_servers)}", 2)
        except Exception as e:
            self.result_whois_query.emit(f"Whois查询出错: {str(e)}", 1)

    def stop(self):
        self.is_running = False
        print('stopping thread...SubdirScan')
        self.terminate()




