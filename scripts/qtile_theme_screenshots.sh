#!/usr/bin/env bash

themeScreenshot() {
    name=$1
    echo "$name"
    qtile_manager -t $name
    sleep 5
    scrot "$name.jpg"
}

screen() {
    cd "$HOME/.config/qtile/themes"
    sleep 3
    for file in $(ls *.yml | grep -v 'themes.yml'); do
        name=$(echo $file | sed 's/\.yml$//')
        themeScreenshot $name
        sleep 3
    done
    mv -f *.jpg scheme/
}

screen