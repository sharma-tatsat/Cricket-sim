import random


def teams():

    ## Team and Player Info

    team = {
        "india": {
            "players": [
                {
                    "position": 1,
                    "first_name": "Abhishek",
                    "last_name": "Sharma",
                    "age": 28,
                    "role": "opening batsman",
                    "style": "Aggresive",
                    "bat": "Left-hand batsman",
                    "bowl": "Right arm offspin",
                    "bat-rating": 7.5,
                    "bowl-rating": 3,
                },
                {
                    "position": 10,
                    "first_name": "jasprit",
                    "last_name": "Bumrah",
                    "age": 31,
                    "role": "Fast Bowler",
                    "style": "Aggresive",
                    "bat": "Right-hand batsman",
                    "bowl": "Right arm fast",
                    "bat-rating": 3,
                    "bowl-rating": 9,
                },
            ]
        },
        "South Africa": {
            "players": [
                {
                    "position": 1,
                    "first_name": "Aiden",
                    "last_name": "Markram",
                    "age": 32,
                    "role": "opening batsman",
                    "style": "Balanced",
                    "bat": "Right-hand batsman",
                    "bowl": "Right arm offspin",
                    "bat-rating": 7.5,
                    "bowl-rating": 5,
                },
                {
                    "position": 9,
                    "first_name": "kagiso",
                    "last_name": "Rabada",
                    "age": 30,
                    "role": "Fast Bowler",
                    "style": "Aggresive",
                    "bat": "right-hand batsman",
                    "bowl": "right arm fast",
                    "bat-rating": 3.5,
                    "bowl-rating": 8,
                },
            ]
        },
    }

    return team


## Match conditions logic


def match(team1, team2):

    print(f"Match {team1} vs {team2}\n")

    print("Toss Time ......\n")

    ## Toss logic

    toss_winner = random.choice([team1, team2])
    toss_decision = random.choice(["bat", "bowl"])

    if toss_winner == team1:  ## Identifying batting team and bowling team

        if toss_decision == "bat":
            game_facets = {"bat": team1, "bowl": team2}
        else:

            game_facets = {"bat": team2, "bowl": team1}
    else:

        if toss_decision == "bat":

            game_facets = {"bat": team2, "bowl": team1}
        else:

            game_facets = {"bat": team1, "bowl": team2}

    print(f"{toss_winner} has won the toss and has elected to {toss_decision}\n")

    return game_facets


def runs():

    run = ["wicket", 0, 1, 2, 3, 4, 6]
    runs_scored = random.choice(run)

    # print(runs_scored)

    return runs_scored


def current_players(overs, runs_scored,wicket_fall,batting_team=[], bowling_team=[]):


    if runs_scored == "wicket":
        wicket_fall += 1

    current_batsman = batting_team[wicket_fall]["first_name"]
    

    if overs % 2 == 0:

        current_bowler = bowling_team[0]["first_name"]

    else:

        current_bowler = bowling_team[1]["first_name"]

    current_player = {
        current_batsman : current_bowler
    }
    
    return current_player


## matchup betweeen teams logic

def matchup(team1, team2):

    teamInfo = teams()

    players_team1 = teamInfo[team1]["players"]
    players_team2 = teamInfo[team2]["players"]

    facets_info = match(team1, team2)

    if team1 in facets_info["bat"]:

        batting_team = team1
        bowling_team = team2

        print(f"Batting XI : {players_team1}\n")
        print(f"Bowling XI : {players_team2}\n")

    else:
        batting_team = team2
        bowling_team = team1

        print(f"Batting XI : {players_team2}\n")
        print(f"Bowling XI : {players_team1}\n")

    overs = 4
    balls = 6
    wicket_fall = 0

    for i in range(overs):
        
        print(f"over : {i+1}")

        for j in range(balls):

            runs_scored = runs()

            print(f"Ball {j+1} : {runs_scored}")
            
            players_current = current_players(i + 1, runs_scored, wicket_fall, players_team1, players_team2)
            print(players_current)


def play():

    matchup("india", "South Africa") 
    
    


play()
