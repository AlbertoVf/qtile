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
            font=font,
            fontsize=12,
            borderwidth=4,
            rounded=False,
            disable_drag=True,
            highlight_method="line",
            active=colors["active"],
            inactive=colors["inactive"],
            highlight_color=colors["grey"],
            this_current_screen_border=colors["focus"],
            other_current_screen_border=colors["focus"],
            this_screen_border=colors["color3"],
            other_screen_border=colors["color3"],
        ),
        separator(),
        widget.CurrentLayout(
            foreground=colors["focus"],
        ),
        separator(),
        widget.WindowName(
            max_chars=50,
            formant="{name}",
            foreground=colors["focus"],
        ),
        widget.CapsNumLockIndicator(
            fmt="[ {} ]",
            foreground=colors["color4"],
            backgound=colors["dark"]
        ),
        widget.Clock(
            format="[ %c ]",
            mouse_callbacks={
                "Button1":
                lambda: qtile.cmd_spawn("evolution --component=calendar")
            },
            foreground=colors["color3"],
            background=colors["dark"],
        ),
        widget.Net(
            format="[ Up:{up}  Down:{down}",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("nm-connection-editor"),
            },
            foreground=colors["color2"],
        ),
        separator(fg=colors["color2"], size=30),
        widget.CheckUpdates(
            distro="Arch",
            custom_command="pacman -Qu",
            update_interval=1800,
            execute=f"{terminal} -e sudo pacman -Syu",
            display_format='Updates: {updates} ]',
            no_update_string="Updates: 0 ]",
            colour_no_updates=colors["color2"],
            colour_have_updates=colors["color2"],
        ),
        widget.Volume(
            fmt="[ Vol: {}",
            foreground=colors["color1"],
        ),
        separator(fg=colors["color1"], size=30),
        widget.Battery(
            format="Bat: {percent:2.0%} ]",
            mouse_callbacks={
                "Button1":
                lambda: qtile.cmd_spawn("xfce4-power-manager-settings"),
                "Button2": lambda: qtile.cmd_spawn(terminal + " -e htop"),
                "Button3": lambda: qtile.cmd_spawn("xfce4-taskmanager"),
            },
            update_interval=10,
            foreground=colors["color1"],
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
            formant="{name}",
            foreground=colors["focus"],
        ),
        separator(),
        widget.Clock(
            format="[ %c ]",
            foreground=colors["color3"],
            background=colors["dark"],
        ),
    ]
    return widgets_list
