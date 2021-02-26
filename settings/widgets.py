from libqtile import qtile, widget
import os
import socket
from settings.shortcut import terminal
from settings.themes import *
from settings.path import *

colors = Colors()
icon_left = ""
icon_right = ""
f = 'FiraCode Nerd Font'


def init_widgets_list0():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

    widgets_list = [
        widget.TextBox(
            text="",
            fontsize=22,
            padding=16,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('rofi -show run'),
                "Button3": lambda: qtile.cmd_spawn('xfce4-appfinder'),
            },
            background=colors.dark,
            foreground=colors.color3,
        ),
        widget.TextBox(
            text=icon_left,
            fontsize=40,
            padding=-6,
            foreground=colors.dark,
            background=colors.grey,
        ),
        widget.GroupBox(
            fontsize=18,
            margin=4,
            padding=8,
            borderwidth=0,
            disable_drag=True,
            rounded=False,
            highlight_method="text",
            active=colors.active,
            inactive=colors.inactive,
            this_current_screen_border=colors.focus,
            background=colors.grey,
        ),
        widget.TextBox(
            text=icon_left,
            fontsize=40,
            padding=-6,
            foreground=colors.grey,
            background=colors.focus,
        ),
        widget.CurrentLayout(
            foreground=colors.light,
            background=colors.focus,
        ),
        widget.CurrentLayoutIcon(
            scale=0.7,
            padding=0,
            background=colors.focus,
        ),
        widget.TextBox(
            text=icon_left,
            fontsize=40,
            padding=-6,
            foreground=colors.focus,
        ),
        widget.WindowName(
            fontsize=12,
            foreground=colors.focus,
        ),
        widget.TextBox(
            text=icon_right,
            fontsize=40,
            padding=-6,
            foreground=colors.color4,
        ),
        widget.CapsNumLockIndicator(
            font="{f} Italic Bold",
            fontsize=12,
            padding=8,
            foreground=colors.text,
            background=colors.color4,
        ),

        widget.TextBox(
            text=icon_right,
            fontsize=40,
            padding=-6,
            foreground=colors.color3,
            background=colors.color4,
        ),
        widget.Clock(
            padding=4,
            format=" %H:%M:%S - %d/%m/%Y",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('evolution --component=calendar')
            },
            foreground=colors.text,
            background=colors.color3,
        ),

        widget.TextBox(
            text=icon_right,
            fontsize=40,
            padding=-6,
            foreground=colors.color2,
            background=colors.color3,
        ),
        widget.Systray(
            icon_size=22,
            margin=4,
            padding=8,
            background=colors.color2,
        ),

        widget.TextBox(
            text=icon_right,
            fontsize=40,
            padding=-6,
            foreground=colors.color1,
            background=colors.color2,
        ),
        widget.Battery(
            format="  {percent:2.0%}",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('xfce4-power-manager-settings')
            },
            padding=0,
            update_interval=10,
            foreground=colors.text,
            background=colors.color1,
        ),
        widget.ThermalSensor(
            padding=8,
            metric=True,
            threshold=40,
            fmt=" {}",
            foreground="#ffff00",
            foreground_alert="#ff0000",
            background=colors.color1,
        ),
        widget.TextBox(
            text="⏻",
            padding=8,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('arcolinux-logout')
            },
            foreground=colors.text,
            background=colors.color1,
        ),
    ]
    return widgets_list


