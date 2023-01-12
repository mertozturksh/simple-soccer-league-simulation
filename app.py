import sys, json, os
from PyQt5 import QtWidgets, QtCore, QtGui
from src.main_window import Ui_MainWindow
from src.inspect_window import Ui_Form
from src.manager import LeagueManager

class InspectWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.UI = Ui_Form()
        self.UI.setupUi(self)
        self.setWindowTitle("Super League")
        # self.setWindowIcon(QtGui.QIcon(os.path.join("icons", "logo.jpg")))

        self.UI._tableWidget.verticalHeader().setVisible(False)
        self.UI._tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

    def _setWidgets(self, data:dict, played=True):    
        if played:           
            home_icon = QtGui.QPixmap(os.path.join("icons", "teams", f"team_icon_{data['home_id']}.gif"))
            away_icon = QtGui.QPixmap(os.path.join("icons", "teams", f"team_icon_{data['home_id']}.gif"))

            self.UI._week_area.setText(str(data['week'])+". Week")
            self.UI._home_icon_area.setScaledContents(True)
            self.UI._home_icon_area.setPixmap(home_icon)
            self.UI._home_name_area.setText(data['home_name'])
            self.UI._home_score_area.setText(str(data['home_score']))
            self.UI._away_icon_area.setScaledContents(True)
            self.UI._away_icon_area.setPixmap(away_icon)
            self.UI._away_name_area.setText(data['away_name'])
            self.UI._away_score_area.setText(str(data['away_score']))
            self.UI.label.setText("FT")

            height =  37 * (len(data['actions'])+1)
            self.setMaximumHeight(180 + height)
            self.setMinimumHeight(180 + height)
            self._fill_tableWidget(home_id=data['home_id'], home_name=data['home_name'], away_name=data['away_name'], actions=data['actions'])
            self.UI._body.setEnabled(True)
            self.UI._body.setVisible(True)
        else:
            home_icon = QtGui.QPixmap(os.path.join("icons", "teams", f"team_icon_{data[1]}.gif"))
            away_icon = QtGui.QPixmap(os.path.join("icons", "teams", f"team_icon_{data[4]}.gif"))

            self.UI._home_icon_area.setScaledContents(True)
            self.UI._home_icon_area.setPixmap(home_icon)
            self.UI._home_name_area.setText(data[2])
            self.UI._home_score_area.setText("-")
            self.UI._away_icon_area.setScaledContents(True)
            self.UI._away_icon_area.setPixmap(away_icon)
            self.UI._away_name_area.setText(data[5])
            self.UI._away_score_area.setText("-")
            self.UI.label.setText("-")
            
            self.UI._body.setEnabled(False)
            self.UI._body.setVisible(False)
            self.setMaximumHeight(180)
            self.setMinimumHeight(180)

    def _set_tableWidget_column_sizes(self):
        header = self.UI._tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        header.resizeSection(1, 50)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

    def _fill_tableWidget(self, home_id:int, home_name:str, away_name:str, actions:list):
        self.UI._tableWidget.setColumnCount(3)   # week,home,home_score,--,away_score,away
        self._set_tableWidget_column_sizes()
        self.UI._tableWidget.setHorizontalHeaderLabels([home_name, "", away_name])
        self.UI._tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.UI._tableWidget.setRowCount(len(actions))
        home_score, away_score = 0,0
        for i,each in enumerate(actions):
            if each[0] == home_id:      # home's goal
                item = QtWidgets.QTableWidgetItem(each[2]['goal'][1])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._tableWidget.setItem(i, 0, item)
                home_score += 1
                item = QtWidgets.QTableWidgetItem(f"{home_score} - {away_score}")
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._tableWidget.setItem(i, 1, item)
                item = QtWidgets.QTableWidgetItem("")
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._tableWidget.setItem(i, 2, item)

            else:   # away's goal
                item = QtWidgets.QTableWidgetItem("")
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._tableWidget.setItem(i, 0, item)
                away_score += 1
                item = QtWidgets.QTableWidgetItem(f"{home_score} - {away_score}")
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._tableWidget.setItem(i, 1, item)
                item = QtWidgets.QTableWidgetItem(each[2]['goal'][1])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._tableWidget.setItem(i, 2, item)
            for j in range(3):
                if i % 2 == 0:
                    self.UI._tableWidget.item(i,j).setBackground(QtGui.QColor(233, 236, 239))
                else:
                    self.UI._tableWidget.item(i,j).setBackground(QtGui.QColor(248, 249, 250))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.LeagueManager = LeagueManager(self._init_data())
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        self.setWindowTitle("Super League")
        # self.setWindowIcon(QtGui.QIcon(os.path.join("icons", "logo.jpg")))
        self.inspectWindow = InspectWindow()

        self.UI._header_menu_button.clicked.connect(lambda: self._slide_menu(self.UI._left_menu,225,0))

        self.UI._menu_table_button.clicked.connect(lambda: self.UI.stackedWidget.setCurrentIndex(0))
        self.UI._menu_fixture_button.clicked.connect(lambda: self.UI.stackedWidget.setCurrentIndex(1))
        self.UI._menu_statistics_button.clicked.connect(lambda: self.UI.stackedWidget.setCurrentIndex(2))
        self.UI._menu_general_button.clicked.connect(lambda: self.UI.stackedWidget_2.setCurrentIndex(0))
        self.UI._menu_teams_button.clicked.connect(lambda: self.UI.stackedWidget_2.setCurrentIndex(1))
        self.UI._menu_play_current_week_button.clicked.connect(self._run_playMatch)
        self.UI._menu_simulate_button.clicked.connect(self._run_simulateLeague)
        self.UI._menu_restart_button.clicked.connect(self._init_start_league)

        self.UI._body_previous_button.clicked.connect(lambda: self._set_previous_fixture(self.LeagueManager._mover_week))
        self.UI._body_current_button.clicked.connect(self._set_current_fixture)
        self.UI._body_next_button.clicked.connect(lambda: self._set_next_fixture(self.LeagueManager._mover_week))
        self.UI._body_stats_players_button.clicked.connect(lambda: self._set_third_page_view(kind="players",value="Goals"))
        self.UI._body_stats_teams_button.clicked.connect(lambda: self._set_third_page_view(kind="teams",value="Points"))
        self.UI._body_stats_list_button.clicked.connect(lambda: self._fill_third_page_tableWidget(kind=self.UI._body_stats_comboBox.count(), value=self.UI._body_stats_comboBox.currentText()))
        self.UI._body_teams_fixture_button.clicked.connect(lambda: self._fill_fourth_page_tableWidget(team_id = self.LeagueManager.getTeamIdByName(self.UI._label_team_name.text()),get_fixture=True))
        self.UI._body_teams_players_button.clicked.connect(lambda: self._fill_fourth_page_tableWidget(team_id = self.LeagueManager.getTeamIdByName(self.UI._label_team_name.text()),get_fixture=False))
        self._set_inspect_match_buttons_signals()
        self._set_teams_buttons_signals()

        self.UI._body_table_tableWidget.verticalHeader().setVisible(False)
        self.UI._body_fixture_tableWidget.verticalHeader().setVisible(False)
        self.UI._body_fixture_table_tableWidget.verticalHeader().setVisible(False)
        self.UI._body_stats_tableWidget.verticalHeader().setVisible(False)
        self.UI._body_teams_tableWidget.verticalHeader().setVisible(False)
        self.UI._body_table_tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.UI._body_fixture_tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.UI._body_fixture_table_tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.UI._body_stats_tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.UI._body_teams_tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self._fill_first_page_tableWidget()    
        self._fill_second_page_first_tableWidget()
        self._fill_second_page_second_tableWidget()
        self._fill_third_page_tableWidget()
        self._fill_third_page_comboBox()
        self._fill_fourth_page_tableWidget()

        self._set_inspect_match_buttons()
        self._set_teams_buttons()

        self._set_first_page_tableWidget_column_sizes()
        self._set_second_page_first_tableWidget_column_sizes()
        self._set_second_page_second_tableWidget_column_sizes()
        self._set_third_page_tableWidget_column_sizes()
        self._set_fourth_page_tableWidget_column_sizes()

    def _run_simulateLeague(self):
        if not self.LeagueManager._COMPLETED:
            self._run_playMatch()
            QtCore.QTimer.singleShot(250, lambda: self._run_simulateLeague())

    def _run_playMatch(self):
        self.LeagueManager.playCurrentWeek()
        self.LeagueManager._mover_week = self.LeagueManager._week
        self._fill_first_page_tableWidget()
        self._fill_second_page_first_tableWidget(week=self.LeagueManager._week)
        self._fill_second_page_second_tableWidget()
        self._fill_third_page_tableWidget(kind=8,value="Points")
        self._fill_fourth_page_tableWidget()

    # menu slide animation
    def _slide_menu(self, menu, _max, _min):
        width = menu.width()
        newWidth = _max if width == _min else _min
        self._animation = QtCore.QPropertyAnimation(menu, b"minimumWidth")
        self._animation.setDuration(400)
        self._animation.setStartValue(width)
        self._animation.setEndValue(newWidth)
        self._animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self._animation.start()

    # browse through fixtures
    def _set_previous_fixture(self, current_week):
        if current_week == 1:
            pass
        else:
            self.LeagueManager._mover_week -= 1
            self._fill_second_page_first_tableWidget(self.LeagueManager._mover_week)

    def _set_current_fixture(self):
        self.LeagueManager._mover_week = self.LeagueManager._week
        self._fill_second_page_first_tableWidget(self.LeagueManager._week)

    def _set_next_fixture(self, current_week):
        if current_week == 38:
            pass
        else:
            self.LeagueManager._mover_week += 1
            self._fill_second_page_first_tableWidget(self.LeagueManager._mover_week)

    # setting some buttons and signals
    def _set_inspect_match_buttons(self):
        for i in range(0,10):
            button = self.UI.frame_3.findChild(QtWidgets.QPushButton, f"_body_inspect_button_{i}")
            button.setIcon(QtGui.QIcon(os.path.join("icons", "up-arrow.png")))

    def _set_inspect_match_buttons_signals(self):
        self.UI._body_inspect_button_0.clicked.connect(lambda: self.inspectMatch(0))
        self.UI._body_inspect_button_1.clicked.connect(lambda: self.inspectMatch(1))
        self.UI._body_inspect_button_2.clicked.connect(lambda: self.inspectMatch(2))
        self.UI._body_inspect_button_3.clicked.connect(lambda: self.inspectMatch(3))
        self.UI._body_inspect_button_4.clicked.connect(lambda: self.inspectMatch(4))
        self.UI._body_inspect_button_5.clicked.connect(lambda: self.inspectMatch(5))
        self.UI._body_inspect_button_6.clicked.connect(lambda: self.inspectMatch(6))
        self.UI._body_inspect_button_7.clicked.connect(lambda: self.inspectMatch(7))
        self.UI._body_inspect_button_8.clicked.connect(lambda: self.inspectMatch(8))
        self.UI._body_inspect_button_9.clicked.connect(lambda: self.inspectMatch(9))

    def _set_teams_buttons(self):
        for i in range(20):
            button = self.UI.scrollAreaWidgetContents.findChild(QtWidgets.QPushButton, f"_menu_teams_{i}")
            button.setIcon(QtGui.QIcon(os.path.join("icons", "teams", f"team_icon_{i}.gif")))
            button.setIconSize(QtCore.QSize(25,25))
            button.setText(" "+self.LeagueManager._DATA["teams"][i]["team_name"])
            button.setLayoutDirection(QtCore.Qt.LeftToRight)

    def _set_teams_buttons_signals(self):
        self.UI._menu_teams_0.clicked.connect(lambda: self._set_fourth_page_view(team_id=0))
        self.UI._menu_teams_1.clicked.connect(lambda: self._set_fourth_page_view(team_id=1))
        self.UI._menu_teams_2.clicked.connect(lambda: self._set_fourth_page_view(team_id=2))
        self.UI._menu_teams_3.clicked.connect(lambda: self._set_fourth_page_view(team_id=3))
        self.UI._menu_teams_4.clicked.connect(lambda: self._set_fourth_page_view(team_id=4))
        self.UI._menu_teams_5.clicked.connect(lambda: self._set_fourth_page_view(team_id=5))
        self.UI._menu_teams_6.clicked.connect(lambda: self._set_fourth_page_view(team_id=6))
        self.UI._menu_teams_7.clicked.connect(lambda: self._set_fourth_page_view(team_id=7))
        self.UI._menu_teams_8.clicked.connect(lambda: self._set_fourth_page_view(team_id=8))
        self.UI._menu_teams_9.clicked.connect(lambda: self._set_fourth_page_view(team_id=9))
        self.UI._menu_teams_10.clicked.connect(lambda: self._set_fourth_page_view(team_id=10))
        self.UI._menu_teams_11.clicked.connect(lambda: self._set_fourth_page_view(team_id=11))
        self.UI._menu_teams_12.clicked.connect(lambda: self._set_fourth_page_view(team_id=12))
        self.UI._menu_teams_13.clicked.connect(lambda: self._set_fourth_page_view(team_id=13))
        self.UI._menu_teams_14.clicked.connect(lambda: self._set_fourth_page_view(team_id=14))
        self.UI._menu_teams_15.clicked.connect(lambda: self._set_fourth_page_view(team_id=15))
        self.UI._menu_teams_16.clicked.connect(lambda: self._set_fourth_page_view(team_id=16))
        self.UI._menu_teams_17.clicked.connect(lambda: self._set_fourth_page_view(team_id=17))
        self.UI._menu_teams_18.clicked.connect(lambda: self._set_fourth_page_view(team_id=18))
        self.UI._menu_teams_19.clicked.connect(lambda: self._set_fourth_page_view(team_id=19))

    def inspectMatch(self, index):
        if self.LeagueManager._played_fixture[self.LeagueManager._mover_week] != []:
            self.inspectWindow._setWidgets(data=self.LeagueManager._played_fixture[self.LeagueManager._mover_week][index])
            self.inspectWindow.show()
        else:
            self.inspectWindow._setWidgets(self.LeagueManager._fixture[self.LeagueManager._mover_week][index], played=False)
            self.inspectWindow.UI._week_area.setText(str(self.LeagueManager._mover_week)+". Week")
            self.inspectWindow.show()

    # set page view for button signals    
    def _set_third_page_view(self, kind, value):
        col_size = 8 if kind == "teams" else 3
        self._fill_third_page_comboBox(kind=kind)
        self._fill_third_page_tableWidget(kind=col_size,value=value)    

    def _set_fourth_page_view(self, team_id):
        self.UI.stackedWidget.setCurrentIndex(3)
        self._fill_fourth_page_tableWidget(team_id=team_id)

    # setting tableWidget column widths
    def _set_first_page_tableWidget_column_sizes(self):
        header = self.UI._body_table_tableWidget.horizontalHeader()
        # header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)         
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        header.resizeSection(1, 165)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(9, QtWidgets.QHeaderView.Stretch)

    def _set_second_page_first_tableWidget_column_sizes(self, col_size=5):
        header = self.UI._body_fixture_tableWidget.horizontalHeader()
        if col_size == 5:
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(0, 15)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(2, 20)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(4, 15)
        else:
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(0, 15)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(2, 15)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(3, 15)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(4, 15)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(6, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(6, 15)
            
    def _set_second_page_second_tableWidget_column_sizes(self):
        header = self.UI._body_fixture_table_tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        header.resizeSection(0, 10)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        header.resizeSection(2, 15)

    def _set_third_page_tableWidget_column_sizes(self, col_size=4):
        header = self.UI._body_stats_tableWidget.horizontalHeader()
        if col_size == 4:   # teams
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(0, 80)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(1, 50)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(3, 180)
        else:   # players
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(0, 30)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(1, 80)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(2, 30)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(4, 60)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(5, 100)

    def _set_fourth_page_tableWidget_column_sizes(self, col_size=7):
        header = self.UI._body_teams_tableWidget.horizontalHeader()
        if col_size == 7:   # players
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(0, 30)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(2, 60)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(4, 120)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(5, 75)
            header.setSectionResizeMode(6, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(6, 75)
        else:   # fixture
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(0, 30)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(1, 30)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(3, 50)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(4, 50)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(5, 50)
            header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(7, QtWidgets.QHeaderView.Fixed)
            header.resizeSection(7, 30)


    # filling tableWidget's
    def _fill_first_page_tableWidget(self):
        data = self.LeagueManager.sortTeamsByValue(self.LeagueManager._DATA["teams"],value="points")
        self.UI._body_table_tableWidget.setRowCount(20)
        for i,each in enumerate(data):
            item = QtWidgets.QTableWidgetItem(str(i+1))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.UI._body_table_tableWidget.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem("  "+str(each["team_name"]))
            item.setTextAlignment(QtCore.Qt.AlignVCenter)
            
            item.setIcon(QtGui.QIcon(os.path.join("icons", "teams", f"team_icon_{each['team_id']}.gif")))
            self.UI._body_table_tableWidget.setItem(i, 1, item)
            item = QtWidgets.QTableWidgetItem(str(each["match_played"]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.UI._body_table_tableWidget.setItem(i, 2, item)
            item = QtWidgets.QTableWidgetItem(str(each["match_win"]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.UI._body_table_tableWidget.setItem(i, 3, item)
            item = QtWidgets.QTableWidgetItem(str(each["match_draw"]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.UI._body_table_tableWidget.setItem(i, 4, item)
            item = QtWidgets.QTableWidgetItem(str(each["match_lost"]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.UI._body_table_tableWidget.setItem(i, 5, item)
            item = QtWidgets.QTableWidgetItem(str(each["goal_scored"]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.UI._body_table_tableWidget.setItem(i, 6, item)
            item = QtWidgets.QTableWidgetItem(str(each["goal_conceded"]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.UI._body_table_tableWidget.setItem(i, 7, item)
            item = QtWidgets.QTableWidgetItem(str(each["average"]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.UI._body_table_tableWidget.setItem(i, 8, item)
            item = QtWidgets.QTableWidgetItem(str(each["points"]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.UI._body_table_tableWidget.setItem(i, 9, item)
            for j in range(10):
                if i % 2 == 0:
                    self.UI._body_table_tableWidget.item(i,j).setBackground(QtGui.QColor(233, 236, 239))
                else:
                    self.UI._body_table_tableWidget.item(i,j).setBackground(QtGui.QColor(248, 249, 250))

    def _fill_second_page_first_tableWidget(self, week=1):
        # self.UI._body_fixture_tableWidget.setRowCount(0)
        if self.LeagueManager._played_fixture[week] == []:
            data = self.LeagueManager._fixture[week]
            self.UI._body_fixture_tableWidget.setColumnCount(5)
            self.UI._body_fixture_tableWidget.setHorizontalHeaderLabels(["","Home", str(week), "Away",""])
            self.UI._body_fixture_tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
            self.UI._body_fixture_tableWidget.setRowCount(10)
            self._set_second_page_first_tableWidget_column_sizes(5)
            for i,each in enumerate(data):
                item = QtWidgets.QTableWidgetItem(" ")
                item.setTextAlignment(QtCore.Qt.AlignLeft)
                item.setIcon(QtGui.QIcon(os.path.join("icons", "teams", f"team_icon_{each[1]}.gif")))
                self.UI._body_fixture_tableWidget.setItem(i, 0, item)
                item = QtWidgets.QTableWidgetItem(each[2])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_fixture_tableWidget.setItem(i, 1, item)
                item = QtWidgets.QTableWidgetItem("   --   ")
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_fixture_tableWidget.setItem(i, 2, item)
                item = QtWidgets.QTableWidgetItem(each[5])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_fixture_tableWidget.setItem(i, 3, item)
                item = QtWidgets.QTableWidgetItem("")
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setIcon(QtGui.QIcon(os.path.join("icons", "teams", f"team_icon_{each[4]}.gif")))
                self.UI._body_fixture_tableWidget.setItem(i, 4, item)
                for j in range(5):
                    if i % 2 == 0:
                        self.UI._body_fixture_tableWidget.item(i,j).setBackground(QtGui.QColor(233, 236, 239))
                    else:
                        self.UI._body_fixture_tableWidget.item(i,j).setBackground(QtGui.QColor(248, 249, 250))
        else:
            data = self.LeagueManager._played_fixture[week]
            self.UI._body_fixture_tableWidget.setColumnCount(7)
            self.UI._body_fixture_tableWidget.setHorizontalHeaderLabels(["","Home", "", str(week), "", "Away",""])
            self.UI._body_fixture_tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
            self.UI._body_fixture_tableWidget.setRowCount(10)
            self._set_second_page_first_tableWidget_column_sizes(7)
            for i,each in enumerate(data):
                item = QtWidgets.QTableWidgetItem(" ")
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setIcon(QtGui.QIcon(os.path.join("icons", "teams", f"team_icon_{each['home_id']}.gif")))
                self.UI._body_fixture_tableWidget.setItem(i, 0, item)
                item = QtWidgets.QTableWidgetItem(each["home_name"])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_fixture_tableWidget.setItem(i, 1, item)
                item = QtWidgets.QTableWidgetItem(str(each["home_score"]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_fixture_tableWidget.setItem(i, 2, item)
                item = QtWidgets.QTableWidgetItem(" -- ")
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_fixture_tableWidget.setItem(i, 3, item)
                item = QtWidgets.QTableWidgetItem(str(each["away_score"]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_fixture_tableWidget.setItem(i, 4, item)
                item = QtWidgets.QTableWidgetItem(each["away_name"])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_fixture_tableWidget.setItem(i, 5, item)
                item = QtWidgets.QTableWidgetItem(" ")
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setIcon(QtGui.QIcon(os.path.join("icons", "teams", f"team_icon_{each['away_id']}.gif")))
                self.UI._body_fixture_tableWidget.setItem(i, 6, item)
                for j in range(7):
                    if i % 2 == 0:
                        self.UI._body_fixture_tableWidget.item(i,j).setBackground(QtGui.QColor(233, 236, 239))
                    else:
                        self.UI._body_fixture_tableWidget.item(i,j).setBackground(QtGui.QColor(248, 249, 250))

    def _fill_second_page_second_tableWidget(self):
        data = self.LeagueManager.sortTeamsByValue(self.LeagueManager._DATA["teams"],value="points")
        self.UI._body_fixture_table_tableWidget.setRowCount(20)
        for i,each in enumerate(data):
            item = QtWidgets.QTableWidgetItem(str(i+1))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.UI._body_fixture_table_tableWidget.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem(str(each["team_short_name"]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setIcon(QtGui.QIcon(os.path.join("icons", "teams", f"team_icon_{each['team_id']}.gif")))
            self.UI._body_fixture_table_tableWidget.setItem(i, 1, item)
            item = QtWidgets.QTableWidgetItem(str(each["points"]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.UI._body_fixture_table_tableWidget.setItem(i, 2, item)
            for j in range(3):
                if i % 2 == 0:
                    self.UI._body_fixture_table_tableWidget.item(i,j).setBackground(QtGui.QColor(233, 236, 239))
                else:
                    self.UI._body_fixture_table_tableWidget.item(i,j).setBackground(QtGui.QColor(248, 249, 250))

    def _fill_third_page_tableWidget(self, value="Points", kind=8):
        if kind == 8:
            text = "points" if value == "Points" else "goal_scored" if value == "Goals For" else "average" if value == "Goal Difference"\
                else "goal_conceded" if value == "Goals Against" else "match_win" if value == "Matches Won" else "match_lost"\
                if value == "Matches Lost" else "match_draw" if value == "Matches Drawn" else "marketcap"
            data = self.LeagueManager.sortTeamsByValue(self.LeagueManager._DATA["teams"],value=text)
            self.UI._body_stats_tableWidget.setColumnCount(4)
            self.UI._body_stats_tableWidget.setHorizontalHeaderLabels(["#","","Club",value])
            self.UI._body_stats_tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
            self.UI._body_stats_tableWidget.setRowCount(20)
            self._set_third_page_tableWidget_column_sizes(4)
            for i,each in enumerate(data):
                item = QtWidgets.QTableWidgetItem(str(i+1)+"  ")
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_stats_tableWidget.setItem(i, 0, item)
                item = QtWidgets.QTableWidgetItem("")
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setIcon(QtGui.QIcon(os.path.join("icons", "teams", f"team_icon_{each['team_id']}.gif")))
                self.UI._body_stats_tableWidget.setItem(i, 1, item)
                item = QtWidgets.QTableWidgetItem(str(each["team_name"]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_stats_tableWidget.setItem(i, 2, item)
                item = QtWidgets.QTableWidgetItem(str(each[text]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_stats_tableWidget.setItem(i, 3, item)
                for j in range(4):
                    if i % 2 == 0:
                        self.UI._body_stats_tableWidget.item(i,j).setBackground(QtGui.QColor(233, 236, 239))
                    else:
                        self.UI._body_stats_tableWidget.item(i,j).setBackground(QtGui.QColor(248, 249, 250))
        else:   #players    # goal assist marketcap
            text = "goal" if value == "Goals" else "assist" if value == "Assists" else "marketcap"
            data = self.LeagueManager.sortPlayersByValue(self.LeagueManager._DATA["players"], value=text, is_ascending=True)
            self.UI._body_stats_tableWidget.setColumnCount(6)
            self.UI._body_stats_tableWidget.setHorizontalHeaderLabels(["#","Club","No","Name","Position",value])
            self.UI._body_stats_tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
            self.UI._body_stats_tableWidget.setRowCount(220)
            self._set_third_page_tableWidget_column_sizes(6)
            for i,each in enumerate(data):
                item = QtWidgets.QTableWidgetItem(str(i+1))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_stats_tableWidget.setItem(i, 0, item)
                item = QtWidgets.QTableWidgetItem(each["team_short_name"])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setIcon(QtGui.QIcon(os.path.join("icons", "teams", f"team_icon_{each['team_id']}.gif")))
                self.UI._body_stats_tableWidget.setItem(i, 1, item)
                item = QtWidgets.QTableWidgetItem(str(each["player_no"]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_stats_tableWidget.setItem(i, 2, item)
                item = QtWidgets.QTableWidgetItem(each["name"])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_stats_tableWidget.setItem(i, 3, item)
                item = QtWidgets.QTableWidgetItem(each["spe_pos"])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_stats_tableWidget.setItem(i, 4, item)
                item = QtWidgets.QTableWidgetItem(str(each[text]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_stats_tableWidget.setItem(i, 5, item)
                for j in range(6):
                    if i % 2 == 0:
                        self.UI._body_stats_tableWidget.item(i,j).setBackground(QtGui.QColor(233, 236, 239))
                    else:
                        self.UI._body_stats_tableWidget.item(i,j).setBackground(QtGui.QColor(248, 249, 250))

    def _fill_fourth_page_tableWidget(self, team_id=0, get_fixture=False):
        if get_fixture: # fixture view
            data = self.LeagueManager.getTeamFixture(team_name=self.UI._label_team_name.text(), current_week=self.LeagueManager._week)
            self.UI._body_teams_tableWidget.setColumnCount(8)   # week,home,home_score,--,away_score,away
            self._set_fourth_page_tableWidget_column_sizes(8)
            self.UI._body_teams_tableWidget.setHorizontalHeaderLabels(["#","","Home"," "," "," ","Away",""])
            self.UI._body_teams_tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
            self.UI._body_teams_tableWidget.setRowCount(38)
            for i,each in enumerate(data.values()):
                if type(each) == dict:  # played fixture
                    item = QtWidgets.QTableWidgetItem(str(i+1)+" ")
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.UI._body_teams_tableWidget.setItem(i, 0, item)
                    item = QtWidgets.QTableWidgetItem("")
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setIcon(QtGui.QIcon(os.path.join("icons", "teams", f"team_icon_{each['home_id']}.gif")))
                    self.UI._body_teams_tableWidget.setItem(i, 1, item)
                    item = QtWidgets.QTableWidgetItem(each["home_name"])
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.UI._body_teams_tableWidget.setItem(i, 2, item)
                    item = QtWidgets.QTableWidgetItem(str(each["home_score"]))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.UI._body_teams_tableWidget.setItem(i, 3, item)
                    # result text and color
                    if each['home_id'] == team_id:
                        if each['home_score'] > each['away_score']:
                            item = QtWidgets.QTableWidgetItem(" W ")
                            item.setBackground(QtGui.QColor(146, 230, 167))
                        elif each['home_score'] == each['away_score']:
                            item = QtWidgets.QTableWidgetItem(" D ")
                            item.setBackground(QtGui.QColor(255, 229, 102))
                        else:
                            item = QtWidgets.QTableWidgetItem(" L ")
                            item.setBackground(QtGui.QColor(255, 87, 20))
                    else:
                        if each['away_score'] > each['home_score']:
                            item = QtWidgets.QTableWidgetItem(" W ")
                            item.setBackground(QtGui.QColor(146, 230, 167))
                        elif each['away_score'] == each['home_score']:
                            item = QtWidgets.QTableWidgetItem(" D ")
                            item.setBackground(QtGui.QColor(255, 229, 102))
                        else:
                            item = QtWidgets.QTableWidgetItem(" L ")
                            item.setBackground(QtGui.QColor(255, 87, 20))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.UI._body_teams_tableWidget.setItem(i, 4, item)

                    item = QtWidgets.QTableWidgetItem(str(each["away_score"]))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.UI._body_teams_tableWidget.setItem(i, 5, item)
                    item = QtWidgets.QTableWidgetItem(each["away_name"])
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.UI._body_teams_tableWidget.setItem(i, 6, item)
                    item = QtWidgets.QTableWidgetItem("")
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setIcon(QtGui.QIcon(os.path.join("icons", "teams", f"team_icon_{each['away_id']}.gif")))
                    self.UI._body_teams_tableWidget.setItem(i, 7, item)
                else:   # fixture
                    item = QtWidgets.QTableWidgetItem(str(i+1)+" ")
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.UI._body_teams_tableWidget.setItem(i, 0, item)
                    item = QtWidgets.QTableWidgetItem("")
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setIcon(QtGui.QIcon(os.path.join("icons", "teams", f"team_icon_{each[1]}.gif")))
                    self.UI._body_teams_tableWidget.setItem(i, 1, item)
                    item = QtWidgets.QTableWidgetItem(each[2])
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.UI._body_teams_tableWidget.setItem(i, 2, item)
                    item = QtWidgets.QTableWidgetItem(" ")
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.UI._body_teams_tableWidget.setItem(i, 3, item)
                    item = QtWidgets.QTableWidgetItem("  --  ")
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.UI._body_teams_tableWidget.setItem(i, 4, item)
                    if i % 2 == 0:
                        item.setBackground(QtGui.QColor(233, 236, 239))
                    else:
                        item.setBackground(QtGui.QColor(248, 249, 250))
                    item = QtWidgets.QTableWidgetItem(" ")
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.UI._body_teams_tableWidget.setItem(i, 5, item)
                    item = QtWidgets.QTableWidgetItem(each[5])
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.UI._body_teams_tableWidget.setItem(i, 6, item)
                    item = QtWidgets.QTableWidgetItem("")
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setIcon(QtGui.QIcon(os.path.join("icons", "teams", f"team_icon_{each[4]}.gif")))
                    self.UI._body_teams_tableWidget.setItem(i, 7, item)
                for j in [0,1,2,3,5,6,7]:
                    if i % 2 == 0:
                        self.UI._body_teams_tableWidget.item(i,j).setBackground(QtGui.QColor(233, 236, 239))
                    else:
                        self.UI._body_teams_tableWidget.item(i,j).setBackground(QtGui.QColor(248, 249, 250))
        else:   # players view
            image = QtGui.QPixmap(os.path.join("icons", "teams", f"team_icon_{team_id}.gif"))
            self.UI._team_logo_area.setScaledContents(True)
            self.UI._team_logo_area.setPixmap(image)
            self.UI._label_team_name.setText(self.LeagueManager._DATA["teams"][team_id]["team_name"])
            self.UI._label_team_short_name.setText(self.LeagueManager._DATA["teams"][team_id]["team_short_name"])
            self.UI._label_team_president.setText("President :   "+self.LeagueManager._DATA["teams"][team_id]["president"]+"  ")
            self.UI._label_team_coach.setText("Coach      :   "+self.LeagueManager._DATA["teams"][team_id]["coach"]+"  ")
            data = self.LeagueManager.filterPlayersByValue(players=self.LeagueManager._DATA["players"], feature="team_id", value=team_id)
            self.UI._body_teams_tableWidget.setColumnCount(7)
            self._set_fourth_page_tableWidget_column_sizes(7)
            self.UI._body_teams_tableWidget.setHorizontalHeaderLabels(["No","Name","Position","Country","Marketcap","Goal","Assist"])
            self.UI._body_teams_tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
            self.UI._body_teams_tableWidget.setRowCount(11)
            for i,each in enumerate(data):
                item = QtWidgets.QTableWidgetItem(str(each["player_no"]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_teams_tableWidget.setItem(i, 0, item)
                item = QtWidgets.QTableWidgetItem(each["name"])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_teams_tableWidget.setItem(i, 1, item)
                item = QtWidgets.QTableWidgetItem(each["spe_pos"])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_teams_tableWidget.setItem(i, 2, item)
                item = QtWidgets.QTableWidgetItem(each["country"])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_teams_tableWidget.setItem(i, 3, item)
                item = QtWidgets.QTableWidgetItem(str(each["marketcap"])+"M€")
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_teams_tableWidget.setItem(i, 4, item)
                item = QtWidgets.QTableWidgetItem(str(each["goal"]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_teams_tableWidget.setItem(i, 5, item)
                item = QtWidgets.QTableWidgetItem(str(each["assist"]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UI._body_teams_tableWidget.setItem(i, 6, item)
                for j in range(7):
                    if i % 2 == 0:
                        self.UI._body_teams_tableWidget.item(i,j).setBackground(QtGui.QColor(233, 236, 239))
                    else:
                        self.UI._body_teams_tableWidget.item(i,j).setBackground(QtGui.QColor(248, 249, 250))

    # filling comboBox
    def _fill_third_page_comboBox(self, kind="teams"):
        self.UI._body_stats_comboBox.clear()
        if kind == "players":
            self.UI._body_stats_comboBox.addItems(["Goals", "Assists", "Marketcap"])
        else:   # teams
            self.UI._body_stats_comboBox.addItems(["Points", "Goals For", "Goal Difference", "Goals Against", "Matches Won", "Matches Lost", "Matches Drawn", "Marketcap"])

    # start or restart self.LeagueManager object
    def _init_start_league(self):
        self.LeagueManager = LeagueManager(self._init_data())
        self._fill_first_page_tableWidget()
        self._fill_second_page_first_tableWidget(self.LeagueManager._week)
        self._fill_second_page_second_tableWidget()
        self._fill_third_page_tableWidget(kind=8,value="Points")
        self._fill_fourth_page_tableWidget()

    # load and init .json file
    def _init_data(self):
        with open(os.path.join("src", "data.json"), "r", encoding="utf-8") as f:
            data = json.load(f)

            for each in data["teams"]:
                each["goal_scored"] = 0; each["goal_conceded"] = 0; each["average"] = 0; each["match_played"] = 0
                each["match_win"] = 0; each["match_draw"] = 0; each["match_lost"] = 0; each["points"] = 0

            for each in data["players"]:
                each["goal"] = 0; each["assist"] = 0

            return data


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("closing...")
