#!/bin/bash

QTILE_PATH_CONFIG="$HOME/.config/qtile/.config"
USER_PATH_CONFIG="$HOME/.config"

CONFIG=$USER_PATH_CONFIG # QTILE_PATH_CONFIG

function run {
    if ! pgrep $1; then
        $@ &
    fi
}

run variety
run plank
run xfce4-power-manager
run xfce4-clipman
numlockx on &
run volumeicon
run nm-applet
blueberry-tray &
run pamac-tray
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
sxhkd -c $CONFIG/sxhkd/sxhkdrc &
picom --config $CONFIG/picom/picom.conf &
(conky -c $CONFIG/conky/.conkyrc) &