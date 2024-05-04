from os.path import join, expanduser, exists

from yaml import safe_load as load


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
config        = join(expanduser("~"), ".config")
qtile_path    = join(config, "qtile")
qtile_scripts = join(qtile_path, "scripts")
qtile_themes  = join(qtile_path, "themes")
terminal      = getenv("console")
font          = getenv("font")
mail          = getenv("mail")


def theme_selector(theme=getenv("theme")) -> Theme:
    try:
        if exists(join(qtile_themes, "themes.yaml")):
            t = load(open(join(qtile_themes, "themes.yaml")))[theme]
        elif exists(join(qtile_themes, f"{theme}.yaml")):
            t = load(open(join(qtile_themes, f"{theme}.yaml")))
        if not set(t.keys()).issubset(set([Theme.background, Theme.foreground, Theme.active, Theme.inactive, Theme.color1, Theme.color2, Theme.color3, Theme.color4])):
            raise ValueError("Theme must have 8 values")
    except (ValueError, FileNotFoundError):
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
    return {layout: color.replace("0x", "#") for layout, color in t.items()}


theme = theme_selector()
