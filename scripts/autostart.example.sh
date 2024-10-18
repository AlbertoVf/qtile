#!/bin/bash

CONFIG="$HOME/.config/qtile/scripts/.config"

variety &
xfce4-clipman &
blueberry-tray &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
(conky -c ~/.conkyrc) &
nm-applet
sxhkd -c "$CONFIG/sxhkd/sxhkdrc" &
picom --config "$CONFIG/picom/picom.conf" &