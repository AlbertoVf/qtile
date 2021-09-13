import json
from settings.shortcut import qtile_path, qtile_themes
from os import path


def theme_selector():
    theme = "default"
    config = path.join(qtile_path, "theme.json")

    if path.isfile(config):
        with open(config) as f:
            theme = json.load(f)["theme"]
    else:
        with open(config, "w") as f:
            f.write(f'{{\n"theme": "{theme}\n"}}\n')

    theme_file = path.join(qtile_themes, f'{theme}.json')

    if not path.isfile(theme_file):
        raise Exception(f'"{theme_file}" does not exist')

    with open(theme_file) as f:
        return json.load(f)


colors = theme_selector()
