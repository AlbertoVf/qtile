import json
from os import path
from settings.shortcut import qtile_path, qtile_themes


def check_theme():
    theme = "default"
    config = path.join(qtile_path, "theme.json")

    if path.isfile(config):
        with open(config) as f:
            theme = json.load(f)["theme"]
    else:
        with open(config, "w") as f:
            f.write(f'{{\n"theme": "{theme}\n"}}\n')
    return theme


def theme_selector(theme=check_theme()):
    # 1 theme in 1 file
    theme_file = path.join(qtile_themes, f'{theme}.json')

    if not path.isfile(theme_file):
        # raise Exception(f'"{theme_file}" does not exist')
        return 0
    with open(theme_file) as f:
        return json.load(f)


def theme_selector_v2(theme=check_theme()):
    # +1 themes in 1 file
    theme_file = path.join(qtile_themes, 'themes.json')

    if not path.isfile(theme_file):
        # raise Exception(f'"{theme_file}" does not exist')
        return 0
    with open(theme_file) as f:
        return json.load(f)[theme]


def scheme_selector():
    color_scheme = None

    if theme_selector() != 0:
        color_scheme = theme_selector()
    else:
        color_scheme = theme_selector_v2()
    return color_scheme


colors = scheme_selector()
