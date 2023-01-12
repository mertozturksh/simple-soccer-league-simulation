import random

class LeagueManager:

    def __init__(self, data:dict) -> None:
        self._DATA = data
        self._COMPLETED = False
        self._week = 1
        self._mover_week = 1
        self._fixture = self._executeNewFixture()
        self._played_fixture = {i:[] for i in range(1,39)}


    def playCurrentWeek(self) -> None:
        if not self._COMPLETED:
            current_fixture = self._fixture[self._week]
            for each in current_fixture:
                self._playMatch(home_id=each[1],home_name=each[2],away_id=each[4],away_name=each[5], week=self._week, match_id=each[0])
        self._week += 1
        self._mover_week += 1
        if self._week == 39:
            self._COMPLETED = True
            self._week = 38
            self._mover_week = 38
    
    def sortPlayersByValue(self, players:list, value:str, is_ascending:bool=True) -> list:
        #goal,assist,marketcap,name
        if value == "goal":
            return sorted(players, key= lambda x: (x["goal"],x["assist"],x["marketcap"],x["name"]), reverse=is_ascending)
        elif value == "assist":
            return sorted(players, key= lambda x: (x["assist"],x["goal"],x["marketcap"],x["name"]), reverse=is_ascending)
        elif value == "marketcap":
            return sorted(players, key= lambda x: (x["marketcap"],x["goal"],x["assist"],x["name"]), reverse=is_ascending)
        elif value == "name":
            return sorted(players, key= lambda x: (x["name"],x["goal"],x["assist"],x["marketcap"]), reverse=is_ascending)

    def sortTeamsByValue(self, teams:list, value:str, is_ascending:bool=True) -> list:
        #points,goal_scored,average - match_win,match_lost,match_draw,goal_conceded,matketcap
        if value == "points":
            return sorted(teams, key= lambda x: (x["points"],x["average"],x["goal_scored"]), reverse=is_ascending)
        elif value == "goal_scored":
            return sorted(teams, key= lambda x: (x["goal_scored"],x["points"],x["average"]), reverse=is_ascending)
        elif value == "average":
            return sorted(teams, key= lambda x: (x["average"],x["points"],x["goal_scored"]), reverse=is_ascending)
        ##### EXTRAS
        elif value == "match_win":
            return sorted(teams, key= lambda x: (x["match_win"],x["points"],x["goal_scored"],x["average"]), reverse=is_ascending)
        elif value == "match_lost":
            return sorted(teams, key= lambda x: (x["match_lost"],x["points"],x["goal_scored"],x["average"]), reverse=is_ascending)
        elif value == "match_draw":
            return sorted(teams, key= lambda x: (x["match_draw"],x["points"],x["goal_scored"],x["average"]), reverse=is_ascending)
        elif value == "goal_conceded":
            return sorted(teams, key= lambda x: (x["goal_conceded"],x["points"],x["goal_scored"],x["average"]), reverse=is_ascending)
        elif value == "marketcap":
            return sorted(teams, key= lambda x: (x["marketcap"],x["points"],x["goal_scored"],x["average"]), reverse=is_ascending)

    def filterPlayersByValue(self, players:list, feature:str, value) -> list:
        if feature == "team_id":
            return list(filter(lambda x: x["team_id"] == value, players))
        elif feature == "position":
            return list(filter(lambda x: x["position"] == value, players))
        elif feature == "marketcap":
            return list(filter(lambda x: x["marketcap"] > value, players))

    def getTeamIdByName(self, team_name:str) -> int:
        for each in self._DATA["teams"]:
            if each["team_name"] == team_name:
                return each["team_id"]

    def getTeamFixture(self, team_name, current_week) -> dict:
        fixture = {i:[] for i in range(1,39)}
        if self._played_fixture[current_week] == []:
            for i in range(1,current_week):
                for match in self._played_fixture[i]:
                    if match['home_name'] == team_name or match['away_name'] == team_name:
                        fixture[i] = match
            for i in range(current_week, 39):
                for match in self._fixture[i]:
                    if match[2] == team_name or match[5] == team_name:
                        fixture[i] = match
        else:
            for i in range(1,39):
                for match in self._played_fixture[i]:
                    if match['home_name'] == team_name or match['away_name'] == team_name:
                        fixture[i] = match
        return fixture

    def _playMatch(self, home_id:int, home_name:str, away_id:int, away_name:str, week:int, match_id:int) -> None:
        home_mcap = self._DATA["teams"][home_id]["marketcap"]
        away_mcap = self._DATA["teams"][away_id]["marketcap"]
        home_players = self._DATA["players"][(home_id*11):((home_id+1)*11)]
        away_players = self._DATA["players"][(away_id*11):((away_id+1)*11)]
        home_score = 0
        away_score = 0
        actions = []

        total_attempts = 12
        while total_attempts > 0:
            # home's attack
            if random.choices([home_id, away_id], weights=[home_mcap, away_mcap], k=1)[0] == home_id:
                # 28% goal chance
                if random.choices([1,0], weights=[28,72], k=1)[0]:
                    home_score += 1
                    # solo goal chance 30%
                    if random.choices([1,0], weights=[30,70], k=1)[0]:
                        scorer = self._selectGoalScorer(players=home_players, goal_type="solo")
                        self._scoreAndConcedeGoal(home_id, away_id, scorer["player_id"])
                        actions.append((home_id, home_name, {"goal":(scorer["player_id"], scorer["name"])}))
                    # goal with assist chance %70
                    else:
                        scorer, assister = self._selectGoalScorer(players=home_players, goal_type="duo")
                        self._scoreAndConcedeGoal(home_id, away_id, scorer["player_id"])
                        self._scoreAssist(assister["player_id"])
                        actions.append((home_id, home_name, {"goal":(scorer["player_id"], scorer["name"]), "assist":(assister["player_id"], assister["name"])}))
            # away's attack
            else:
                # 25% goal chance
                if random.choices([1,0], weights=[25,75], k=1)[0]:
                    away_score += 1
                    # solo goal chance %30
                    if random.choices([1,0], weights=[30,70], k=1)[0]:
                        scorer = self._selectGoalScorer(players=away_players, goal_type="solo")
                        self._scoreAndConcedeGoal(away_id, home_id, scorer["player_id"])
                        actions.append((away_id, away_name, {"goal":(scorer["player_id"], scorer["name"])}))
                    # goal with assist chance %70
                    else:
                        scorer, assister = self._selectGoalScorer(players=away_players, goal_type="duo")
                        self._scoreAndConcedeGoal(away_id, home_id, scorer["player_id"])
                        self._scoreAssist(assister["player_id"])
                        actions.append((away_id, away_name, {"goal":(scorer["player_id"], scorer["name"]), "assist":(assister["player_id"], assister["name"])}))
            total_attempts -= 1

        match_actions = {
            "match_id":match_id,
            "week": week,
            "home_id":home_id,
            "home_name":home_name,
            "home_score":home_score,
            "away_id":away_id,
            "away_name":away_name,
            "away_score":away_score,
            "actions":actions
        }
        self._played_fixture[week].append(match_actions)
        self._endOfMatch(home_score, away_score, home_id, away_id)

    def _endOfMatch(self, home_score:int, away_score:int, home_id:int, away_id:int) -> None:
        if home_score > away_score:
            self._DATA["teams"][home_id]["match_played"] += 1
            self._DATA["teams"][home_id]["match_win"] += 1
            self._DATA["teams"][home_id]["points"] += 3
            self._DATA["teams"][away_id]["match_played"] += 1
            self._DATA["teams"][away_id]["match_lost"] += 1
            # self._DATA["teams"][away_id]["points"] += 0
        elif home_score < away_score:
            self._DATA["teams"][home_id]["match_played"] += 1
            self._DATA["teams"][home_id]["match_lost"] += 1
            # self._DATA["teams"][home_id]["points"] += 0
            self._DATA["teams"][away_id]["match_played"] += 1
            self._DATA["teams"][away_id]["match_win"] += 1
            self._DATA["teams"][away_id]["points"] += 3
        else:
            self._DATA["teams"][home_id]["match_played"] += 1
            self._DATA["teams"][home_id]["match_draw"] += 1
            self._DATA["teams"][home_id]["points"] += 1
            self._DATA["teams"][away_id]["match_played"] += 1
            self._DATA["teams"][away_id]["match_draw"] += 1
            self._DATA["teams"][away_id]["points"] += 1

    def _scoreAndConcedeGoal(self, scorer_team_id:int, conceder_team_id:int, player_id:int) -> None:
        self._DATA["teams"][scorer_team_id]["goal_scored"] += 1
        self._DATA["teams"][scorer_team_id]["average"] += 1
        self._DATA["teams"][conceder_team_id]["goal_conceded"] += 1
        self._DATA["teams"][conceder_team_id]["average"] -= 1
        self._DATA["players"][player_id]["goal"] += 1

    def _scoreAssist(self, player_id:int) -> None:
        self._DATA["players"][player_id]["assist"] += 1

    def _selectGoalScorer(self, players:dict, goal_type:str) -> dict:
        pl_dict = {"goalkeeper":[], "defenders":[], "midfielders":[], "strikers":[]}
        for each in players:
            if each["position"] == "Goalkeeper":
                pl_dict["goalkeeper"].append(each)
            elif each["position"] == "Defender":
                pl_dict["defenders"].append(each)
            elif each["position"] == "Midfielder":
                pl_dict["midfielders"].append(each)
            else:
                pl_dict["strikers"].append(each)
        
        if goal_type == "solo":
            # goal chance: goalkeeper 0.05, defender 16.95, midfielder 33 striker 50
            pos = random.choices(["goalkeeper","defenders","midfielders","strikers"], weights=[0.05, 16.95, 33, 50])[0]
            scorer = random.choice(pl_dict[pos])
            return scorer
        else:
            # goal chance: goalkeeper 0.05, defender 16.95, midfielder 33 striker 50
            goal_pos = random.choices(["goalkeeper","defenders","midfielders","strikers"], weights=[0.05, 16.95, 33, 50])[0]
            scorer = random.choice(pl_dict[goal_pos])
            players_cpy = pl_dict.copy()
            players_cpy[goal_pos].remove(scorer)
            # assist chance: goalkeeper 1.5, defender 19.5, midfielder 52 striker 28
            assist_pos = random.choices(["goalkeeper","defenders","midfielders","strikers"], weights=[1.5, 19.5, 52, 28])[0]
            assister = random.choice(players_cpy[assist_pos])
            return scorer, assister

    def _executeNewFixture(self) -> dict:
        base_list = [i for i in range(0,20)]
        random.shuffle(base_list)
        head = base_list[:10]
        tail = base_list[10:]

        match_id_counter = 0
        fixture_dict = {}
        for week in range(1,39):
            current = []
            if week % 2 == 0:
                for each in range(10):
                    team1_id = head[each]
                    team2_id = tail[each]
                    current.append(
                        (
                            match_id_counter,
                            self._DATA["teams"][team1_id]["team_id"], self._DATA["teams"][team1_id]["team_name"], self._DATA["teams"][team1_id]["team_short_name"],
                            self._DATA["teams"][team2_id]["team_id"], self._DATA["teams"][team2_id]["team_name"], self._DATA["teams"][team2_id]["team_short_name"]
                        )
                    )
            else:
                for each in range(10):
                    team1_id = head[each]
                    team2_id = tail[each]
                    current.append(
                        (
                            match_id_counter,
                            self._DATA["teams"][team2_id]["team_id"], self._DATA["teams"][team2_id]["team_name"], self._DATA["teams"][team2_id]["team_short_name"],
                            self._DATA["teams"][team1_id]["team_id"], self._DATA["teams"][team1_id]["team_name"], self._DATA["teams"][team1_id]["team_short_name"]
                        )
                    )
                match_id_counter += 1
            fixture_dict[week] = current
            head.insert(1, tail.pop(0))
            tail.append(head.pop())
        return fixture_dict
