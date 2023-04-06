import sys

import requests
import xlsxwriter
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog

from QThread.QThreadDirScan import DirScan
from QThread.QThreadDnsResolve import DnsResolve
from QThread.QThreadEmailCollect import EmailCollect
from QThread.QThreadFingerprintIdentification import FingerprintIdentification
from QThread.QThreadPortScan import PortScan
from QThread.QThreadServerInfo import ServerInfo
from QThread.QThreadSubdirScan import SubdirScan
from QThread.QThreadWhoisQuery import WhoisQuery
from py_ui.tool_main import Ui_Form
import utils.font_uitl as format


class ShowUI(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.thread_server_info = None
        self.thread_fingerprint_identification = None
        self.thread_dir_scan = None
        self.thread_email_collect = None
        self.thread_dns_resolve = None
        self.thread_whois_scan = None
        self.thread_subdir_scan = None
        self.thread_port_scan = None
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构建UI界面
        self.threads = []

    # =====================按钮=======================
    @pyqtSlot()
    def on_export_results_button_clicked(self):
        # 导出结果
        file_name, _ = QFileDialog.getSaveFileName(self, "导出结果", "", "Excel files (*.xls)")
        if file_name:
            if not file_name.endswith(".xls"):
                file_name += ".xls"
            workbook = xlsxwriter.Workbook(file_name)
            worksheet = workbook.add_worksheet()
            row = 0
            for line in self.ui.textEdit.toPlainText().split("\n"):
                worksheet.write(row, 0, line)
                row += 1
            workbook.close()
            self.format_font(f"结果已导出到: {file_name}", 2)

    @pyqtSlot()
    def on_button_1_clicked(self):
        # 端口扫描
        self.stop_threads()
        self.ui.textEdit.clear()
        target = self.ui.lineEdit.text()
        if not target:
            self.format_font("请先输入目标域名/IP", 1)
            return
        self.thread_port_scan = PortScan(target)
        self.threads.append(self.thread_port_scan)
        self.thread_port_scan.result_port_scan.connect(self.post_call_back)
        self.thread_port_scan.start()

    @pyqtSlot()
    def on_button_2_clicked(self):
        # 子域名扫描
        self.stop_threads()
        self.ui.textEdit.clear()
        target = self.ui.lineEdit.text()
        if not target:
            self.format_font("请先输入目标域名/IP", 1)
            return
        self.thread_subdir_scan = SubdirScan(target)
        self.threads.append(self.thread_subdir_scan)
        self.thread_subdir_scan.result_subdir_scan.connect(self.post_call_back)
        self.thread_subdir_scan.start()

    @pyqtSlot()
    def on_button_3_clicked(self):
        # Whois查询
        self.stop_threads()
        self.ui.textEdit.clear()
        target = self.ui.lineEdit.text()
        if not target:
            self.format_font("请先输入目标域名/IP", 1)
            return
        self.thread_whois_scan = WhoisQuery(target)
        self.threads.append(self.thread_whois_scan)
        self.thread_whois_scan.result_whois_query.connect(self.post_call_back)
        self.thread_whois_scan.start()

    @pyqtSlot()
    def on_button_4_clicked(self):
        # DNS解析
        self.stop_threads()
        self.ui.textEdit.clear()
        target = self.ui.lineEdit.text()
        if not target:
            self.format_font("请先输入目标域名/IP", 1)
            return
        self.thread_dns_resolve = DnsResolve(target)
        self.threads.append(self.thread_dns_resolve)
        self.thread_dns_resolve.result_dns_resolve.connect(self.post_call_back)
        self.thread_dns_resolve.start()

    @pyqtSlot()
    def on_button_5_clicked(self):
        # 邮箱收集
        self.stop_threads()
        self.ui.textEdit.clear()
        target = self.ui.lineEdit.text()
        if not target:
            self.format_font("请先输入目标域名/IP", 1)
            return
        self.thread_email_collect = EmailCollect(target)
        self.threads.append(self.thread_email_collect)
        self.thread_email_collect.result_email_collect.connect(self.post_call_back)
        self.thread_email_collect.start()

    @pyqtSlot()
    def on_button_6_clicked(self):
        # 目录扫描
        self.stop_threads()
        self.ui.textEdit.clear()
        target = self.ui.lineEdit.text()
        if not target:
            self.format_font("请先输入目标域名/IP", 1)
            return
        self.thread_dir_scan = DirScan(target)
        self.threads.append(self.thread_dir_scan)
        self.thread_dir_scan.result_dir_scan.connect(self.post_call_back)
        self.thread_dir_scan.start()

    @pyqtSlot()
    def on_button_7_clicked(self):
        # 指纹识别
        self.stop_threads()
        self.ui.textEdit.clear()
        target = self.ui.lineEdit.text()
        if not target:
            self.format_font("请先输入目标域名/IP", 1)
            return
        self.thread_fingerprint_identification = FingerprintIdentification(target)
        self.threads.append(self.thread_fingerprint_identification)
        self.thread_fingerprint_identification.result_fingerprint_identification.connect(self.post_call_back)
        self.thread_fingerprint_identification.start()

    @pyqtSlot()
    def on_button_8_clicked(self):
        # 服务器信息
        self.stop_threads()
        self.ui.textEdit.clear()
        target = self.ui.lineEdit.text()
        if not target:
            self.format_font("请先输入目标域名/IP", 1)
            return
        self.thread_server_info = ServerInfo(target)
        self.threads.append(self.thread_server_info)
        self.thread_server_info.result_server_info.connect(self.post_call_back)
        self.thread_server_info.start()

    @pyqtSlot()
    def on_minimize_button_clicked(self):
        self.showMinimized()

    @pyqtSlot()
    def on_close_button_clicked(self):
        self.close()

    # =====================自定义方法==================
    def format_font(self, msg, code):
        if code == 1:
            self.ui.textEdit.append(format.log_out_format(msg, '红色'))
        elif code == 2:
            self.ui.textEdit.append(format.log_out_format(msg, '绿色'))
        elif code == 3:
            self.ui.textEdit.append(format.log_out_format(msg, '黄色'))

        # self.ui.textEdit.append(format.log_out_format(f'--->>>response 1<<<---', '粉色'))
        # self.ui.textEdit.append(format.log_out_format(f'--->>>response 4<<<---', '橙色'))
        # self.ui.textEdit.append(format.log_out_format(f'--->>>response 5<<<---', '蓝绿'))
        # self.ui.textEdit.append(format.log_out_format(f'--->>>response 7<<<---', '蓝色'))
        # self.ui.textEdit.append(format.log_out_format(f'--->>>response 8<<<---', '茶色'))

    def post_call_back(self, msg, code):
        self.format_font(msg, code)

    def stop_threads(self):
        for item in self.threads:
            print(item)
            item.stop()
            self.threads.remove(item)

    ## ====================重写方法====================
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.Move = True
            self.Point = event.globalPos() - self.pos()
            event.accept()
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        if Qt.LeftButton and self.Move:
            self.move(event.globalPos() - self.Point)
            event.accept()
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.Move = False
        return super().mouseReleaseEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = ShowUI()  # 创建窗体
    form.show()
    sys.exit(app.exec_())


    #  background:QLinearGradient(x1:0,y1:0,x2:2,y2:0,stop:0 #666699,stop:1 #DB7093);
