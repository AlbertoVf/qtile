import os
import socket
from libqtile import qtile, widget

from settings.shortcut import terminal, font
from settings.themes import colors
from settings.widgets_mod import *


# PRYMARY WIDGETS LIST
def init_widgets_list():
    widgets_list = [
        group_box(colors["color2"], colors["color3"]),
        current_layout(),
        window_name(),
        widget.CapsNumLockIndicator(
            font=f"{font} Bold",
            fontsize=12,
            fmt="{}",
            foreground=colors["color4"],
        ),
        widget.Volume(
            font=f"{font}",
            fmt="\uf026 {}",
            foreground=colors["color3"],
            mouse_callbacks={
                "Button3": lambda: qtile.cmd_spawn("pavucontrol"),
            },
        ),
        widget.Battery(
            font=f"{font} Bold",
            format=" {percent:2.0%} \ufbd3",
            mouse_callbacks={
                "Button1":
                lambda: qtile.cmd_spawn("xfce4-power-manager-settings"),
                "Button2": lambda: qtile.cmd_spawn(terminal + " -e htop"),
                "Button3": lambda: qtile.cmd_spawn("xfce4-taskmanager"),
            },
            update_interval=10,
            foreground=colors["color2"],
        ),
        widget.CheckUpdates(
            font=f"{font} Bold",
            distro="Arch_checkupdates",
            execute=f"{terminal} -e sudo pacman -Syu",
            update_interval=1800,
            display_format='\uf547 {updates} Updates',
            colour_have_updates=colors["color1"],
        ),
        widget.Clock(
            font=f"{font} Bold",
            format="\uf5ec %c",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(terminal + " -e calcurse"),
                "Button3": lambda: qtile.cmd_spawn("gnome-calendar")
            },
            foreground=colors["color1"],
        ),
        systray(size=22),
    ]
    return widgets_list


# SECONDARY WINDEWTS LIST
def init_widgets_list01():
    widgets_list = [
        current_layout(),
        window_name(),
        group_box(colors["color3"], colors["color2"]),
    ]
    return widgets_list
