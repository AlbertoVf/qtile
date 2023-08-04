#!/bin/sh
env_file="$HOME/.config/qtile/.env"

# change qtile properties:
# :: change_environment "font" "FantasqueSansM Nerd Font"
# :: change_environment "mail" "thunderbird"
# :: change_environment "terminal" "kitty"
# :: change_environment "theme" "gruvbox"
change_environment(){
    property="$1"
    value="$2"

    echo "property $property change to value $value"
    jq -r ".\"$property\" = \"$value\"" $env_file > $env_file.temp && mv $env_file.temp $env_file
}

change_environment "$1" "$2"
