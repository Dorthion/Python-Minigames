from configparser import ConfigParser

def create_new_config():
    config = ConfigParser()

    #Basic Settings of App
    config["Basic"] = {
        "TITLE":"Battleships",
        "WIDTH":"800",
        "HEIGHT":"600",
        "FPS":"60",
        "ALG":"1"
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
        "AI1":"AI1",
        "AI2":"AI2",
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