def init_widgets_list1():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

    widgets_list = [
        widget.TextBox(
            text="",
            fontsize=22,
            padding=16,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('rofi -show run'),
                "Button3": lambda: qtile.cmd_spawn('xfce4-appfinder'),
            },
            background=colors.dark,
            foreground=colors.color3,
        ),
        widget.TextBox(
            text=icon_left,
            fontsize=40,
            padding=-6,
            foreground=colors.dark,
            background=colors.grey,
        ),
        widget.GroupBox(
            fontsize=18,
            margin=4,
            padding=8,
            borderwidth=0,
            disable_drag=True,
            rounded=False,
            highlight_method="text",
            active=colors.active,
            inactive=colors.inactive,
            highlight_color=colors.grey,
            this_current_screen_border=colors.focus,
            background=colors.grey,
            this_screen_border=colors.grey,
            other_current_screen_border=colors.active,
            other_screen_border=colors.inactive,
        ),
        widget.TextBox(
            text=icon_left,
            fontsize=40,
            padding=-6,
            foreground=colors.grey,
            background=colors.focus,
        ),
        widget.CurrentLayout(
            foreground=colors.light,
            background=colors.focus,
        ),
        widget.CurrentLayoutIcon(
            scale=0.7,
            padding=0,
            background=colors.focus,
        ),
        widget.TextBox(
            text=icon_left,
            fontsize=40,
            padding=-6,
            foreground=colors.focus,
        ),
        widget.WindowName(
            fontsize=12,
            foreground=colors.focus,
        ),
        widget.TextBox(
            text=icon_right,
            fontsize=40,
            padding=-6,
            foreground=colors.color4,
        ),
        widget.CapsNumLockIndicator(
            font="{f} Italic Bold",
            fontsize=10,
            foreground=colors.text,
            background=colors.color4,
        ),

        widget.TextBox(
            text=icon_right,
            fontsize=40,
            padding=-6,
            foreground=colors.color3,
            background=colors.color4,
        ),
        widget.Clock(
            format=" %H:%M:%S %d/%m/%Y",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('evolution --component=calendar')
            },
            foreground=colors.text,
            background=colors.color3,
        ),
        widget.TextBox(
            text=icon_right,
            fontsize=40,
            padding=-6,
            foreground=colors.color2,
            background=colors.color3,
        ),
        widget.Systray(
            icon_size=22,
            margin=4,
            padding=8,
            background=colors.color2,
        ),
        widget.TextBox(
            text=icon_right,
            fontsize=40,
            padding=-6,
            foreground=colors.color1,
            background=colors.color2,
        ),
        widget.Net(
            format='{down}\uf545 {up}\uf55d',
            fontsize=14,
            margin=4,
            padding=8,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn('nm-connection-editor'),
            },
            foreground=colors.text,
            background=colors.color1,
        ),
        widget.TextBox(
            text="",
            fontsize=22,
            margin=4,
            padding=8,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')
            },
            foreground=colors.text,
            background=colors.color1,
        ),
        widget.TextBox(
            text="",
            fontsize=22,
            margin=4,
            padding=8,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')
            },
            foreground=colors.text,
            background=colors.color1,
        ),
        widget.Battery(
            format="  {percent:2.0%}",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('xfce4-power-manager-settings')
            },
            padding=0,
            update_interval=10,
            foreground=colors.text,
            background=colors.color1,
        ),
        widget.ThermalSensor(
            padding=8,
            metric=True,
            threshold=40,
            fmt=" {}",
            foreground="#ffff00",
            foreground_alert="#ff0000",
            background=colors.color1,
        ),
    ]
    return widgets_list


