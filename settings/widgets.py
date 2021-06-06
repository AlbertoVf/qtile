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
        groupbox(fontsize=13, highlight_method="text"),
        widget.Sep(
            padding=8,
            margin=8,
            foreground=colors["grey"],
            size_percent=50,
        ),
        widget.CurrentLayout(
            margin=4,
            padding=4,
            foreground=colors["focus"],
        ),
        widget.Sep(
            padding=8,
            margin=8,
            foreground=colors["grey"],
            size_percent=50,
        ),
        widget.WindowName(
            max_chars=50,
            formant="{name}",
            margin=4,
            padding=4,
            foreground=colors["focus"],
        ),
        indicator(tx="[{}]", fg=colors["color4"], bg=colors["dark"]),
        widget.Clock(
            padding=4,
            format="[%c]",
            mouse_callbacks={
                "Button1":
                lambda: qtile.cmd_spawn("evolution --component=calendar")
            },
            foreground=colors["color3"],
            background=colors["dark"],
        ),
        widget.Net(
            format="[Up: {up} Down: {down}",
            margin=4,
            padding=4,
            mouse_callbacks={
                "Button3": lambda: qtile.cmd_spawn("nm-connection-editor"),
            },
            foreground=colors["color2"],
        ),
        widget.Sep(
            padding=8,
            margin=8,
            foreground=colors["color2"],
            size_percent=30,
        ),
        widget.CheckUpdates(
            update_interval=1800,
            foreground=colors["color2"],
            distro="Arco_checkupdates",
            display_format="{updates}",
            mouse_callbacks={
                "Button1":
                lambda: qtile.cmd_spawn(terminal + " -e sudo pacman -Syu")
            },
        ),
        widget.TextBox(
            text="⟳ ]",
            foreground=colors["color2"],
        ),
        widget.Volume(
            fmt="[ Vol: {}",
            margin=4,
            padding=4,
            foreground=colors["color1"],
        ),
        widget.Sep(
            padding=8,
            margin=8,
            foreground=colors["color1"],
            size_percent=30,
        ),
        widget.Battery(
            format=" Bat: {percent:2.0%}]",
            mouse_callbacks={
                "Button1":
                lambda: qtile.cmd_spawn("xfce4-power-manager-settings"),
                "Button3": lambda: qtile.cmd_spawn("xfce4-taskmanager"),
                "Button2": lambda: qtile.cmd_spawn(terminal + " -e htop"),
            },
            margin=4,
            padding=4,
            update_interval=10,
            foreground=colors["color1"],
        ),
        systray(size=18),
    ]
    return widgets_list


#
# SECONDARY WINDEWTS LIST
#
def init_widgets_list01():
    widgets_list = [
        groupbox(fontsize=14, highlight_method="text"),
        widget.Sep(
            padding=8,
            margin=8,
            foreground=colors["grey"],
            size_percent=50,
        ),
        widget.CurrentLayout(
            margin=4,
            padding=4,
            foreground=colors["focus"],
        ),
        widget.Sep(
            padding=8,
            margin=8,
            foreground=colors["grey"],
            size_percent=50,
        ),
        widget.WindowName(
            max_chars=50,
            formant="{name}",
            margin=4,
            padding=4,
            foreground=colors["focus"],
        ),
    ]
    return widgets_list
