# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'package_update.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_name.setText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name)
        self.checkBox_version = QtWidgets.QCheckBox(Form)
        self.checkBox_version.setObjectName("checkBox_version")
        self.formLayout.setWidget(
            1,
            QtWidgets.QFormLayout.LabelRole,
            self.checkBox_version)
        self.comboBox_version = QtWidgets.QComboBox(Form)
        self.comboBox_version.setEnabled(False)
        self.comboBox_version.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox_version.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_version.setObjectName("comboBox_version")
        self.comboBox_version.addItem("")
        self.formLayout.setWidget(
            1,
            QtWidgets.QFormLayout.FieldRole,
            self.comboBox_version)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox_source = QtWidgets.QComboBox(Form)
        self.comboBox_source.setEnabled(True)
        self.comboBox_source.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_source.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_source.setObjectName("comboBox_source")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_source)
        self.lineEdit_source = QtWidgets.QLineEdit(Form)
        self.lineEdit_source.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEdit_source.setReadOnly(True)
        self.lineEdit_source.setObjectName("lineEdit_source")
        self.horizontalLayout_3.addWidget(self.lineEdit_source)
        self.formLayout.setLayout(
            2,
            QtWidgets.QFormLayout.FieldRole,
            self.horizontalLayout_3)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_dir = QtWidgets.QComboBox(Form)
        self.comboBox_dir.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_dir.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_dir.setObjectName("comboBox_dir")
        self.comboBox_dir.addItem("")
        self.comboBox_dir.addItem("")
        self.comboBox_dir.addItem("")
        self.comboBox_dir.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_dir)
        self.lineEdit_dir = QtWidgets.QLineEdit(Form)
        self.lineEdit_dir.setReadOnly(True)
        self.lineEdit_dir.setObjectName("lineEdit_dir")
        self.horizontalLayout.addWidget(self.lineEdit_dir)
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.formLayout.setLayout(
            3,
            QtWidgets.QFormLayout.FieldRole,
            self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textEdit_desc = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_desc.setObjectName("textEdit_desc")
        self.horizontalLayout_5.addWidget(self.textEdit_desc)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.textEdit_log = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_log.setObjectName("textEdit_log")
        self.horizontalLayout_6.addWidget(self.textEdit_log)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_ok = QtWidgets.QPushButton(self.widget)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_2.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_2.addWidget(self.pushButton_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "更新"))
        self.label_2.setText(_translate("Form", "包名:"))
        self.checkBox_version.setText(_translate("Form", "指定版本"))
        self.comboBox_version.setItemText(0, _translate("Form", "最新版本"))
        self.label.setText(_translate("Form", "下载源:"))
        self.comboBox_source.setItemText(0, _translate("Form", "腾讯(推荐)"))
        self.comboBox_source.setItemText(1, _translate("Form", "官方"))
        self.comboBox_source.setItemText(2, _translate("Form", "清华大学"))
        self.comboBox_source.setItemText(3, _translate("Form", "阿里"))
        self.comboBox_source.setItemText(4, _translate("Form", "豆瓣"))
        self.comboBox_source.setItemText(5, _translate("Form", "自定义"))
        self.lineEdit_source.setText(
            _translate(
                "Form",
                "https://mirrors.cloud.tencent.com/pypi/simple"))
        self.lineEdit_source.setPlaceholderText(_translate("Form", "腾讯镜像源"))
        self.label_3.setText(_translate("Form", "安装选项:"))
        self.comboBox_dir.setItemText(0, _translate("Form", "默认位置"))
        self.comboBox_dir.setItemText(1, _translate("Form", "用户目录"))
        self.comboBox_dir.setItemText(2, _translate("Form", "仅下载"))
        self.comboBox_dir.setItemText(3, _translate("Form", "自定义"))
        self.lineEdit_dir.setPlaceholderText(_translate("Form", "默认"))
        self.toolButton.setText(_translate("Form", "..."))
        self.groupBox.setTitle(_translate("Form", "详情"))
        self.groupBox_2.setTitle(_translate("Form", "执行记录"))
        self.pushButton_ok.setText(_translate("Form", "确定"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))
