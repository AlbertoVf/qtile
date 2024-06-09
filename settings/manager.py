from os.path import join, expanduser, exists
from toml import load, loads

qtile_path    = join(expanduser("~"), ".config", "qtile")
qtile_scripts = join(qtile_path, "scripts")
qtile_themes  = join(qtile_path, "themes")


def getenv(key, config_name="USER"):
    config = load(open(f"{qtile_path}/qtile.conf"))
    return config.get(config_name, {}).get(key, config["DEFAULT"].get(key))


class Theme:
    background, foreground = "background", "foreground"
    active, inactive = ( "active", "inactive")
    color1, color2, color3, color4 = ( "color1", "color2", "color3", "color4" )
    tf = set([background, foreground, active, inactive, color1, color2, color3, color4])
    file_theme = lambda file: join(qtile_themes, f"{file}.toml")


def theme_selector(theme=getenv("theme")) -> Theme:
    try:
        t = (
            loads(open(Theme.file_theme("themes")).read())[theme]
            if exists(Theme.file_theme("themes"))
            else loads(open(Theme.file_theme(theme)).read())
        )
        if not set(t.keys()).issubset(Theme.tf):
            raise ValueError("Theme must have 8 values")
    except (ValueError, FileNotFoundError):
        t = { Theme.background: "#0f101a", Theme.foreground: "#f1ffff", Theme.active: "#f1ffff", Theme.inactive: "#4c566a", Theme.color1: "#a151d3", Theme.color2: "#F07178", Theme.color3: "#fb9f7f", Theme.color4: "#ffd47e", }
    return t


mail, terminal = (getenv("mail"), getenv("terminal"))
font, theme    = (getenv("font"), theme_selector())

if __name__ == "__main__":
    print(theme)
