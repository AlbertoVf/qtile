import os
import socket
from libqtile import qtile, widget
from settings.shortcut import terminal, colors, font
from settings.widgets_mod import *

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
icon_triangle = ["", ""]
icon_used = icon_triangle


#
# PRYMARY WIDGETS LIST
#
def init_widgets_list():
    widgets_list = [
        widget.GroupBox(
            fontsize=12,
            borderwidth=2,
            rounded=False,
            disable_drag=True,
            highlight_method="line",
            active=colors["active"],
            inactive=colors["inactive"],
            highlight_color=colors["text"],
            this_current_screen_border=colors["focus"],
            other_current_screen_border=colors["text"],
        ),
        widget.CurrentLayout(
            font=f"{font} Bold",
            foreground=colors["urgent"],
        ),
        widget.WindowName(
            font=f"{font} Bold",
            max_chars=50,
            formant="{name}",
            foreground=colors["focus"],
        ),
        widget.CapsNumLockIndicator(
            font=f"{font} Bold",
            fmt="{}",
            foreground=colors["color4"],
        ),
        widget.Volume(
            font=f"{font} Bold",
            fmt="\uf026 {}",
            foreground=colors["color3"],
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
            distro="Arch",
            custom_command="pacman -Qu",
            execute=f"{terminal} -e sudo pacman -Syu",
            update_interval=3600,
            display_format='\uf547 {updates} Updates',
            # no_update_string="\uf547  0 Updates",
            colour_have_updates=colors["urgent"],
            # colour_no_updates=colors["urgent"],
        ),
        widget.Clock(
            font=f"{font} Bold",
            format="\uf5ec  %c",
            mouse_callbacks={
                "Button1":
                lambda: qtile.cmd_spawn("gnome-calendar")
            },
            foreground=colors["color1"],
            background=colors["dark"],
        ),
        systray(),
    ]
    return widgets_list


#
# SECONDARY WINDEWTS LIST
#
def init_widgets_list01():
    widgets_list = [
        widget.WindowName(
            font=f"{font} Bold",
            formant="{name}",
            foreground=colors["focus"],
        ),
        widget.Clock(
            font=f"{font} Bold",
            format="[ %c ]",
            foreground=colors["color4"],
            background=colors["dark"],
        ),
    ]
    return widgets_list
