# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inspect_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(706, 201)
        Form.setStyleSheet("/* vertical scrollbar */\n"
"QScrollBar::vertical{\n"
"    border: none;\n"
"    background-color: #e9ecef;\n"
"    width: 12px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* handlebar vertical */\n"
"QScrollBar::handle::vertical{\n"
"    background-color: #52b788;\n"
"    max-height: 50px;\n"
"    border-radius: 6px;\n"
"}\n"
"QScrollBar::handle::vertical::hover{\n"
"    background-color: #74c69d;\n"
"}\n"
"QScrollBar::handle::vertical::pressed{\n"
"    background-color: #40916c;\n"
"}\n"
"\n"
"/* btn top-scroolbar*/\n"
"QScrollBar::sub-line::vertical{\n"
"    border: none;\n"
"    background-color: #e9ecef;\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line::vertical::hover{\n"
"    border: none;\n"
"    background-color: rgb(59,59,59);\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self._header = QtWidgets.QFrame(self.frame)
        self._header.setStyleSheet("background-color: #e9ecef;")
        self._header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._header.setFrameShadow(QtWidgets.QFrame.Raised)
        self._header.setObjectName("_header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self._header)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self._header_home_frame = QtWidgets.QFrame(self._header)
        self._header_home_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._header_home_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self._header_home_frame.setObjectName("_header_home_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self._header_home_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self._header_home_frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self._home_name_area = QtWidgets.QLabel(self.frame_2)
        self._home_name_area.setStyleSheet("font-size: 15px;\n"
"font-weight: 600;\n"
"")
        self._home_name_area.setAlignment(QtCore.Qt.AlignCenter)
        self._home_name_area.setObjectName("_home_name_area")
        self.verticalLayout_12.addWidget(self._home_name_area)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self._header_home_frame)
        self.frame_3.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self._home_icon_area = QtWidgets.QLabel(self.frame_3)
        self._home_icon_area.setMaximumSize(QtCore.QSize(100, 100))
        self._home_icon_area.setText("")
        self._home_icon_area.setObjectName("_home_icon_area")
        self.verticalLayout_4.addWidget(self._home_icon_area, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout_2.addWidget(self._header_home_frame)
        self._header_common_frame = QtWidgets.QFrame(self._header)
        self._header_common_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._header_common_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self._header_common_frame.setObjectName("_header_common_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self._header_common_frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_6 = QtWidgets.QFrame(self._header_common_frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self._home_score_area = QtWidgets.QLabel(self.frame_8)
        self._home_score_area.setStyleSheet("color: #000;\n"
"font-size: 35px;\n"
"font-weight: 700;")
        self._home_score_area.setAlignment(QtCore.Qt.AlignCenter)
        self._home_score_area.setObjectName("_home_score_area")
        self.verticalLayout_8.addWidget(self._home_score_area)
        self.horizontalLayout_3.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label = QtWidgets.QLabel(self.frame_9)
        self.label.setMinimumSize(QtCore.QSize(70, 45))
        self.label.setMaximumSize(QtCore.QSize(70, 45))
        self.label.setStyleSheet("color: #fff;\n"
"background-color: #52b788;\n"
"font-weight: 700;\n"
"font-size: 19px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.horizontalLayout_3.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_6)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self._away_score_area = QtWidgets.QLabel(self.frame_10)
        self._away_score_area.setStyleSheet("color: #000;\n"
"font-size: 35px;\n"
"font-weight: 700;")
        self._away_score_area.setAlignment(QtCore.Qt.AlignCenter)
        self._away_score_area.setObjectName("_away_score_area")
        self.verticalLayout_9.addWidget(self._away_score_area)
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self._header_common_frame)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self._week_area = QtWidgets.QLabel(self.frame_7)
        self._week_area.setStyleSheet("font-size: 15px;\n"
"font-weight: 600;\n"
"")
        self._week_area.setAlignment(QtCore.Qt.AlignCenter)
        self._week_area.setObjectName("_week_area")
        self.verticalLayout_7.addWidget(self._week_area)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.horizontalLayout_2.addWidget(self._header_common_frame)
        self._header_away_frame = QtWidgets.QFrame(self._header)
        self._header_away_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._header_away_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self._header_away_frame.setObjectName("_header_away_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self._header_away_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self._header_away_frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self._away_name_area = QtWidgets.QLabel(self.frame_4)
        self._away_name_area.setStyleSheet("font-size: 15px;\n"
"font-weight: 600;\n"
"")
        self._away_name_area.setAlignment(QtCore.Qt.AlignCenter)
        self._away_name_area.setObjectName("_away_name_area")
        self.verticalLayout_11.addWidget(self._away_name_area)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self._header_away_frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self._away_icon_area = QtWidgets.QLabel(self.frame_5)
        self._away_icon_area.setMaximumSize(QtCore.QSize(100, 100))
        self._away_icon_area.setText("")
        self._away_icon_area.setObjectName("_away_icon_area")
        self.verticalLayout_5.addWidget(self._away_icon_area, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.horizontalLayout_2.addWidget(self._header_away_frame)
        self.verticalLayout.addWidget(self._header)
        self._body = QtWidgets.QFrame(self.frame)
        self._body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._body.setFrameShadow(QtWidgets.QFrame.Raised)
        self._body.setObjectName("_body")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self._body)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self._tableWidget = QtWidgets.QTableWidget(self._body)
        self._tableWidget.setStyleSheet("/* table header style*/\n"
"QHeaderView::section{\n"
"    background-color:  #52b788;\n"
"    border-bottom: 0px solid rgb(141, 141, 141);\n"
"    border-top: 0px solid rgb(141,141,141);\n"
"    height: 30px;\n"
"    color: #ffffff;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QTableView{\n"
"    selection-background-color: rgb(222, 222, 222);\n"
"    background-color:  rgb(255, 255, 255);\n"
"    border: 2px solid rgb(141, 141, 141);\n"
"    gridline-color: rgb(141, 141, 141);\n"
"    text-align: center;\n"
"}\n"
"\n"
"QTableWidget{\n"
" border-radius: 4px;\n"
"}\n"
"\n"
"")
        self._tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self._tableWidget.setShowGrid(False)
        self._tableWidget.setObjectName("_tableWidget")
        self._tableWidget.setColumnCount(0)
        self._tableWidget.setRowCount(0)
        self.horizontalLayout_4.addWidget(self._tableWidget)
        self.verticalLayout.addWidget(self._body)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self._home_name_area.setText(_translate("Form", ".."))
        self._home_score_area.setText(_translate("Form", "5"))
        self.label.setText(_translate("Form", "MS"))
        self._away_score_area.setText(_translate("Form", "5"))
        self._week_area.setText(_translate("Form", ".."))
        self._away_name_area.setText(_translate("Form", ".."))
