#!/bin/bash

function run {
    if ! pgrep $1; then
        $@ &
    fi
}

run variety &
run plank &
run xfce4-power-manager &
run xfce4-clipman &
numlockx on &
run volumeicon &
run nm-applet &
blueberry-tray &
run pamac-tray &
run megasync &
sxhkd -c $HOME/.config/sxhkd/sxhkdrc &
picom --config $HOME/.config/picom/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
(conky -c $HOME/.conkyrc) &
