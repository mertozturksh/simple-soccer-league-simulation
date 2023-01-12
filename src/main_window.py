# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(970, 568)
        MainWindow.setMinimumSize(QtCore.QSize(0, 568))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 568))
        MainWindow.setStyleSheet("/* vertical scrollbar */\n"
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
        MainWindow.setIconSize(QtCore.QSize(40, 40))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self._header = QtWidgets.QFrame(self.centralwidget)
        self._header.setMinimumSize(QtCore.QSize(0, 55))
        self._header.setMaximumSize(QtCore.QSize(16777215, 65))
        self._header.setStyleSheet("background-color: #e9ecef;")
        self._header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._header.setFrameShadow(QtWidgets.QFrame.Raised)
        self._header.setObjectName("_header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self._header)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self._header_menu_button = QtWidgets.QPushButton(self._header)
        self._header_menu_button.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 20px;\n"
"  font-weight: 700;\n"
"  line-height: 20px;\n"
"  padding: 8px 70px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._header_menu_button.setObjectName("_header_menu_button")
        self.horizontalLayout.addWidget(self._header_menu_button)
        spacerItem = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self._header)
        self._body = QtWidgets.QFrame(self.centralwidget)
        self._body.setStyleSheet("background-color: rgb(255,255, 255);")
        self._body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._body.setFrameShadow(QtWidgets.QFrame.Raised)
        self._body.setObjectName("_body")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self._body)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self._left_menu = QtWidgets.QFrame(self._body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._left_menu.sizePolicy().hasHeightForWidth())
        self._left_menu.setSizePolicy(sizePolicy)
        self._left_menu.setMinimumSize(QtCore.QSize(0, 0))
        self._left_menu.setMaximumSize(QtCore.QSize(224, 16777215))
        self._left_menu.setStyleSheet("QFrame{\n"
"    background-color: #ffffff;\n"
" border-top-right-radius: 15px;\n"
" border-top-left-radius: 15px;\n"
"}")
        self._left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self._left_menu.setObjectName("_left_menu")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self._left_menu)
        self.stackedWidget_2.setGeometry(QtCore.QRect(0, 30, 224, 481))
        self.stackedWidget_2.setMaximumSize(QtCore.QSize(225, 16777215))
        self.stackedWidget_2.setStyleSheet("background-color: #e9ecef;")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setStyleSheet("border-right: 4px solid #52b788;")
        self.page_3.setObjectName("page_3")
        self._menu_table_button = QtWidgets.QPushButton(self.page_3)
        self._menu_table_button.setGeometry(QtCore.QRect(10, 30, 201, 35))
        self._menu_table_button.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_table_button.setObjectName("_menu_table_button")
        self._menu_statistics_button = QtWidgets.QPushButton(self.page_3)
        self._menu_statistics_button.setGeometry(QtCore.QRect(10, 130, 201, 35))
        self._menu_statistics_button.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_statistics_button.setObjectName("_menu_statistics_button")
        self._menu_restart_button = QtWidgets.QPushButton(self.page_3)
        self._menu_restart_button.setGeometry(QtCore.QRect(10, 414, 201, 41))
        self._menu_restart_button.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_restart_button.setObjectName("_menu_restart_button")
        self._menu_fixture_button = QtWidgets.QPushButton(self.page_3)
        self._menu_fixture_button.setGeometry(QtCore.QRect(10, 80, 201, 35))
        self._menu_fixture_button.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_fixture_button.setObjectName("_menu_fixture_button")
        self._menu_simulate_button = QtWidgets.QPushButton(self.page_3)
        self._menu_simulate_button.setGeometry(QtCore.QRect(10, 354, 201, 41))
        self._menu_simulate_button.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_simulate_button.setObjectName("_menu_simulate_button")
        self._menu_play_current_week_button = QtWidgets.QPushButton(self.page_3)
        self._menu_play_current_week_button.setGeometry(QtCore.QRect(10, 300, 201, 41))
        self._menu_play_current_week_button.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_play_current_week_button.setObjectName("_menu_play_current_week_button")
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setStyleSheet("")
        self.page_4.setObjectName("page_4")
        self.scrollArea = QtWidgets.QScrollArea(self.page_4)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 224, 481))
        self.scrollArea.setStyleSheet("border:none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 100, 1030))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 1030))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self._menu_teams_0 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_0.setGeometry(QtCore.QRect(10, 20, 191, 38))
        self._menu_teams_0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self._menu_teams_0.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_0.setObjectName("_menu_teams_0")
        self._menu_teams_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_1.setGeometry(QtCore.QRect(10, 70, 191, 38))
        self._menu_teams_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self._menu_teams_1.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_1.setObjectName("_menu_teams_1")
        self._menu_teams_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_2.setGeometry(QtCore.QRect(10, 120, 191, 38))
        self._menu_teams_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self._menu_teams_2.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_2.setObjectName("_menu_teams_2")
        self._menu_teams_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_3.setGeometry(QtCore.QRect(10, 170, 191, 38))
        self._menu_teams_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._menu_teams_3.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_3.setObjectName("_menu_teams_3")
        self._menu_teams_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_4.setGeometry(QtCore.QRect(10, 220, 191, 38))
        self._menu_teams_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._menu_teams_4.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_4.setObjectName("_menu_teams_4")
        self._menu_teams_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_5.setGeometry(QtCore.QRect(10, 270, 191, 38))
        self._menu_teams_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._menu_teams_5.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_5.setObjectName("_menu_teams_5")
        self._menu_teams_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_6.setGeometry(QtCore.QRect(10, 320, 191, 38))
        self._menu_teams_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._menu_teams_6.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_6.setObjectName("_menu_teams_6")
        self._menu_teams_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_7.setGeometry(QtCore.QRect(10, 370, 191, 38))
        self._menu_teams_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._menu_teams_7.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_7.setObjectName("_menu_teams_7")
        self._menu_teams_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_8.setGeometry(QtCore.QRect(10, 420, 191, 38))
        self._menu_teams_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._menu_teams_8.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_8.setObjectName("_menu_teams_8")
        self._menu_teams_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_9.setGeometry(QtCore.QRect(10, 470, 191, 38))
        self._menu_teams_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._menu_teams_9.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_9.setObjectName("_menu_teams_9")
        self._menu_teams_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_10.setGeometry(QtCore.QRect(10, 520, 191, 38))
        self._menu_teams_10.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._menu_teams_10.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_10.setObjectName("_menu_teams_10")
        self._menu_teams_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_11.setGeometry(QtCore.QRect(10, 570, 191, 38))
        self._menu_teams_11.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._menu_teams_11.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_11.setObjectName("_menu_teams_11")
        self._menu_teams_12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_12.setGeometry(QtCore.QRect(10, 620, 191, 38))
        self._menu_teams_12.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._menu_teams_12.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_12.setObjectName("_menu_teams_12")
        self._menu_teams_13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_13.setGeometry(QtCore.QRect(10, 670, 191, 38))
        self._menu_teams_13.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._menu_teams_13.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_13.setObjectName("_menu_teams_13")
        self._menu_teams_14 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_14.setGeometry(QtCore.QRect(10, 720, 191, 38))
        self._menu_teams_14.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._menu_teams_14.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_14.setObjectName("_menu_teams_14")
        self._menu_teams_15 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_15.setGeometry(QtCore.QRect(10, 770, 191, 38))
        self._menu_teams_15.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._menu_teams_15.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_15.setObjectName("_menu_teams_15")
        self._menu_teams_16 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_16.setGeometry(QtCore.QRect(10, 820, 191, 38))
        self._menu_teams_16.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._menu_teams_16.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_16.setObjectName("_menu_teams_16")
        self._menu_teams_17 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_17.setGeometry(QtCore.QRect(10, 870, 191, 38))
        self._menu_teams_17.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._menu_teams_17.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_17.setObjectName("_menu_teams_17")
        self._menu_teams_18 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_18.setGeometry(QtCore.QRect(10, 920, 191, 38))
        self._menu_teams_18.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._menu_teams_18.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_18.setObjectName("_menu_teams_18")
        self._menu_teams_19 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self._menu_teams_19.setGeometry(QtCore.QRect(10, 970, 191, 38))
        self._menu_teams_19.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._menu_teams_19.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_19.setObjectName("_menu_teams_19")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget_2.addWidget(self.page_4)
        self._menu_general_button = QtWidgets.QPushButton(self._left_menu)
        self._menu_general_button.setGeometry(QtCore.QRect(-1, -2, 113, 34))
        self._menu_general_button.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  color: #fff;\n"
" font-size: 18px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 6px 16px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_general_button.setObjectName("_menu_general_button")
        self._menu_teams_button = QtWidgets.QPushButton(self._left_menu)
        self._menu_teams_button.setGeometry(QtCore.QRect(111, -2, 114, 34))
        self._menu_teams_button.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  color: #fff;\n"
" font-size: 18px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 6px 16px;\n"
"  border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._menu_teams_button.setObjectName("_menu_teams_button")
        self.horizontalLayout_2.addWidget(self._left_menu)
        self._main_menu = QtWidgets.QFrame(self._body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._main_menu.sizePolicy().hasHeightForWidth())
        self._main_menu.setSizePolicy(sizePolicy)
        self._main_menu.setMinimumSize(QtCore.QSize(0, 0))
        self._main_menu.setStyleSheet("background-color: #edf6f9;")
        self._main_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._main_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self._main_menu.setObjectName("_main_menu")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self._main_menu)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self._main_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setContentsMargins(0, 4, 0, 4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self._body_table_tableWidget = QtWidgets.QTableWidget(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._body_table_tableWidget.sizePolicy().hasHeightForWidth())
        self._body_table_tableWidget.setSizePolicy(sizePolicy)
        self._body_table_tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self._body_table_tableWidget.setMaximumSize(QtCore.QSize(10000, 500616))
        self._body_table_tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self._body_table_tableWidget.setStyleSheet("/* table header style*/\n"
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
        self._body_table_tableWidget.setLineWidth(0)
        self._body_table_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self._body_table_tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self._body_table_tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self._body_table_tableWidget.setShowGrid(False)
        self._body_table_tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self._body_table_tableWidget.setCornerButtonEnabled(False)
        self._body_table_tableWidget.setObjectName("_body_table_tableWidget")
        self._body_table_tableWidget.setColumnCount(10)
        self._body_table_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self._body_table_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self._body_table_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self._body_table_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self._body_table_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self._body_table_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self._body_table_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self._body_table_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self._body_table_tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self._body_table_tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self._body_table_tableWidget.setHorizontalHeaderItem(9, item)
        self._body_table_tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout_3.addWidget(self._body_table_tableWidget)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setContentsMargins(0, 4, 0, 4)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame = QtWidgets.QFrame(self.page_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self._body_fixture_tableWidget = QtWidgets.QTableWidget(self.frame)
        self._body_fixture_tableWidget.setStyleSheet("/* table header style*/\n"
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
        self._body_fixture_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self._body_fixture_tableWidget.setShowGrid(False)
        self._body_fixture_tableWidget.setObjectName("_body_fixture_tableWidget")
        self._body_fixture_tableWidget.setColumnCount(0)
        self._body_fixture_tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self._body_fixture_tableWidget)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setContentsMargins(-1, 5, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self._body_previous_button = QtWidgets.QPushButton(self.frame_2)
        self._body_previous_button.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._body_previous_button.setObjectName("_body_previous_button")
        self.horizontalLayout_5.addWidget(self._body_previous_button)
        self._body_current_button = QtWidgets.QPushButton(self.frame_2)
        self._body_current_button.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._body_current_button.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self._body_current_button.setObjectName("_body_current_button")
        self.horizontalLayout_5.addWidget(self._body_current_button)
        self._body_next_button = QtWidgets.QPushButton(self.frame_2)
        self._body_next_button.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._body_next_button.setObjectName("_body_next_button")
        self.horizontalLayout_5.addWidget(self._body_next_button)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout_4.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.page_2)
        self.frame_3.setMinimumSize(QtCore.QSize(30, 481))
        self.frame_3.setMaximumSize(QtCore.QSize(30, 481))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(3, 32, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem1)
        self._body_inspect_button_0 = QtWidgets.QPushButton(self.frame_3)
        self._body_inspect_button_0.setMinimumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_0.setMaximumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_0.setStyleSheet("QPushButton{\n"
"    border: 0;\n"
"    background-color: #e9ecef;\n"
"    border-radius: 5px;\n"
"    image: url(src/uparrow.png);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #dee2e6;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #ced4da;\n"
"}")
        self._body_inspect_button_0.setText("")
        self._body_inspect_button_0.setIconSize(QtCore.QSize(25, 25))
        self._body_inspect_button_0.setObjectName("_body_inspect_button_0")
        self.verticalLayout_5.addWidget(self._body_inspect_button_0)
        self._body_inspect_button_1 = QtWidgets.QPushButton(self.frame_3)
        self._body_inspect_button_1.setMinimumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_1.setMaximumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_1.setStyleSheet("QPushButton{\n"
"    border: 0;\n"
"    background-color: #e9ecef;\n"
"    border-radius: 5px;\n"
"    image: url(src/uparrow.png);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #dee2e6;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #ced4da;\n"
"}")
        self._body_inspect_button_1.setText("")
        self._body_inspect_button_1.setIconSize(QtCore.QSize(25, 25))
        self._body_inspect_button_1.setObjectName("_body_inspect_button_1")
        self.verticalLayout_5.addWidget(self._body_inspect_button_1)
        self._body_inspect_button_2 = QtWidgets.QPushButton(self.frame_3)
        self._body_inspect_button_2.setMinimumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_2.setMaximumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_2.setStyleSheet("QPushButton{\n"
"    border: 0;\n"
"    background-color: #e9ecef;\n"
"    border-radius: 5px;\n"
"    image: url(src/uparrow.png);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #dee2e6;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #ced4da;\n"
"}")
        self._body_inspect_button_2.setText("")
        self._body_inspect_button_2.setIconSize(QtCore.QSize(25, 25))
        self._body_inspect_button_2.setObjectName("_body_inspect_button_2")
        self.verticalLayout_5.addWidget(self._body_inspect_button_2)
        self._body_inspect_button_3 = QtWidgets.QPushButton(self.frame_3)
        self._body_inspect_button_3.setMinimumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_3.setMaximumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_3.setStyleSheet("QPushButton{\n"
"    border: 0;\n"
"    background-color: #e9ecef;\n"
"    border-radius: 5px;\n"
"    image: url(src/uparrow.png);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #dee2e6;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #ced4da;\n"
"}")
        self._body_inspect_button_3.setText("")
        self._body_inspect_button_3.setIconSize(QtCore.QSize(25, 25))
        self._body_inspect_button_3.setObjectName("_body_inspect_button_3")
        self.verticalLayout_5.addWidget(self._body_inspect_button_3)
        self._body_inspect_button_4 = QtWidgets.QPushButton(self.frame_3)
        self._body_inspect_button_4.setMinimumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_4.setMaximumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_4.setStyleSheet("QPushButton{\n"
"    border: 0;\n"
"    background-color: #e9ecef;\n"
"    border-radius: 5px;\n"
"    image: url(src/uparrow.png);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #dee2e6;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #ced4da;\n"
"}")
        self._body_inspect_button_4.setText("")
        self._body_inspect_button_4.setIconSize(QtCore.QSize(25, 25))
        self._body_inspect_button_4.setObjectName("_body_inspect_button_4")
        self.verticalLayout_5.addWidget(self._body_inspect_button_4)
        self._body_inspect_button_5 = QtWidgets.QPushButton(self.frame_3)
        self._body_inspect_button_5.setMinimumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_5.setMaximumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_5.setStyleSheet("QPushButton{\n"
"    border: 0;\n"
"    background-color: #e9ecef;\n"
"    border-radius: 5px;\n"
"    image: url(src/uparrow.png);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #dee2e6;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #ced4da;\n"
"}")
        self._body_inspect_button_5.setText("")
        self._body_inspect_button_5.setIconSize(QtCore.QSize(25, 25))
        self._body_inspect_button_5.setObjectName("_body_inspect_button_5")
        self.verticalLayout_5.addWidget(self._body_inspect_button_5)
        self._body_inspect_button_6 = QtWidgets.QPushButton(self.frame_3)
        self._body_inspect_button_6.setMinimumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_6.setMaximumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_6.setStyleSheet("QPushButton{\n"
"    border: 0;\n"
"    background-color: #e9ecef;\n"
"    border-radius: 5px;\n"
"    image: url(src/uparrow.png);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #dee2e6;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #ced4da;\n"
"}")
        self._body_inspect_button_6.setText("")
        self._body_inspect_button_6.setIconSize(QtCore.QSize(25, 25))
        self._body_inspect_button_6.setObjectName("_body_inspect_button_6")
        self.verticalLayout_5.addWidget(self._body_inspect_button_6)
        self._body_inspect_button_7 = QtWidgets.QPushButton(self.frame_3)
        self._body_inspect_button_7.setMinimumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_7.setMaximumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_7.setStyleSheet("QPushButton{\n"
"    border: 0;\n"
"    background-color: #e9ecef;\n"
"    border-radius: 5px;\n"
"    image: url(src/uparrow.png);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #dee2e6;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #ced4da;\n"
"}")
        self._body_inspect_button_7.setText("")
        self._body_inspect_button_7.setIconSize(QtCore.QSize(25, 25))
        self._body_inspect_button_7.setObjectName("_body_inspect_button_7")
        self.verticalLayout_5.addWidget(self._body_inspect_button_7)
        self._body_inspect_button_8 = QtWidgets.QPushButton(self.frame_3)
        self._body_inspect_button_8.setMinimumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_8.setMaximumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_8.setStyleSheet("QPushButton{\n"
"    border: 0;\n"
"    background-color: #e9ecef;\n"
"    border-radius: 5px;\n"
"    image: url(src/uparrow.png);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #dee2e6;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #ced4da;\n"
"}")
        self._body_inspect_button_8.setText("")
        self._body_inspect_button_8.setIconSize(QtCore.QSize(25, 25))
        self._body_inspect_button_8.setObjectName("_body_inspect_button_8")
        self.verticalLayout_5.addWidget(self._body_inspect_button_8)
        self._body_inspect_button_9 = QtWidgets.QPushButton(self.frame_3)
        self._body_inspect_button_9.setMinimumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_9.setMaximumSize(QtCore.QSize(30, 30))
        self._body_inspect_button_9.setStyleSheet("QPushButton{\n"
"    border: 0;\n"
"    background-color: #e9ecef;\n"
"    border-radius: 5px;\n"
"    image: url(src/uparrow.png);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #dee2e6;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #ced4da;\n"
"}")
        self._body_inspect_button_9.setText("")
        self._body_inspect_button_9.setIconSize(QtCore.QSize(25, 25))
        self._body_inspect_button_9.setObjectName("_body_inspect_button_9")
        self.verticalLayout_5.addWidget(self._body_inspect_button_9)
        spacerItem2 = QtWidgets.QSpacerItem(20, 67, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_4.addWidget(self.frame_3)
        self._body_fixture_table_tableWidget = QtWidgets.QTableWidget(self.page_2)
        self._body_fixture_table_tableWidget.setMaximumSize(QtCore.QSize(185, 16777215))
        self._body_fixture_table_tableWidget.setStyleSheet("/* table header style*/\n"
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
"}\n"
"\n"
"QTableWidget{\n"
" border-radius: 4px;\n"
"}")
        self._body_fixture_table_tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self._body_fixture_table_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self._body_fixture_table_tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self._body_fixture_table_tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self._body_fixture_table_tableWidget.setShowGrid(False)
        self._body_fixture_table_tableWidget.setObjectName("_body_fixture_table_tableWidget")
        self._body_fixture_table_tableWidget.setColumnCount(3)
        self._body_fixture_table_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self._body_fixture_table_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self._body_fixture_table_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self._body_fixture_table_tableWidget.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_4.addWidget(self._body_fixture_table_tableWidget)
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page_5)
        self.horizontalLayout_6.setContentsMargins(0, 4, 0, 4)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self._body_stats_tableWidget = QtWidgets.QTableWidget(self.page_5)
        self._body_stats_tableWidget.setStyleSheet("/* table header style*/\n"
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
        self._body_stats_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self._body_stats_tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self._body_stats_tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self._body_stats_tableWidget.setShowGrid(False)
        self._body_stats_tableWidget.setObjectName("_body_stats_tableWidget")
        self._body_stats_tableWidget.setColumnCount(0)
        self._body_stats_tableWidget.setRowCount(0)
        self.horizontalLayout_6.addWidget(self._body_stats_tableWidget)
        self.frame_4 = QtWidgets.QFrame(self.page_5)
        self.frame_4.setMinimumSize(QtCore.QSize(160, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem3)
        self._body_stats_teams_button = QtWidgets.QPushButton(self.frame_4)
        self._body_stats_teams_button.setMinimumSize(QtCore.QSize(0, 40))
        self._body_stats_teams_button.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._body_stats_teams_button.setObjectName("_body_stats_teams_button")
        self.verticalLayout_4.addWidget(self._body_stats_teams_button)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem4)
        self._body_stats_players_button = QtWidgets.QPushButton(self.frame_4)
        self._body_stats_players_button.setMinimumSize(QtCore.QSize(0, 40))
        self._body_stats_players_button.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._body_stats_players_button.setObjectName("_body_stats_players_button")
        self.verticalLayout_4.addWidget(self._body_stats_players_button)
        spacerItem5 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem5)
        self._body_stats_comboBox = QtWidgets.QComboBox(self.frame_4)
        self._body_stats_comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self._body_stats_comboBox.setStyleSheet("/*52b788 74c69d 40914c*/\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #52b788;\n"
"    selection-color: yellow;\n"
"    color: white;\n"
"    border: 1px solid #828282;\n"
"    border-radius: 6px;\n"
"    font-size: 15px;\n"
"    font-weight: 500px;\n"
"}\n"
"\n"
"QComboBox:hover, QPushButton:hover\n"
"{\n"
"    background-color: #74c69d;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #52b788;\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"    background-color: #52b788;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    selection-background-color: #74c69d;\n"
"    font-weight: 400px;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     color: white;\n"
"     border-bottom-right-radius: 3px;\n"
"     border-bottom-left-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::drop-down::subcontrol{\n"
"    background-color: #74c69d;\n"
"}")
        self._body_stats_comboBox.setObjectName("_body_stats_comboBox")
        self.verticalLayout_4.addWidget(self._body_stats_comboBox)
        spacerItem6 = QtWidgets.QSpacerItem(20, 210, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem6)
        self._body_stats_list_button = QtWidgets.QPushButton(self.frame_4)
        self._body_stats_list_button.setMinimumSize(QtCore.QSize(0, 40))
        self._body_stats_list_button.setMaximumSize(QtCore.QSize(722725, 40))
        self._body_stats_list_button.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._body_stats_list_button.setObjectName("_body_stats_list_button")
        self.verticalLayout_4.addWidget(self._body_stats_list_button)
        self.horizontalLayout_6.addWidget(self.frame_4)
        self.stackedWidget.addWidget(self.page_5)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.page_7)
        self.horizontalLayout_11.setContentsMargins(0, 4, 0, 4)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_11 = QtWidgets.QFrame(self.page_7)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_15.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setMaximumSize(QtCore.QSize(70, 70))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self._team_logo_area = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._team_logo_area.sizePolicy().hasHeightForWidth())
        self._team_logo_area.setSizePolicy(sizePolicy)
        self._team_logo_area.setMinimumSize(QtCore.QSize(68, 68))
        self._team_logo_area.setMaximumSize(QtCore.QSize(68, 68))
        self._team_logo_area.setText("")
        self._team_logo_area.setObjectName("_team_logo_area")
        self.verticalLayout_11.addWidget(self._team_logo_area)
        self.horizontalLayout_7.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setMinimumSize(QtCore.QSize(180, 0))
        self.frame_15.setMaximumSize(QtCore.QSize(180, 16777215))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_12.setContentsMargins(8, -1, 0, -1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self._label_team_name = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self._label_team_name.setFont(font)
        self._label_team_name.setObjectName("_label_team_name")
        self.verticalLayout_12.addWidget(self._label_team_name)
        self._label_team_short_name = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self._label_team_short_name.setFont(font)
        self._label_team_short_name.setObjectName("_label_team_short_name")
        self.verticalLayout_12.addWidget(self._label_team_short_name)
        self.horizontalLayout_10.addWidget(self.frame_15)
        self.horizontalLayout_7.addWidget(self.frame_14)
        self.frame_5 = QtWidgets.QFrame(self.frame_12)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self._body_teams_fixture_button = QtWidgets.QPushButton(self.frame_5)
        self._body_teams_fixture_button.setMaximumSize(QtCore.QSize(150, 33))
        self._body_teams_fixture_button.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 14px;\n"
"  font-weight: 700;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._body_teams_fixture_button.setObjectName("_body_teams_fixture_button")
        self.verticalLayout_6.addWidget(self._body_teams_fixture_button)
        self._body_teams_players_button = QtWidgets.QPushButton(self.frame_5)
        self._body_teams_players_button.setMaximumSize(QtCore.QSize(150, 33))
        self._body_teams_players_button.setStyleSheet("QPushButton{\n"
"  background-color: #52b788;\n"
"  border: 1.5px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
"  color: #fff;\n"
"  font-size: 14px;\n"
"  font-weight: 700;\n"
"  line-height: 20px;\n"
"  padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  background-color: #74c69d;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed {\n"
"  background-color: #40916c;\n"
"}")
        self._body_teams_players_button.setObjectName("_body_teams_players_button")
        self.verticalLayout_6.addWidget(self._body_teams_players_button)
        self.horizontalLayout_7.addWidget(self.frame_5)
        self.frame_16 = QtWidgets.QFrame(self.frame_12)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self._label_team_president = QtWidgets.QLabel(self.frame_16)
        font = QtGui.QFont()
        font.setPointSize(10)
        self._label_team_president.setFont(font)
        self._label_team_president.setObjectName("_label_team_president")
        self.verticalLayout_13.addWidget(self._label_team_president)
        self._label_team_coach = QtWidgets.QLabel(self.frame_16)
        font = QtGui.QFont()
        font.setPointSize(10)
        self._label_team_coach.setFont(font)
        self._label_team_coach.setObjectName("_label_team_coach")
        self.verticalLayout_13.addWidget(self._label_team_coach)
        self.horizontalLayout_7.addWidget(self.frame_16)
        self.verticalLayout_15.addWidget(self.frame_12)
        self.frame_17 = QtWidgets.QFrame(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_14.setContentsMargins(0, 3, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self._body_teams_tableWidget = QtWidgets.QTableWidget(self.frame_17)
        self._body_teams_tableWidget.setStyleSheet("/* table header style*/\n"
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
        self._body_teams_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self._body_teams_tableWidget.setShowGrid(False)
        self._body_teams_tableWidget.setObjectName("_body_teams_tableWidget")
        self._body_teams_tableWidget.setColumnCount(0)
        self._body_teams_tableWidget.setRowCount(0)
        self.verticalLayout_14.addWidget(self._body_teams_tableWidget)
        self.verticalLayout_15.addWidget(self.frame_17)
        self.horizontalLayout_11.addWidget(self.frame_11)
        self.stackedWidget.addWidget(self.page_7)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self._main_menu)
        self.verticalLayout.addWidget(self._body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self._header_menu_button.setText(_translate("MainWindow", "Menu"))
        self._menu_table_button.setText(_translate("MainWindow", "Table"))
        self._menu_statistics_button.setText(_translate("MainWindow", "Statistics"))
        self._menu_restart_button.setText(_translate("MainWindow", "Restart League"))
        self._menu_fixture_button.setText(_translate("MainWindow", "Fixture"))
        self._menu_simulate_button.setText(_translate("MainWindow", "Simulate League"))
        self._menu_play_current_week_button.setText(_translate("MainWindow", "Play Current Week"))
        self._menu_teams_0.setText(_translate("MainWindow", "Table"))
        self._menu_teams_1.setText(_translate("MainWindow", "Table"))
        self._menu_teams_2.setText(_translate("MainWindow", "Table"))
        self._menu_teams_3.setText(_translate("MainWindow", "Table"))
        self._menu_teams_4.setText(_translate("MainWindow", "Table"))
        self._menu_teams_5.setText(_translate("MainWindow", "Table"))
        self._menu_teams_6.setText(_translate("MainWindow", "Table"))
        self._menu_teams_7.setText(_translate("MainWindow", "Table"))
        self._menu_teams_8.setText(_translate("MainWindow", "Table"))
        self._menu_teams_9.setText(_translate("MainWindow", "Table"))
        self._menu_teams_10.setText(_translate("MainWindow", "Table"))
        self._menu_teams_11.setText(_translate("MainWindow", "Table"))
        self._menu_teams_12.setText(_translate("MainWindow", "Table"))
        self._menu_teams_13.setText(_translate("MainWindow", "Table"))
        self._menu_teams_14.setText(_translate("MainWindow", "Table"))
        self._menu_teams_15.setText(_translate("MainWindow", "Table"))
        self._menu_teams_16.setText(_translate("MainWindow", "Table"))
        self._menu_teams_17.setText(_translate("MainWindow", "Table"))
        self._menu_teams_18.setText(_translate("MainWindow", "Table"))
        self._menu_teams_19.setText(_translate("MainWindow", "Table"))
        self._menu_general_button.setText(_translate("MainWindow", "General"))
        self._menu_teams_button.setText(_translate("MainWindow", "Teams"))
        item = self._body_table_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#"))
        item = self._body_table_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Club"))
        item = self._body_table_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Played"))
        item = self._body_table_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Won"))
        item = self._body_table_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Drawn"))
        item = self._body_table_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Lost"))
        item = self._body_table_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "GF"))
        item = self._body_table_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "GA"))
        item = self._body_table_tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "GD"))
        item = self._body_table_tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Points"))
        self._body_previous_button.setText(_translate("MainWindow", "Previous"))
        self._body_current_button.setText(_translate("MainWindow", "Current"))
        self._body_next_button.setText(_translate("MainWindow", "Next"))
        item = self._body_fixture_table_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#"))
        item = self._body_fixture_table_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Club"))
        item = self._body_fixture_table_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "P"))
        self._body_stats_teams_button.setText(_translate("MainWindow", "Team Stats"))
        self._body_stats_players_button.setText(_translate("MainWindow", "Player Stats"))
        self._body_stats_list_button.setText(_translate("MainWindow", "List"))
        self._label_team_name.setText(_translate("MainWindow", ".."))
        self._label_team_short_name.setText(_translate("MainWindow", ".."))
        self._body_teams_fixture_button.setText(_translate("MainWindow", "Fixture"))
        self._body_teams_players_button.setText(_translate("MainWindow", "Players"))
        self._label_team_president.setText(_translate("MainWindow", ".."))
        self._label_team_coach.setText(_translate("MainWindow", ".."))
