from os.path import join, expanduser, exists

from toml import load, loads

config        = join(expanduser("~"), ".config")
qtile_path    = join(config, "qtile")
qtile_scripts = join(qtile_path, "scripts")
qtile_themes  = join(qtile_path, "themes")
getenv        = lambda key: load(open(f"{qtile_path}/qtile.conf"))['USER'][key]
terminal      = getenv("console")
font          = getenv("font")
mail          = getenv("mail")

class Theme:
    background = "background"
    foreground = "foreground"
    active = "active"
    inactive = "inactive"
    color1 = "color1"
    color2 = "color2"
    color3 = "color3"
    color4 = "color4"
    tf = set([background, foreground, active, inactive, color1, color2, color3, color4])

def theme_selector(theme=getenv("theme")) -> Theme:
    try:
        t = loads(open(join(qtile_themes, "themes.toml")).read())[theme] if exists(join(qtile_themes, "themes.toml")) else loads(open(join(qtile_themes, f"{theme}.toml")).read())
        if not set(t.keys()).issubset(Theme.tf):
            raise ValueError("Theme must have 8 values")
    except (ValueError, FileNotFoundError):
        t = { Theme.background: "#0f101a", Theme.foreground: "#f1ffff", Theme.active: "#f1ffff", Theme.inactive: "#4c566a", Theme.color1: "#a151d3", Theme.color2: "#F07178", Theme.color3: "#fb9f7f", Theme.color4: "#ffd47e" }
    return t


theme = theme_selector()

if __name__ == "__main__":
    print(theme)
