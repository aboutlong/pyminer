# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_column_encode.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.listWidget_var = QtWidgets.QListWidget(self.widget_2)
        self.listWidget_var.setObjectName("listWidget_var")
        self.verticalLayout_2.addWidget(self.listWidget_var)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.addWidget(self.widget_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget_selecetd = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_selecetd.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget_selecetd.setObjectName("listWidget_selecetd")
        self.verticalLayout.addWidget(self.listWidget_selecetd)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_6.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_13.addWidget(self.tabWidget)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_help = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_help.setObjectName("pushButton_help")
        self.horizontalLayout_3.addWidget(self.pushButton_help)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_ok = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_3.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_cancel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_13.addWidget(self.widget_3)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "数据-重编码值"))
        self.label_3.setText(_translate("Form", "全部变量:"))
        self.groupBox_2.setTitle(_translate("Form", "已选变量"))
        self.groupBox_3.setTitle(_translate("Form", "选项"))
        self.label_8.setText(_translate("Form", "编码方案:"))
        self.comboBox_6.setItemText(0, _translate("Form", "OneHot"))
        self.pushButton.setText(_translate("Form", "预览"))
        self.groupBox_4.setTitle(_translate("Form", "重编码后预览"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "基本"))
        self.pushButton_help.setText(_translate("Form", "帮助"))
        self.pushButton_ok.setText(_translate("Form", "确定"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))
