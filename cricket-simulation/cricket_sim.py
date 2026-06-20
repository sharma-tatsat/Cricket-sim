import random


def teams():

    ## Team and Player Info

    team = {
        "india": {
            "players": [
                {
                    "position": 1,
                    "first name": "Abhishek",
                    "last name": "Sharma",
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
                    "first name": "jasprit",
                    "last name": "Bumrah",
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
                    "first name": "Aiden",
                    "last name": "Markram",
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
                    "first name": "kagiso",
                    "last name": "Rabada",
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

    if toss_winner == team1:                                  ## Identifying batting team and bowling team 

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


## matchup betweeen teams logic


def matchup(team1, team2):

    runs = ["wicket", 0, 1, 2, 3, 4, 6]

    teamInfo = teams()

    players_team1 = teamInfo[team1]["players"]
    players_team2 = teamInfo[team2]["players"]

    # print(players_team1, "\n")
    # print(players_team2)
    
    facets_info = match(team1,team2)
    
    if team1 in facets_info["bat"] :
        
        print(f"Batting Team : {players_team1}\n")
        print(f"Bowling Team : {players_team2}\n")
    
    else :
        
        print(f"Batting Team : {players_team2}\n")
        print(f"Bowling Team : {players_team1}\n") 
        
        
    


def play():

    matchup("india", "South Africa")


play()
