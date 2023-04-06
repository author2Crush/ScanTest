# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tool_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1213, 862)
        # Form.setUnifiedTitleAndToolBarOnMac(False)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 1200, 850))
        self.label.setMinimumSize(QtCore.QSize(1200, 850))
        self.label.setMaximumSize(QtCore.QSize(1200, 850))
        self.label.setStyleSheet("background-color: rgba(16,30,41,240);\n"
"border-radius:10px\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 1181, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.minimize_button = QtWidgets.QPushButton(self.layoutWidget)
        self.minimize_button.setMaximumSize(QtCore.QSize(20, 20))
        self.minimize_button.setStyleSheet("QPushButton#minimize_button{\n"
"    background-color:rgba(0,0,0,0);\n"
"    border:1px solid rgba(0,0,0,0);\n"
"}\n"
"QPushButton#minimize_button:hover{\n"
"    background-color:rgba(2,65,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#minimize_button:pressed{\n"
"    background-color:rgba(2,65,118,100);\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.minimize_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/minimsize_pushbutton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout_5.addWidget(self.minimize_button)
        self.close_button = QtWidgets.QPushButton(self.layoutWidget)
        self.close_button.setMaximumSize(QtCore.QSize(20, 20))
        self.close_button.setStyleSheet("\n"
"\n"
"QPushButton#close_button{\n"
"    background-color:rgba(0,0,0,0);\n"
"    border:1px solid rgba(0,0,0,0);\n"
"}\n"
"QPushButton#close_button:hover{\n"
"    background-color:rgba(2,65,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#close_button:pressed{\n"
"    background-color:rgba(2,65,118,100);\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.close_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/close_pushbutton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon1)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_5.addWidget(self.close_button)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(550, 10, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(255,255,255,200)")
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 70, 1141, 761))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(80, 25))
        self.label_2.setMaximumSize(QtCore.QSize(80, 25))
        self.label_2.setStyleSheet("color:rgba(255,255,255,200)")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(255,255,255,255);\n"
"padding-bottom:7px;\n"
"color:rgba(255,255,255,200)")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.export_results_button = QtWidgets.QPushButton(self.widget)
        self.export_results_button.setMinimumSize(QtCore.QSize(100, 25))
        self.export_results_button.setMaximumSize(QtCore.QSize(100, 25))
        self.export_results_button.setStyleSheet("QPushButton#export_results_button{\n"
"    background-color:rgba(2,62,118,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#export_results_button:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#export_results_button:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.export_results_button.setObjectName("export_results_button")
        self.horizontalLayout.addWidget(self.export_results_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_1 = QtWidgets.QPushButton(self.widget)
        self.button_1.setMinimumSize(QtCore.QSize(120, 25))
        self.button_1.setMaximumSize(QtCore.QSize(120, 25))
        self.button_1.setStyleSheet("QPushButton#button_1{\n"
"    background-color:rgba(2,62,118,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#button_1:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#button_1:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.button_1.setObjectName("button_1")
        self.horizontalLayout_2.addWidget(self.button_1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.button_2 = QtWidgets.QPushButton(self.widget)
        self.button_2.setMinimumSize(QtCore.QSize(120, 25))
        self.button_2.setMaximumSize(QtCore.QSize(120, 25))
        self.button_2.setStyleSheet("QPushButton#button_2{\n"
"    background-color:rgba(2,62,118,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#button_2:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#button_2:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.button_2.setObjectName("button_2")
        self.horizontalLayout_2.addWidget(self.button_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.button_3 = QtWidgets.QPushButton(self.widget)
        self.button_3.setMinimumSize(QtCore.QSize(120, 25))
        self.button_3.setMaximumSize(QtCore.QSize(120, 25))
        self.button_3.setStyleSheet("QPushButton#button_3{\n"
"    background-color:rgba(2,62,118,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#button_3:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#button_3:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.button_3.setObjectName("button_3")
        self.horizontalLayout_2.addWidget(self.button_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.button_4 = QtWidgets.QPushButton(self.widget)
        self.button_4.setMinimumSize(QtCore.QSize(120, 25))
        self.button_4.setMaximumSize(QtCore.QSize(120, 25))
        self.button_4.setStyleSheet("QPushButton#button_4{\n"
"    background-color:rgba(2,62,118,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#button_4:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#button_4:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.button_4.setObjectName("button_4")
        self.horizontalLayout_2.addWidget(self.button_4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.button_5 = QtWidgets.QPushButton(self.widget)
        self.button_5.setMinimumSize(QtCore.QSize(120, 25))
        self.button_5.setMaximumSize(QtCore.QSize(120, 25))
        self.button_5.setStyleSheet("QPushButton#button_5{\n"
"    background-color:rgba(2,62,118,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#button_5:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#button_5:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.button_5.setObjectName("button_5")
        self.horizontalLayout_2.addWidget(self.button_5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.button_6 = QtWidgets.QPushButton(self.widget)
        self.button_6.setMinimumSize(QtCore.QSize(120, 25))
        self.button_6.setMaximumSize(QtCore.QSize(120, 25))
        self.button_6.setStyleSheet("QPushButton#button_6{\n"
"    background-color:rgba(2,62,118,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#button_6:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#button_6:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.button_6.setObjectName("button_6")
        self.horizontalLayout_2.addWidget(self.button_6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.button_7 = QtWidgets.QPushButton(self.widget)
        self.button_7.setMinimumSize(QtCore.QSize(120, 25))
        self.button_7.setMaximumSize(QtCore.QSize(120, 25))
        self.button_7.setStyleSheet("QPushButton#button_7{\n"
"    background-color:rgba(2,62,118,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#button_7:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#button_7:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.button_7.setObjectName("button_7")
        self.horizontalLayout_2.addWidget(self.button_7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.button_8 = QtWidgets.QPushButton(self.widget)
        self.button_8.setMinimumSize(QtCore.QSize(120, 25))
        self.button_8.setMaximumSize(QtCore.QSize(120, 25))
        self.button_8.setStyleSheet("QPushButton#button_8{\n"
"    background-color:rgba(2,62,118,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#button_8:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#button_8:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.button_8.setObjectName("button_8")
        self.horizontalLayout_2.addWidget(self.button_8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setMinimumSize(QtCore.QSize(1100, 680))
        self.textEdit.setMaximumSize(QtCore.QSize(1140, 680))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(255,255,255,255);\n"
"padding-bottom:7px;\n"
"border-top-color:ragb(255,255,255,255);\n"
"padding-top:7px;\n"
"border-left-color:ragb(255,255,255,255);\n"
"padding-left:7px;\n"
"border-right-color:ragb(255,255,255,255);\n"
"padding-right:7px;\n"
"color:rgba(255,255,255,200);\n"
"border-radius:10px\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Tool"))
        self.label_2.setText(_translate("Form", "目标域名/IP:"))
        self.export_results_button.setText(_translate("Form", "导出结果"))
        self.button_1.setText(_translate("Form", "端口扫描"))
        self.button_2.setText(_translate("Form", "子域名扫描"))
        self.button_3.setText(_translate("Form", "Whois查询"))
        self.button_4.setText(_translate("Form", "DNS解析"))
        self.button_5.setText(_translate("Form", "邮箱收集"))
        self.button_6.setText(_translate("Form", "目录扫描"))
        self.button_7.setText(_translate("Form", "指纹识别"))
        self.button_8.setText(_translate("Form", "服务器信息"))
import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
