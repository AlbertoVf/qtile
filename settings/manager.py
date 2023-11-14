from os import path
import json

home = path.expanduser("~")
qtile_path = path.join(home, ".config", "qtile")
qtile_scripts = path.join(qtile_path, "scripts")


getenv = lambda key: json.load(open(f"{qtile_path}/.env", "r"))[key]

terminal = getenv("console")
font = getenv("font")
mail = getenv("mail")


def theme_selector(theme=getenv("theme")):
    qtile_themes = path.join(qtile_path, "themes")
    try:
        return json.load(open(path.join(qtile_themes, "themes.json")))[theme]
    except:
        try:
            return json.load(open(path.join(qtile_themes, f"{theme}.json")))
        except:
            pass

    return {
        "background": "#0f101a",
        "foreground": "#f1ffff",
        "active": "#f1ffff",
        "inactive": "#4c566a",
        "color1": "#a151d3",
        "color2": "#F07178",
        "color3": "#fb9f7f",
        "color4": "#ffd47e",
    }

theme = theme_selector()
