from os.path import join, expanduser, exists
from toml import load, loads

qtile_path    = join(expanduser("~"), ".config", "qtile")
qtile_scripts = join(qtile_path, "scripts")
qtile_themes  = join(qtile_path, "themes")


class Theme:
    background, foreground = "background", "foreground"
    active, inactive, focus = color1, color2, color3 = "color1", "color2", "color3"
    color4, color5, color6 = "color4", "color5", "color6"
    file_theme = lambda file: join(qtile_themes, f"{file}.toml")
    default = { background: "#0f101a", foreground: "#f1ffff", color1: "#f1ffff", color2: "#4c566a", color3: "#a151d3", color4: "#F07178", color5: "#fb9f7f", color6: "#ffd47e", }
    tf = set(default.keys())


getenv = lambda key: load(open(f"{qtile_path}/qtile.conf"))["USER"][key]


def theme_selector(theme=getenv("theme")) -> Theme:
    try:
        t = (
            loads(open(Theme.file_theme("themes")).read())[theme]
            if exists(Theme.file_theme("themes"))
            else loads(open(Theme.file_theme(theme)).read())
        )
        if set(t).difference(Theme.tf):
            raise TypeError
    except (ValueError, FileNotFoundError, TypeError):
        t = Theme.default
    return t


mail, console = (getenv("mail"), getenv("console"))
font, theme   = (getenv("font"), theme_selector())

if __name__ == "__main__":
    print(theme)
