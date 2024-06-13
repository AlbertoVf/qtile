from libqtile.config import Key, Click, Drag
from libqtile.lazy import lazy
from .screen import groups

mod = "mod4"  # mod4 or mod = super key

keys = [
    # QTILE CONFIGURATION
    Key([mod], "q", lazy.window.kill(), desc="Kill the focused window"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill the focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Close session"),
    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen(), desc="show next screen"),
    Key([mod], "comma", lazy.prev_screen(), desc="show previous screen"),
    Key([mod], "space", lazy.next_layout(), desc="change layout"),
    # CHANGE FOCUS
    Key([mod], "k", lazy.layout.up(), desc="change focus to up window"),
    Key([mod], "Up", lazy.layout.up(), desc="change focus to up window"),
    Key([mod], "j", lazy.layout.down(), desc="change focus to down window"),
    Key([mod], "Down", lazy.layout.down(), desc="change focus to down window"),
    Key([mod], "h", lazy.layout.left(), desc="change focus to left window"),
    Key([mod], "Left", lazy.layout.left(), desc="change focus to left window"),
    Key([mod], "l", lazy.layout.right(), desc="change focus to right window"),
    Key([mod], "Right", lazy.layout.right(), desc="change focus to right window"),
    # # WINDOWS STATE
    Key([mod, "shift"], "m", lazy.layout.maximize(), desc='window is maximized'),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc='make fullscreen window'),
    Key([mod, "shift"], "n", lazy.layout.normalize(), lazy.layout.reset(), desc="Reset window size"),
    Key([mod, "shift"], "space", lazy.layout.flip(), lazy.layout.toggle_split(), desc="Change flip orientation"),
    Key([mod, "control"], "f", lazy.window.toggle_floating(), desc='make float window'),

    # monadtall / monadwide / bsp / max
    # windows position
    Key([mod, "shift"], "h", lazy.layout.swap_left(), lazy.layout.shuffle_left(), lazy.layout.flip_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right(), lazy.layout.shuffle_right(), lazy.layout.flip_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), lazy.layout.flip_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), lazy.layout.flip_up()),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), lazy.layout.flip_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), lazy.layout.flip_down()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right(), lazy.layout.shuffle_right(), lazy.layout.flip_right()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left(), lazy.layout.shuffle_left(), lazy.layout.flip_left()),
    # windows size
    Key([mod,"control"], "Up", lazy.layout.grow(), lazy.layout.grow_up(),lazy.layout.grow_main()),
    Key([mod,"control"], "Down", lazy.layout.shrink(), lazy.layout.grow_down(),lazy.layout.shrink_main()),
    Key([mod,"control"], "Right", lazy.layout.grow(), lazy.layout.grow_right(),lazy.layout.grow_main()),
    Key([mod,"control"], "Left", lazy.layout.shrink(), lazy.layout.grow_left(),lazy.layout.shrink_main()),
    # CHANGE WORKSPACE
    Key([mod], "Tab", lazy.screen.next_group()),
    Key([mod, "shift"], "Tab", lazy.screen.prev_group())
]

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        ]
    )

mouse = [
    Click([mod], "Button1", lazy.window.bring_to_front()),
    Drag([mod], "Button2", lazy.window.set_position_floating(), start=lazy.window.get_position(), ),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size(), ),
]
