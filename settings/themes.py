import json

from settings.path import qtile_themes, qtile_path


class Colors:
    dark = "#292d3e"
    grey = "#434758"
    light = "#ffffff"
    text = "#292d3e"
    focus = "#A77AC4"
    active = "#ff5555"
    inactive = "#f1ffff"
    urgent = "#4c566a"
    color1 = "#ff5555"
    color2 = "#A77AC4"
    color3 = "#7197E7"
    color4 = "#ffb86c"

    def __init__(self):
        tema = theme_selector()
        p = f"{qtile_themes}/{tema}.json"

        with open(p) as themes:
            theme = json.load(themes)[tema]
            for colors in theme:
                self.dark = colors["dark"]
                self.grey = colors["grey"]
                self.light = colors["light"]
                self.text = colors["text"]
                self.focus = colors["focus"]
                self.active = colors["active"]
                self.inactive = colors["inactive"]
                self.urgent = colors["urgent"]
                self.color1 = colors["color1"]
                self.color2 = colors["color2"]
                self.color3 = colors["color3"]
                self.color4 = colors["color4"]


def theme_selector():
    configTheme = f"{qtile_path}/theme.json"
    with open(configTheme) as f:
        theme = json.load(f)["theme"]
        return str(theme)
