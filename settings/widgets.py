from libqtile import qtile, widget
import os
import socket
from settings.shortcut import terminal, colors, font
from settings.path import *


def init_widgets_list0():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    font = 'FiraCode Nerd Font'
    icon_left = ""
    icon_right = ""

    widgets_list = [
        widget.TextBox(
            text="",
            font='{font}',
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
            font=f'{font}',
            fontsize=40,
            padding=-6,
            foreground=colors.dark,
            background=colors.grey,
        ),
        widget.GroupBox(
            font=f'{font}',
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
            font=f'{font}',
            text=icon_left,
            fontsize=40,
            padding=-6,
            foreground=colors.grey,
            background=colors.focus,
        ),
        widget.CurrentLayout(
            font=f'{font}',
            foreground=colors.light,
            background=colors.focus,
        ),
        widget.CurrentLayoutIcon(
            font=f'{font}',
            scale=0.7,
            padding=0,
            background=colors.focus,
        ),
        widget.TextBox(
            font=f'{font}',
            text=icon_left,
            fontsize=40,
            padding=-6,
            foreground=colors.focus,
        ),
        widget.WindowName(
            font=f'{font}',
            fontsize=12,
            foreground=colors.focus,
        ),
        widget.TextBox(
            font=f'{font}',
            text=icon_right,
            fontsize=40,
            padding=-6,
            foreground=colors.color4,
        ),
        widget.CapsNumLockIndicator(
            font="{font} Italic Bold",
            fontsize=12,
            padding=8,
            foreground=colors.text,
            background=colors.color4,
        ),

        widget.TextBox(
            font=f'{font}',
            text=icon_right,
            fontsize=40,
            padding=-6,
            foreground=colors.color3,
            background=colors.color4,
        ),
        widget.Clock(
            font=f'{font}',
            padding=4,
            format=" %H:%M:%S - %d/%m/%Y",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('evolution --component=calendar')
            },
            foreground=colors.text,
            background=colors.color3,
        ),

        widget.TextBox(
            font=f'{font}',
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
            font=f'{font}',
            text=icon_right,
            fontsize=40,
            padding=-6,
            foreground=colors.color1,
            background=colors.color2,
        ),
        widget.Battery(
            font=f'{font}',
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
            font=f'{font}',
            padding=8,
            metric=True,
            threshold=40,
            fmt=" {}",
            foreground="#ffff00",
            foreground_alert="#ff0000",
            background=colors.color1,
        ),
        widget.TextBox(
            font=f'{font}',
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
    font = 'FiraCode Nerd Font'
    icon_left = ""
    icon_right = ""
    widgets_list = [
        widget.TextBox(
            font=f'{font}',
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
            font=f'{font}',
            text=icon_left,
            fontsize=40,
            padding=-6,
            foreground=colors.dark,
            background=colors.grey,
        ),
        widget.GroupBox(
            font=f'{font}',
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
            font=f'{font}',
            text=icon_left,
            fontsize=40,
            padding=-6,
            foreground=colors.grey,
            background=colors.focus,
        ),
        widget.CurrentLayout(
            font=f'{font}',
            foreground=colors.light,
            background=colors.focus,
        ),
        widget.CurrentLayoutIcon(
            scale=0.7,
            padding=0,
            background=colors.focus,
        ),
        widget.TextBox(
            font=f'{font}',
            text=icon_left,
            fontsize=40,
            padding=-6,
            foreground=colors.focus,
        ),
        widget.WindowName(
            font=f'{font}',
            fontsize=12,
            foreground=colors.focus,
        ),
        widget.TextBox(
            font=f'{font}',
            text=icon_right,
            fontsize=40,
            padding=-6,
            foreground=colors.color4,
        ),
        widget.CapsNumLockIndicator(
            font="{font} Italic Bold",
            fontsize=10,
            foreground=colors.text,
            background=colors.color4,
        ),

        widget.TextBox(
            font=f'{font}',
            text=icon_right,
            fontsize=40,
            padding=-6,
            foreground=colors.color3,
            background=colors.color4,
        ),
        widget.Clock(
            font=f'{font}',
            format=" %H:%M:%S %d/%m/%Y",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('evolution --component=calendar')
            },
            foreground=colors.text,
            background=colors.color3,
        ),
        widget.TextBox(
            font=f'{font}',
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
            font=f'{font}',
            text=icon_right,
            fontsize=40,
            padding=-6,
            foreground=colors.color1,
            background=colors.color2,
        ),
        widget.Net(
            font=f'{font}',
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
            font=f'{font}',
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
            font=f'{font}',
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
            font=f'{font}',
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
            font=f'{font}',
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
    font = 'FiraCode Nerd Font'
    icon_left = ""
    icon_right = ""
    widgets_list = [
        widget.TextBox(
            font=f'{font}',
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
            font=f'{font}',
            text=icon_left,
            fontsize=38,
            margin=0,
            padding=-5,
            foreground=colors.dark,
            background=colors.grey,
        ),
        widget.GroupBox(
            font=f'{font}',
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
            font=f'{font}',
            text=icon_left,
            fontsize=38,
            margin=0,
            padding=-5,
            foreground=colors.grey,
            background=colors.focus,
        ),
        widget.CurrentLayout(
            font=f'{font}',
            foreground=colors.light,
            background=colors.focus,
        ),
        widget.CurrentLayoutIcon(
            scale=0.7,
            padding=0,
            background=colors.focus,
        ),
        widget.TextBox(
            font=f'{font}',
            text=icon_left,
            fontsize=38,
            margin=0,
            padding=-5,
            foreground=colors.focus,
        ),
        widget.WindowName(
            font=f'{font}',
            fontsize=12,
            max_chars=32,
            formant='{name}',
            foreground=colors.focus,
        ),
        widget.TextBox(
            font=f'{font}',
            text=icon_right,
            fontsize=38,
            margin=0,
            padding=-5,
            foreground=colors.color4,
        ),
        widget.CapsNumLockIndicator(
            font=f"{font} Italic Bold",
            fontsize=10,
            foreground=colors.text,
            background=colors.color4,
        ),

        widget.TextBox(
            font=f'{font}',
            text=icon_right,
            fontsize=38,
            margin=0,
            padding=-5,
            foreground=colors.color3,
            background=colors.color4,
        ),
        widget.Clock(
            font=f'{font}',
            format="%d %b, %H.%M",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('evolution --component=calendar')
            },
            foreground=colors.text,
            background=colors.color3,
        ),
        widget.TextBox(
            font=f'{font}',
            text=icon_right,
            fontsize=38,
            margin=0,
            padding=-5,
            foreground=colors.color2,
            background=colors.color3,
        ),
        widget.Net(
            font=f'{font}',
            format='Net:{down} \uf545\uf55d {up}',
            padding=4,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn('nm-connection-editor'),
            },
            foreground=colors.text,
            background=colors.color2,
        ),
        widget.Volume(
            font=f'{font}',
            fmt="Vol: {}",
            padding=4,
            foreground=colors.text,
            background=colors.color2,
        ),
        widget.TextBox(
            font=f'{font}',
            text=icon_right,
            fontsize=38,
            margin=0,
            padding=-5,
            foreground=colors.color1,
            background=colors.color2,
        ),
        widget.Systray(
            font=f'{font}',
            icon_size=22,
            margin=8,
            padding=8,
            background=colors.color1,
        ),
        widget.Battery(
            font=f'{font}',
            format="Bat:{percent:2.0%}",
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
    font = 'Monofurbold Nerd Font'
    widgets_list = [
        widget.GroupBox(
            font=f'{font}',
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
            font=f'{font}',
            margin=4,
            padding=4,
            foreground=colors.focus,
        ),
        widget.Sep(
            padding=8, margin=8,
            foreground=colors.color2,
            size_percent=50,
        ),
        widget.WindowName(
            max_chars=50,
            font=f'{font}',
            formant='{name}',
            margin=4,
            padding=4,
            foreground=colors.focus,
        ),
        widget.CapsNumLockIndicator(
            fmt="[{}]",
            font=f'{font}',
            fontsize=12,
            margin=4,
            padding=4,
            foreground=colors.color4,
        ),

        widget.Clock(
            format="[%c]",
            font=f'{font}',
            margin=4,
            padding=4,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('evolution --component=calendar')
            },
            foreground=colors.color3,
        ),
        widget.Net(
            format='[Up: {up} Down: {down}',
            font=f'{font}',
            margin=4,
            padding=4,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn('nm-connection-editor'),
            },
            foreground=colors.color2,
        ),
        widget.Sep(
            padding=8, margin=8,
            foreground=colors.color2,
            size_percent=30,
        ),
        widget.Volume(
            fmt="Vol: {}]",
            font=f'{font}',
            margin=4,
            padding=4,
            foreground=colors.color2,
        ),
        widget.Battery(
            format="[Bat: {percent:2.0%}]",
            font=f'{font}',
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
            icon_size=18,
        ),
    ]
    return widgets_list
