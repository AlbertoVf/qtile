# Copyright (c) 2010 Aldo Cortesi Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes Copyright (c) 2013 horsik  Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import re
import socket
import subprocess
from libqtile.config import Drag, Key, Screen, Group, Drag, Click, Rule
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer

from settings.themes import *
from settings.path import *
from settings.callbacks import *


colors = Colors()
temperature = ["#00ff00", "#ffff00", "#ff0000"]

# mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"


dgroups_key_binder = None
dgroups_app_rules = []

main = None
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
auto_fullscreen = True
# focus_on_window_activation = "smart"
focus_on_window_activation = "focus"
wmname = "LG3D"


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([qtile_scripts + "/autostart.sh"])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for() or window.window.get_wm_type() in floating_types):
        window.floating = True


def init_widgets_defaults():
    return dict(
        font="FiraCode Nerd Font",
        fontsize=16,
        padding=8,
        background=colors.dark,
        foreground=colors.light,
    )


icon_left = ""
icon_right = ""


def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
        widget.TextBox(
            text="",
            fontsize=22,
            padding=16,
            mouse_callbacks={"Button3": mouse_app_finder,
                             "Button1": mouse_rofi},
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
            font="FiraCode Nerd Font Italic Bold",
            fontsize=10,
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
            mouse_callbacks={"Button1": mouse_calendar},
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
            mouse_callbacks={"Button1": mouse_power_manager},
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
            foreground=temperature[1],
            foreground_alert=temperature[2],
            background=colors.color1,
        ),
        widget.TextBox(
            text="⏻",
            fontsize=20,
            mouse_callbacks={"Button1": mouse_logout},
            foreground=colors.text,
            background=colors.color1,
        ),
    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2


def init_screens():
    return [
        Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=24)),
        Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=24)),
    ]


def init_layout_theme():
    return {
        "margin": 8,
        "border_width": 2,
        "border_focus": colors.focus,
        "border_normal": colors.grey,
    }


mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
]

