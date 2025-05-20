from os.path import join, expanduser, exists
from toml import load, loads

config        = join(expanduser("~"), ".config")
qtile_path    = join(config, "qtile")
qtile_themes  = join(qtile_path, "themes")


class Theme:
    background, foreground = "#0f101a", "#f1ffff"
    color1    , active     = "#f1ffff", property(lambda self: self.color1)
    color2    , inactive   = "#4c566a", property(lambda self: self.color2)
    color3    , focus      = "#a151d3", property(lambda self: self.color3)
    color4    , color5,     color6     = "#F07178", "#fb9f7f", "#ffd47e"

    file_theme = lambda file: join(qtile_themes, f"{file}.toml")
    default = { "background": background, "foreground": foreground, "color1": active, "color2": inactive, "color3": focus, "color4": color4, "color5": color5, "color6": color6, }
    tf = set(default.keys())

    def __init__(self, theme: dict = default):
        for clave, valor in theme.items():
            setattr(self, clave, valor)


getenv = lambda key: load(open(f"{qtile_path}/qtile.conf")).get("USER", {}).get(key)


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
    return Theme(t)


mail, terminal = (getenv("mail"), getenv("terminal"))
font, theme   = (getenv("font"), theme_selector())

if __name__ == "__main__":
    print(getenv("theme"), theme.__dict__)
