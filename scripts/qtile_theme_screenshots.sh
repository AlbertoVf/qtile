#!/bin/sh

# * Formato de captura:
# * Window 1:
# * - vscode with .env.example and manager.py
# * - thunar on folder themes
# * Window 2:
# * - terminal with script running

themeScreenshot() {
    name=$1
    echo "$name"

    sed -i "32s/.*/theme = theme_selector("\"$name\"")/" "$HOME/.config/qtile/settings/manager.py"
    sed -i "7s/.*/theme=$name/" "$HOME/.config/qtile/.env"
    sed -i "7s/.*/theme=$name/" "$HOME/.config/qtile/.env.example"
    sleep 1

    xdotool key super+ctrl+r
    sleep 4
    sleep 1

    scrot "$name.jpg" -e 'mv $f ./scheme'
}

screen() {
    cd $HOME/config/qtile/themes
    for file in $(ls *.json | grep -v 'themes.json'); do
        name=$(echo $file | sed 's/\.json$//')
        themeScreenshot $name
        sleep 2
    done
}

python $HOME/.config/qtile/settings/manager.py

screen