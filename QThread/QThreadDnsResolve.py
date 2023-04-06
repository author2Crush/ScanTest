import dns.resolver
from PyQt5.QtCore import QThread, pyqtSignal


class DnsResolve(QThread):
    result_dns_resolve = pyqtSignal(str, int)

    def __init__(self, target, parent=None):
        super(DnsResolve, self).__init__(parent)
        self.target = target
        self.is_running = True

    def run(self):
        try:
            answers = dns.resolver.resolve(self.target, 'A')
            if not answers:
                self.result_dns_resolve.emit(f"未找到相关信息", 1)
                return
            for answer in answers:
                self.result_dns_resolve.emit(f"{self.target} 的 IP 地址：{answer.address}", 2)
        except Exception as e:
            self.result_dns_resolve.emit(f"DNS 解析错误: {str(e)}", 1)

    def stop(self):
        self.is_running = False
        print('stopping thread...DnsResolve')
        self.terminate()