keys = [
    # FUNCTION KEYS
    Key([], "F12", lazy.spawn("xfce4-terminal --drop-down")),
    # SUPER + FUNCTION KEYS
    Key([mod], "a", lazy.spawn("android-studio")),
    Key([mod], "b", lazy.spawn("bitwarden-desktop")),
    Key([mod], "c", lazy.spawn("code-oss")),
    Key([mod], "d", lazy.spawn("drawio")),
    Key([mod], "e", lazy.spawn("evolution")),
    Key([mod], "f", lazy.spawn("firefox")),
    Key([mod], "g", lazy.spawn("gparted")),
    # Key([mod], "h", lazy.spawn('')),
    Key([mod], "i", lazy.spawn("idea")),
    # Key([mod], "j", lazy.spawn('')),
    Key([mod], "k", lazy.spawn("krita")),
    # Key([mod], "l", lazy.spawn('')),
    Key([mod], "m", lazy.spawn("pragha")),
    # Key([mod], "n", lazy.spawn('')),
    Key([mod], "o", lazy.spawn("obs")),
    Key([mod], "p", lazy.spawn("pycharm")),
    Key([mod], "q", lazy.window.kill()),
    # Key([mod], "r", lazy.spawn('')),
    Key([mod], "s", lazy.spawn("pamac-manager")),
    Key([mod], "t", lazy.spawn("timeshift")),
    # Key([mod], "u", lazy.spawn('')),
    Key([mod], "v", lazy.spawn("vlc --video-on-top")),
    # Key([mod], "w", lazy.spawn('')),
    Key([mod], "x", lazy.spawn("arcolinux-logout")),
    # Key([mod], "y", lazy.spawn('')),
    # Key([mod], "z", lazy.spawn('')),
    # Key([mod], "c", lazy.spawn('conky-toggle')),
    # Key([mod], "f", lazy.window.toggle_fullscreen()),
    # Key([mod], "v", lazy.spawn('pavucontrol')),
    Key([mod], "Escape", lazy.spawn("xkill")),
    Key([mod], "Return", lazy.spawn("termite")),
    # Key([mod], "KP_Enter", lazy.spawn('termite')),
    Key([mod], "KP_Enter", lazy.spawn("gnome-calculator")),
    Key([mod], "F1", lazy.spawn("firefox")),
    Key([mod], "F2", lazy.spawn("code-oss")),
    Key([mod], "F3", lazy.spawn("inkscape")),
    Key([mod], "F4", lazy.spawn("gimp")),
    Key([mod], "F5", lazy.spawn("meld")),
    Key([mod], "F6", lazy.spawn("vlc --video-on-top")),
    Key([mod], "F7", lazy.spawn("virtualbox")),
    Key([mod], "F8", lazy.spawn("thunar")),
    Key([mod], "F9", lazy.spawn("evolution")),
    Key([mod], "F10", lazy.spawn("spotify")),
    Key([mod], "F11", lazy.spawn("rofi -show run -fullscreen")),
    Key([mod], "F12", lazy.spawn("rofi -show run")),
    # SUPER + SHIFT KEYS
    Key([mod, "shift"], "Return", lazy.spawn("thunar")),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "shift"], "x", lazy.shutdown()),
    # CONTROL + ALT KEYS
    Key(["mod1", "control"], "Next", lazy.spawn("conky-rotate -n")),
    Key(["mod1", "control"], "Prior", lazy.spawn("conky-rotate -p")),
    Key(["mod1", "control"], "a", lazy.spawn("xfce4-appfinder")),
    Key(["mod1", "control"], "b", lazy.spawn("polo")),
    Key(["mod1", "control"], "c", lazy.spawn("catfish")),
    Key(["mod1", "control"], "e", lazy.spawn("arcolinux-tweak-tool")),
    Key(["mod1", "control"], "f", lazy.spawn("firefox")),
    Key(["mod1", "control"], "g", lazy.spawn(
        "chromium -no-default-browser-check")),
    # Key(["mod1", "control"], "h", lazy.spawn('')),
    Key(["mod1", "control"], "i", lazy.spawn("nitrogen")),
    # Key(["mod1", "control"], "j", lazy.spawn('')),
    Key(["mod1", "control"], "k", lazy.spawn("arcolinux-logout")),
    # Key(["mod1", "control"], "l", lazy.spawn('')),
    Key(["mod1", "control"], "m", lazy.spawn("xfce4-settings-manager")),
    # Key(["mod1", "control"], "n", lazy.spawn('')),
    Key(["mod1", "control"], "o", lazy.spawn(
        qtile_scripts + "/picom-toggle.sh")),
    Key(["mod1", "control"], "p", lazy.spawn("pamac-manager")),
    # Key(["mod1", "control"], "q", lazy.spawn('')),
    Key(["mod1", "control"], "r", lazy.spawn("rofi-theme-selector")),
    Key(["mod1", "control"], "s", lazy.spawn("spotify")),
    Key(["mod1", "control"], "t", lazy.spawn("termite")),
    Key(["mod1", "control"], "u", lazy.spawn("pavucontrol")),
    Key(["mod1", "control"], "v", lazy.spawn("vivaldi-stable")),
    Key(["mod1", "control"], "w", lazy.spawn("arcolinux-welcome-app")),
    Key(["mod1", "control"], "x", lazy.spawn("arcolinux-logout")),
    # Key(["mod1", "control"], "y", lazy.spawn('')),
    # Key(["mod1", "control"], "z", lazy.spawn('')),
    Key(["mod1", "control"], "Return", lazy.spawn("termite")),
    # ALT + ... KEYS
    Key(["mod1"], "f", lazy.spawn("variety -f")),
    Key(["mod1"], "h", lazy.spawn("urxvt -e htop")),
    Key(["mod1"], "n", lazy.spawn("variety -n")),
    Key(["mod1"], "p", lazy.spawn("variety -p")),
    Key(["mod1"], "t", lazy.spawn("variety -t")),
    Key(["mod1"], "Up", lazy.spawn("variety --pause")),
    Key(["mod1"], "Down", lazy.spawn("variety --resume")),
    Key(["mod1"], "Left", lazy.spawn("variety -p")),
    Key(["mod1"], "Right", lazy.spawn("variety -n")),
    Key(["mod1"], "F2", lazy.spawn("gmrun")),
    Key(["mod1"], "F3", lazy.spawn("xfce4-appfinder")),
    # VARIETY KEYS WITH PYWAL
    Key(["mod1", "shift"], "f", lazy.spawn(
        qtile_scripts + "/set-pywal.sh -f")),
    Key(["mod1", "shift"], "p", lazy.spawn(
        qtile_scripts + "/set-pywal.sh -p")),
    Key(["mod1", "shift"], "n", lazy.spawn(
        qtile_scripts + "/set-pywal.sh -n")),
    Key(["mod1", "shift"], "u", lazy.spawn(
        qtile_scripts + "/set-pywal.sh -u")),
    # CONTROL + SHIFT KEYS
    Key([mod2, "shift"], "Escape", lazy.spawn("xfce4-taskmanager")),
    # SCREENSHOTS
    Key([], "Print",
        lazy.spawn(
        "scrot 'screenshot_%Y%m%d_%H%M%S.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'"),
        ),
    Key([mod2], "Print", lazy.spawn("xfce4-screenshooter")),
    Key([mod2, "shift"], "Print", lazy.spawn("gnome-screenshot -i")),
    # MULTIMEDIA KEYS
    # INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),
    # INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    # QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),
    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),
    # TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    # CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    # RESIZE UP, DOWN, LEFT, RIGHT
    Key(
        [mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
    Key(
        [mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),

    # FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        lazy.layout.swap_left()
        ),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        lazy.layout.swap_right()
        ),
    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left",
        lazy.layout.swap_left(),
        lazy.layout.shuffle_left()
        ),
    Key([mod, "shift"], "Right",
        lazy.layout.swap_right(),
        lazy.layout.shuffle_right()
        ),

]

