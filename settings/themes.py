import json
from os import path
from settings.path import qtile_themes, qtile_path


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

    with open(path.join(theme_file)) as f:
        return json.load(f)
