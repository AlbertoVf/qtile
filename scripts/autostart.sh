#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

(conky -c $HOME/.conkyrc) &
# run concky-toogle
run variety &
run nm-applet &
run pamac-tray &
run xfce4-power-manager &
numlockx on &
blueberry-tray &
picom --config $HOME/.config/qtile/scripts/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
run volumeicon &
run megasync &
run teamviewer --daemon start
