from os.path import join, expanduser, exists
from toml import load, loads

qtile_path    = join(expanduser("~"), ".config", "qtile")
qtile_scripts = join(qtile_path, "scripts")
qtile_themes  = join(qtile_path, "themes")


class Theme:
    background, foreground = "background", "foreground"
    active, inactive = "color1", "color2"
    color3, color4, color5, color6 = "color3", "color4", "color5", "color6"
    tf = set([background, foreground, active, inactive, color3, color4, color5, color6])
    file_theme = lambda file: join(qtile_themes, f"{file}.toml")
    default = { background: "#0f101a", foreground: "#f1ffff", active: "#f1ffff", inactive: "#4c566a", color3: "#a151d3", color4: "#F07178", color5: "#fb9f7f", color6: "#ffd47e", }


def getenv(key, config_name="USER"):
    config = load(open(f"{qtile_path}/qtile.conf"))
    return config.get(config_name, {}).get(key, config["DEFAULT"].get(key))


def theme_selector(theme=getenv("theme")) -> Theme:
    try:
        t = (
            loads(open(Theme.file_theme("themes")).read())[theme]
            if exists(Theme.file_theme("themes"))
            else loads(open(Theme.file_theme(theme)).read())
        )
        if Theme.tf - set(t):
            raise TypeError
    except (ValueError, FileNotFoundError,TypeError):
        t = Theme.default
    return t


mail, console = (getenv("mail"), getenv("console"))
font, theme   = (getenv("font"), theme_selector())

if __name__ == "__main__":
    print(theme)
