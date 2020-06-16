from configparser import ConfigParser

def create_new_config():
    config = ConfigParser()

    #Basic Settings of App
    config["Basic"] = {
        "TITLE":"Battleships",
        "WIDTH":"800",
        "HEIGHT":"600",
        "FPS":"60",
        "ALG1":"1",
        "ALG2":"2"
    }

    #Game Rules
    config["Rules"] = {
        "SHIP_SIZE":"4",
        "X_RANGE":"10",
        "Y_RANGE":"10"
    }

    #Text
    config["Text"] = {
        "PLAYER":"PLAYER",
        "AI":"AI",
        "AI1":"AI 1",
        "AI2":"AI 2",
        "SCORE":"SCORE"
    }

    #Points
    config["Points"] = {
        "PLAYER_PTS":"0",
        "AI_PTS":"0",
        "AI1_PTS":"0",
        "AI2_PTS":"0"
    }

    with open('./cfg.ini', 'w') as f:
        config.write(f)
    return config