#
# GROUPS
# nerd fonts https://www.nerdfonts.com/cheat-sheet
groups = []  # web - developer - terminal - mail - settings - files - music - video - pictures - games
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# group_labels = ["\uf8a4", "\uf8a7", "\uf8aa", "\uf8ad","\uf8b0", "\uf8b3", "\uf8b6", "\uf8b9", "\uf8bc", "\uf8a1"]
group_labels = ["", "", "ﲵ", "", "漣", "", "ﱘ", "", "", ""]
# group_labels = ["WWW", "DEV", "TER", "MSG","SET", "DOC", "MUS", "VID", "IMG", "GAM"]
for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            label=group_labels[i],
        )
    )

for i in groups:
    keys.extend(
        [
            # CHANGE WORKSPACES
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod], "Tab", lazy.screen.next_group()),
            Key(["mod1"], "Tab", lazy.screen.next_group()),
            Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        ]
    )


#
# WIDGETS FOR THE BAR
#
widget_defaults = init_widgets_defaults()
widgets_list = init_widgets_list()
widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()

screens = init_screens()


#
# LAYOUTS
#
layout_theme = init_layout_theme()
layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.VerticalTile(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Max(**layout_theme),
    layout.TreeTab(
        font="FiraCode Nerd Font",
        sections=["FIRST", "SECOND"],
        fontsize=12,
        section_fontsize=14,
        padding_y=5,
        section_top=10,
        panel_width=320,
        bg_color=colors.dark,
        active_bg=colors.focus,
        active_fg=colors.text,
        inactive_bg=colors.grey,
        inactive_fg=colors.inactive,
    ),
]
floating_types = ["notification", "toolbar", "splash", "dialog"]

floating_layout = layout.Floating(
    float_rules=[
        {"wmclass": "Arcolinux-welcome-app.py"},
        {"wmclass": "Arcolinux-tweak-tool.py"},
        {"wmclass": "confirm"},
        {"wmclass": "dialog"},
        {"wmclass": "download"},
        {"wmclass": "error"},
        {"wmclass": "file_progress"},
        {"wmclass": "notification"},
        {"wmclass": "splash"},
        {"wmclass": "toolbar"},
        {"wmclass": "confirmreset"},
        {"wmclass": "makebranch"},
        {"wmclass": "maketag"},
        {"wmclass": "Arandr"},
        {"wmclass": "feh"},
        {"wmclass": "Galculator"},
        {"wmclass": "arcolinux-logout"},
        {"wmclass": "xfce4-terminal"},
        {"wname": "branchdialog"},
        {"wname": "Open File"},
        {"wname": "pinentry"},
        {"wmclass": "ssh-askpass"},
    ],
    fullscreen_border_width=0,
    border_width=1,
    border_normal=colors.grey,
    border_focus=colors.focus,
)
