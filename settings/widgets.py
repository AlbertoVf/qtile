from libqtile import qtile, widget
import os
import socket
from settings.shortcut import terminal, colors
from settings.path import *

font='FantasqueSansMono NF'
# font = 'Monofurbold NF'  # nerd fonts https://www.nerdfonts.com/cheat-sheet
icon_left = ""
icon_right = ""

widget_defaults = dict(font=font, fontsize=12, padding=4,foreground=colors.light, background=colors.dark)

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


def indicator(tx="{}", size=12, style=f'{font}', pad=8, mg=8, fg=colors.text, bg=colors.color4):
    return widget.CapsNumLockIndicator(
        fmt=tx,
        fontsize=size,
        font=style,
        padding=pad,
        margin=mg,
        foreground=fg,
        background=bg,
    )


def separator(tx="", fg=colors.dark, bg=colors.dark):
    return widget.TextBox(
        font='FiraCode Nerd Font',
        text=tx,
        fontsize=40,
        padding=-6,
        foreground=fg,
        background=bg,
    )


def systray(size=22, bg=colors.dark):
    return widget.Systray(
        icon_size=size,
        margin=4,
        padding=8,
        background=bg,
    )


def groupbox(fontsize=14, border=0, highlight_method="text", bg=colors.dark):
    return widget.GroupBox(
        fontsize=fontsize,
        margin=4,
        padding=8,
        borderwidth=border,
        disable_drag=True,
        rounded=False,
        highlight_method=highlight_method,
        active=colors.active,
        inactive=colors.inactive,
        highlight_color=colors.grey,
        this_current_screen_border=colors.focus,
        this_screen_border=colors.grey,
        other_current_screen_border=colors.active,
        other_screen_border=colors.inactive,
        background=bg,
    )


def menu(fg=colors.color3, bg=colors.dark, size=22):
    return widget.TextBox(
        text="",
        fontsize=size,
        padding=16,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn('rofi -show run'),
            "Button3": lambda: qtile.cmd_spawn('xfce4-appfinder'),
        },
        background=bg,
        foreground=fg,
    ),


def init_widgets_list0():

    widgets_list = [
        menu(),
        separator(tx=icon_left, fg=colors.dark, bg=colors.grey),

        groupbox(fontsize=18, border=0,
                 highlight_method="text", bg=colors.grey),
        separator(tx=icon_left, fg=colors.grey, bg=colors.focus),

        widget.CurrentLayout(
            foreground=colors.light,
            background=colors.focus,
        ),
        widget.CurrentLayoutIcon(
            scale=0.7,
            padding=0,
            background=colors.focus,
        ),
        separator(tx=icon_left, fg=colors.focus),

        widget.WindowName(
            fontsize=12,
            foreground=colors.focus,
        ),

        separator(tx=icon_right, fg=colors.color4),
        indicator(),

        separator(tx=icon_right, fg=colors.text, bg=colors.colors4),
        widget.Clock(
            padding=4,
            format=" %H:%M:%S - %d/%m/%Y",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('evolution --component=calendar')
            },
            foreground=colors.text,
            background=colors.color3,
        ),

        separator(tx=icon_right, fg=colors.color2, bg=colors.color3),
        systray(bg=colors.color2),

        separator(tx=icon_right, fg=colors.color1, bg=colors.color2),
        widget.Battery(
            fontsize=16,
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
            fontsize=16,
            padding=8,
            metric=True,
            threshold=40,
            fmt=" {}",
            foreground="#ffff00",
            foreground_alert="#ff0000",
            background=colors.color1,
        ),
        widget.TextBox(
            fontsize=16,
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
    widgets_list = [
        menu(),
        separator(tx=icon_left, fg=colors.dark, bg=colors.grey),
        groupbox(fontsize=18, highlight_method="text"),
        separator(tx=icon_left, fg=colors.grey, bg=colors.focus),

        widget.CurrentLayout(
            foreground=colors.light,
            background=colors.focus,
        ),
        widget.CurrentLayoutIcon(
            scale=0.7,
            padding=0,
            background=colors.focus,
        ),
        separator(tx=icon_left, fg=colors.focus),

        widget.WindowName(
            fontsize=12,
            max_chars=32,
            formant='{name}',
            foreground=colors.focus,
        ),

        separator(tx=icon_right, fg=colors.color4),
        indicator(),

        separator(tx=icon_right, fg=colors.color3, bg=colors.color4),

        widget.Clock(
            padding=4,
            format="%d %b, %H.%M",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('evolution --component=calendar')
            },
            foreground=colors.text,
            background=colors.color3,
        ),
        separator(tx=icon_right, fg=colors.color2, bg=colors.color3),
        widget.Net(
            format='Net:{down} \uf545\uf55d {up}',
            padding=4,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn('nm-connection-editor'),
            },
            foreground=colors.text,
            background=colors.color2,
        ),
        widget.Volume(
            fmt="Vol: {}",
            padding=4,
            foreground=colors.text,
            background=colors.color2,
        ),

        separator(tx=icon_right, fg=colors.color1, bg=colors.color2),
        systray(bg=colors.color1),
        widget.Battery(
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


def init_widgets_list2():
    widgets_list = [
        groupbox(fontsize=14, highlight_method="text"),
        widget.Sep(padding=8, margin=8,
                   foreground=colors.grey, size_percent=50,),
        widget.CurrentLayout(
            margin=4,
            padding=4,
            foreground=colors.focus,
        ),
        widget.Sep(padding=8, margin=8,
                   foreground=colors.grey, size_percent=50,),
        widget.WindowName(
            max_chars=50,
            formant='{name}',
            margin=4,
            padding=4,
            foreground=colors.focus,
        ),

        indicator(tx="[{}]", fg=colors.color4, bg=colors.dark),

        widget.Clock(
            padding=4,
            format="[%c]",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('evolution --component=calendar')
            },
            foreground=colors.color3,
            background=colors.dark,
        ),
        widget.Net(
            format='[Up: {up} Down: {down}',
            margin=4,
            padding=4,
            mouse_callbacks={
                'Button3': lambda: qtile.cmd_spawn('nm-connection-editor'),
            },
            foreground=colors.color2,
        ),
        widget.Sep(padding=8, margin=8,
                   foreground=colors.color2, size_percent=30,),
        widget.Volume(
            fmt="Vol: {}]",
            margin=4,
            padding=4,
            foreground=colors.color2,
        ),

        widget.Battery(
            format="[Bat: {percent:2.0%}]",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn('xfce4-power-manager-settings'),
                'Button3': lambda: qtile.cmd_spawn('xfce4-taskmanager'),
                'Button2': lambda: qtile.cmd_spawn(terminal + ' -e htop'),
            },
            margin=4,
            padding=4,
            update_interval=10,
            foreground=colors.color1,
        ),
        systray(size=18),
    ]
    return widgets_list

def init_widgets_list01():
    widgets_list=[
        groupbox(fontsize=14, highlight_method="text"),
        widget.Sep(padding=8, margin=8,
                   foreground=colors.grey, size_percent=50,),
        widget.CurrentLayout(
            margin=4,
            padding=4,
            foreground=colors.focus,
        ),
        widget.Sep(padding=8, margin=8,
                   foreground=colors.grey, size_percent=50,),
        widget.WindowName(
            max_chars=50,
            formant='{name}',
            margin=4,
            padding=4,
            foreground=colors.focus,
        ),
    ]
    return widgets_list
