# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draw.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_data = QtWidgets.QWidget()
        self.tab_data.setObjectName("tab_data")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_data)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.toolBox_2 = QtWidgets.QToolBox(self.tab_data)
        self.toolBox_2.setObjectName("toolBox_2")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 226, 405))
        self.page_6.setObjectName("page_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.page_6)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_11.addWidget(self.lineEdit)
        self.pushButton_3 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pyqt/source/images/sc_dataarearefresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_11.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.toolBox_2.addItem(self.page_6, "")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setGeometry(QtCore.QRect(0, 0, 226, 405))
        self.page_7.setObjectName("page_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_8 = QtWidgets.QLabel(self.page_7)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_12.addWidget(self.label_8)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_7)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_12.addWidget(self.lineEdit_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_12.addWidget(self.pushButton_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_9 = QtWidgets.QLabel(self.page_7)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_13.addWidget(self.label_9)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_7)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_13.addWidget(self.lineEdit_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_13.addWidget(self.pushButton_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_10 = QtWidgets.QLabel(self.page_7)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_14.addWidget(self.label_10)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_7)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_14.addWidget(self.lineEdit_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_14.addWidget(self.pushButton_6)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        self.toolBox_2.addItem(self.page_7, "")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setGeometry(QtCore.QRect(0, 0, 226, 405))
        self.page_8.setObjectName("page_8")
        self.toolBox_2.addItem(self.page_8, "")
        self.verticalLayout_4.addWidget(self.toolBox_2)
        self.tabWidget.addTab(self.tab_data, "")
        self.tab_style = QtWidgets.QWidget()
        self.tab_style.setObjectName("tab_style")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_style)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.toolBox = QtWidgets.QToolBox(self.tab_style)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 226, 353))
        self.page.setObjectName("page")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 226, 353))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.layoutWidget_7 = QtWidgets.QWidget(self.page_4)
        self.layoutWidget_7.setGeometry(QtCore.QRect(10, 10, 208, 25))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_7)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_15.addWidget(self.label_11)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_15.addWidget(self.lineEdit_5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem6)
        self.layoutWidget_8 = QtWidgets.QWidget(self.page_4)
        self.layoutWidget_8.setGeometry(QtCore.QRect(10, 40, 208, 25))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_8)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_16.addWidget(self.label_12)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget_8)
        self.spinBox.setProperty("value", 14)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_16.addWidget(self.spinBox)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem7)
        self.layoutWidget_9 = QtWidgets.QWidget(self.page_4)
        self.layoutWidget_9.setGeometry(QtCore.QRect(10, 100, 208, 25))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_9)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_17.addWidget(self.label_13)
        self.spinBox_2 = QtWidgets.QSpinBox(self.layoutWidget_9)
        self.spinBox_2.setProperty("value", 12)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_17.addWidget(self.spinBox_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem8)
        self.layoutWidget_10 = QtWidgets.QWidget(self.page_4)
        self.layoutWidget_10.setGeometry(QtCore.QRect(10, 70, 208, 25))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_10)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_18.addWidget(self.label_14)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget_10)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_18.addWidget(self.lineEdit_6)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem9)
        self.toolBox.addItem(self.page_4, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.page_5)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.page_5)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.page_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.page_5)
        self.doubleSpinBox.setMinimum(1.0)
        self.doubleSpinBox.setMaximum(10000.0)
        self.doubleSpinBox.setProperty("value", 400.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_6.addWidget(self.doubleSpinBox)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.page_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.page_5)
        self.doubleSpinBox_2.setMinimum(1.0)
        self.doubleSpinBox_2.setMaximum(10000.0)
        self.doubleSpinBox_2.setProperty("value", 300.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.horizontalLayout_7.addWidget(self.doubleSpinBox_2)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem13)
        self.toolBox.addItem(self.page_5, "")
        self.horizontalLayout_4.addWidget(self.toolBox)
        self.tabWidget.addTab(self.tab_style, "")
        self.tab_info = QtWidgets.QWidget()
        self.tab_info.setObjectName("tab_info")
        self.tabWidget.addTab(self.tab_info, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.widget_2 = QtWidgets.QWidget(self.splitter)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addWidget(self.splitter)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_help = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_help.setObjectName("pushButton_help")
        self.horizontalLayout_3.addWidget(self.pushButton_help)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
        self.pushButton_ok = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_3.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_cancel)
        self.verticalLayout.addWidget(self.widget_3)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        self.toolBox_2.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图形"))
        self.label_7.setText(_translate("Form", "数据:"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_6), _translate("Form", "数据"))
        self.label_8.setText(_translate("Form", "X 轴:"))
        self.label_9.setText(_translate("Form", "Y 轴:"))
        self.label_10.setText(_translate("Form", "数据:"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_7), _translate("Form", "角色"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_8), _translate("Form", "分类"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data), _translate("Form", "数据"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "基本"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "X 轴"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Form", "Y 轴"))
        self.label_11.setText(_translate("Form", "标题:"))
        self.label_12.setText(_translate("Form", "标题字体大小:"))
        self.label_13.setText(_translate("Form", "脚注字体大小:"))
        self.label_14.setText(_translate("Form", "脚注:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("Form", "标题和脚注"))
        self.label.setText(_translate("Form", "单位:"))
        self.comboBox.setItemText(0, _translate("Form", "像素（默认）"))
        self.comboBox.setItemText(1, _translate("Form", "厘米"))
        self.comboBox.setItemText(2, _translate("Form", "英寸"))
        self.label_2.setText(_translate("Form", "宽度:"))
        self.label_3.setText(_translate("Form", "高度:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("Form", "图形大小"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_style), _translate("Form", "外观"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_info), _translate("Form", "信息"))
        self.pushButton_help.setText(_translate("Form", "帮助"))
        self.pushButton_ok.setText(_translate("Form", "确定"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))
import pyqtsource_rc