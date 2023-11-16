from os.path import join, expanduser

from json import load


class Theme:
    background = "background"
    foreground = "foreground"
    active     = "active"
    inactive   = "inactive"
    color1     = "color1"
    color2     = "color2"
    color3     = "color3"
    color4     = "color4"


getenv        = lambda key: load(open(f"{qtile_path}/.env", "r"))[key]
home          = expanduser("~")
qtile_path    = join(home, ".config", "qtile")
qtile_scripts = join(qtile_path, "scripts")
terminal      = getenv("console")
font          = getenv("font")
mail          = getenv("mail")


def theme_selector(theme=getenv("theme")) -> Theme:
    qtile_themes = join(qtile_path, "themes")
    try:
        t = load(open(join(qtile_themes, "themes.json")))[theme]
    except:
        try:
            t = load(open(join(qtile_themes, f"{theme}.json")))
        except:
            t = {
                Theme.background : "#0f101a",
                Theme.foreground : "#f1ffff",
                Theme.active     : "#f1ffff",
                Theme.inactive   : "#4c566a",
                Theme.color1     : "#a151d3",
                Theme.color2     : "#F07178",
                Theme.color3     : "#fb9f7f",
                Theme.color4     : "#ffd47e",
            }
    return t


theme = theme_selector()
