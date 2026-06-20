def teams():

    team = {
        "india": {
            "players": [
                {
                    "position": 1,
                    "First name": "Abhishek",
                    "Last name": "Sharma",
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
                    "First name": "jasprit",
                    "Last name": "Bumrah",
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
                    "First name": "Aiden",
                    "Last name": "Markram",
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
                    "First name": "kagiso",
                    "Last name": "Rabada",
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


def play():

    playerInfo = teams()
    print(playerInfo)


play()
