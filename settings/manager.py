import os
import json

from dotenv import load_dotenv

load_dotenv()

qtile_path = os.path.join(os.path.expanduser("~"), ".config", "qtile")
qtile_scripts = os.path.join(qtile_path, "scripts")

fileManager = os.getenv("fileManager")
terminal = os.getenv("terminal")
font = os.getenv("font")
mail = os.getenv("mail")


def theme_selector(theme=os.getenv("theme")):
    qtile_themes = os.path.join(qtile_path, "themes")
    try:
        with open(os.path.join(qtile_themes, "themes.json")) as f:
            return json.load(f)[theme]
    except:
        try:
            with open(os.path.join(qtile_themes, f"{theme}.json")) as g:
                return json.load(g)
        except:
            pass

    return {"background": "#0f101a", "foreground": "#f1ffff", "active": "#f1ffff", "inactive": "#4c566a", "color1": "#a151d3", "color2": "#F07178", "color3": "#fb9f7f", "color4": "#ffd47e"}

theme = theme_selector()

if __name__ == "__main__":
    themes = []
    qtile_themes = os.path.join(qtile_path, "themes")
    with open(f"{qtile_themes}/themes.json", "r") as f:
        data = json.load(f)

    for t in data:
        themes.append(t)
        scheme = data[t]
        with open(f"{qtile_themes}/{t}.json", "w") as outfile:
            json.dump(scheme, outfile, indent=4)

    with open(f"{qtile_themes}/Previews.md", "w") as f:
        f.write("# Previews\n")
        for theme in themes:
            l = f"\n## {theme}\n![{theme}](./scheme/{theme}.jpg)\n"
            f.write(l)
