import json

themes=[]

def build_theme_json():
    global themes
    with open("themes/themes.json","r") as f:
        data = json.load(f)

    for t in data:
        themes.append(t)
        scheme = data[t]
        with open(f"themes/{t}.json", "w") as outfile:
            json.dump(scheme, outfile,indent=2)


def update_readme():
    with open("themes/Previews.md","w") as f:
        f.writelines("# Previews\n")
        for theme in themes:
            title = f"\n## {theme}\n"
            image = f"![{theme}](./scheme/{theme}.jpg)\n"
            f.writelines([title,image])

if __name__ == "__main__":
    build_theme_json()
    update_readme()