def init_widgets_list2():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

    widgets_list = [
        widget.TextBox(
            text="",
            fontsize=22,
            padding=10,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('rofi -show run'),
                "Button3": lambda: qtile.cmd_spawn('xfce4-appfinder'),
            },
            background=colors.dark,
            foreground=colors.color3,
        ),
        widget.TextBox(
            text=icon_left,
            fontsize=38,
            margin=0,
            padding=-5,
            foreground=colors.dark,
            background=colors.grey,
        ),
        widget.GroupBox(
            fontsize=18,
            padding=8,
            borderwidth=0,
            disable_drag=True,
            rounded=False,
            highlight_method="text",
            active=colors.active,
            inactive=colors.inactive,
            highlight_color=colors.grey,
            this_current_screen_border=colors.focus,
            background=colors.grey,
            this_screen_border=colors.grey,
            other_current_screen_border=colors.active,
            other_screen_border=colors.inactive,
        ),
        widget.TextBox(
            text=icon_left,
            fontsize=38,
            margin=0,
            padding=-5,
            foreground=colors.grey,
            background=colors.focus,
        ),
        widget.CurrentLayout(
            foreground=colors.light,
            background=colors.focus,
        ),
        widget.CurrentLayoutIcon(
            scale=0.7,
            padding=0,
            background=colors.focus,
        ),
        widget.TextBox(
            text=icon_left,
            fontsize=38,
            margin=0,
            padding=-5,
            foreground=colors.focus,
        ),
        widget.WindowName(
            fontsize=12,
            max_chars=32,
            formant='{name}',
            foreground=colors.focus,
        ),
        widget.TextBox(
            text=icon_right,
            fontsize=38,
            margin=0,
            padding=-5,
            foreground=colors.color4,
        ),
        widget.CapsNumLockIndicator(
            font=f"{f} Italic Bold",
            fontsize=10,
            foreground=colors.text,
            background=colors.color4,
        ),

        widget.TextBox(
            text=icon_right,
            fontsize=38,
            margin=0,
            padding=-5,
            foreground=colors.color3,
            background=colors.color4,
        ),
        widget.Clock(
            format="[%d %b, %H.%M]",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('evolution --component=calendar')
            },
            foreground=colors.text,
            background=colors.color3,
        ),
        widget.TextBox(
            text=icon_right,
            fontsize=38,
            margin=0,
            padding=-5,
            foreground=colors.color2,
            background=colors.color3,
        ),
        widget.Net(
            format='[Net:{down} \uf545\uf55d {up}]',
            padding=4,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn('nm-connection-editor'),
            },
            foreground=colors.text,
            background=colors.color2,
        ),
        widget.Volume(
            fmt="[Vol: {}]",
            padding=4,
            foreground=colors.text,
            background=colors.color2,
        ),
        widget.TextBox(
            text=icon_right,
            fontsize=38,
            margin=0,
            padding=-5,
            foreground=colors.color1,
            background=colors.color2,
        ),
        widget.Systray(
            icon_size=22,
            margin=8,
            padding=8,
            background=colors.color1,
        ),
        widget.Battery(
            format="[Bat:{percent:2.0%}]",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('xfce4-power-manager-settings'),
                'Button1': lambda: qtile.cmd_spawn('xfce4-taskmanager'),
                'Button2': lambda: qtile.cmd_spawn(terminal + ' -e htop'),
            },
            padding=8,
            update_interval=10,
            foreground=colors.text,
            background=colors.color1,
        ),
    ]
    return widgets_list


def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    f = 'Hack Bold'
    widgets_list = [
        widget.GroupBox(
            fontsize=18,
            padding=8,
            borderwidth=0,
            disable_drag=True,
            rounded=False,
            highlight_method="text",
            active=colors.active,
            inactive=colors.inactive,
            highlight_color=colors.grey,
            this_current_screen_border=colors.focus,
            this_screen_border=colors.grey,
            other_current_screen_border=colors.active,
            other_screen_border=colors.inactive,
        ),
        widget.CurrentLayout(
            foreground=colors.focus,
            margin=4,
            padding=4,
        ),
        widget.WindowName(
            fontsize=12,
            max_chars=32,
            formant='{name}',
            margin=4,
            padding=4,
            foreground=colors.focus,
        ),
        widget.CapsNumLockIndicator(
            font=f"{f} italic",
            fmt="[{}]",
            fontsize=12,
            margin=4,
            padding=4,
            foreground=colors.color4,
        ),

        widget.Clock(
            fontsize=14,
            format="[%c]",
            margin=4,
            padding=4,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('evolution --component=calendar')
            },
            foreground=colors.color3,
        ),

        widget.Net(
            fontsize=14,
            format='[Net:{down} \uf545\uf55d {up}]',
            margin=4,
            padding=4,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn('nm-connection-editor'),
            },
            foreground=colors.color2,
        ),
        widget.Volume(
            fontsize=14,
            fmt="[Vol: {}]",
            margin=4,
            padding=4,
            foreground=colors.color2,
        ),
        widget.Battery(
            fontsize=14,
            format="[Bat:{percent:2.0%}]",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('xfce4-power-manager-settings'),
                'Button1': lambda: qtile.cmd_spawn('xfce4-taskmanager'),
                'Button2': lambda: qtile.cmd_spawn(terminal + ' -e htop'),
            },
            margin=4,
            padding=4,
            update_interval=10,
            foreground=colors.color1,
        ),

        widget.Systray(
            icon_size=22,
            margin=8,
            padding=8,
        ),
    ]
    return widgets_list
