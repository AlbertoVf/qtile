from os import path
import json

home = path.expanduser("~")
qtile_path = path.join(home, '.config', 'qtile')
qtile_scripts, qtile_themes, config = path.join(qtile_path, "scripts"), path.join( qtile_path, "themes"), path.join(qtile_path, "manager.json")


def check_propertyes(propertyes: list[str]):
    prop = []
    with open(config) as f:
        data = json.load(f)
        for p in propertyes:
            prop.append(data[p])
    return prop


browser, editor, fileManager, mail, terminal, font = check_propertyes(["browser", "editor", "fileManager", "mail", "terminal", "font"])


def check_theme():
    theme = "default"
    if path.isfile(config):
        with open(config) as f:
            theme = json.load(f)["theme"]
    else:
        with open(config, "w") as f:
            json.dump(theme, f)
    return theme


def theme_selector(theme=check_theme()):
    # 1 theme in 1 file
    theme_file = path.join(qtile_themes, f'{theme}.json')
    if not path.isfile(theme_file):
        return 0
    with open(theme_file) as f:
        return json.load(f)


def theme_selector_v2(theme=check_theme()):
    theme_file = path.join(qtile_themes, 'themes.json')
    if not path.isfile(theme_file):
        return 0
    with open(theme_file) as f:
        return json.load(f)[theme]


def scheme_selector():
    if theme_selector() != 0:
        return theme_selector()
    if theme_selector_v2() != 0:
        return theme_selector_v2()
    return theme_selector_v2("default")


theme = scheme_selector()
