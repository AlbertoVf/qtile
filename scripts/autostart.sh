#!/bin/bash

QTILE_PATH_CONFIG="$HOME/.config/qtile/.config"

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
sxhkd -c $QTILE_PATH_CONFIG/sxhkdrc &
picom --config $QTILE_PATH_CONFIG/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
(conky -c $QTILE_PATH_CONFIG/.conkyrc) &