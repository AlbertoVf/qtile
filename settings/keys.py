from libqtile.config import Key, Click, Drag
from libqtile.lazy import lazy
from settings.screen import groups

modkey = mod = "mod4"  # mod4 or mod = super key


class KEYCODE:
    Up       = "Up" # "k"
    Down     = "Down"  # "j"
    Left     = "Left"  # "h"
    Right    = "Right"  # "l"
    position = [mod, "shift"]
    size     = [mod, "control"]
    flip     = [mod, "mod1"]  # mod + alt


configuration_keys = [
    Key(["control"], "q", lazy.window.kill(), desc="Kill the focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Close session"),
    Key(KEYCODE.size, "F11", lazy.hide_show_bar("top")),
]

screen_keys = [
    Key([mod], "Next", lazy.screen.next_group(), desc="change to next workspace/group"),
    Key([mod], "Prior", lazy.screen.prev_group(), desc="change to previous workspace/group"),
    Key([mod], "End", lazy.function(lambda qtile: qtile.groups[-1].toscreen()), desc="change to last workspace/group"),
    Key([mod], "Home", lazy.function(lambda qtile: qtile.groups[0].toscreen()), desc="change to first workspace/group"),
    Key([mod], "Tab", lazy.screen.toggle_group(), desc='Change to last used group'),

    Key([mod], "space", lazy.next_layout(), desc="change layout"),
    Key(KEYCODE.position, "space", lazy.prev_layout(), desc="change layout"),

    Key([mod], KEYCODE.Up, lazy.layout.up(), desc="change focus to up window"),
    Key([mod], KEYCODE.Down, lazy.layout.down(), desc="change focus to down window"),
    Key([mod], KEYCODE.Right, lazy.layout.right(), desc="change focus to right window"),
    Key([mod], KEYCODE.Left, lazy.layout.left(), desc="change focus to left window"),
]

window_position_keys = [
    Key(KEYCODE.position, KEYCODE.Up, lazy.layout.shuffle_up(), desc="Move focused window Up", ),
    Key(KEYCODE.position, KEYCODE.Down, lazy.layout.shuffle_down(), desc="Move focused window Down", ),
    Key(KEYCODE.position, KEYCODE.Left, lazy.layout.swap_left(), lazy.layout.shuffle_left().when(layout="bsp"), desc="Move focused window to Left", ),
    Key(KEYCODE.position, KEYCODE.Right, lazy.layout.swap_right(), lazy.layout.shuffle_right().when(layout="bsp"), desc="Move focused window to Right", ),
    Key(KEYCODE.flip, "comma", lazy.layout.flip(), lazy.layout.toggle_split().when(layout="bsp"), desc="Change flip orientation. Main section", ),
    Key(KEYCODE.flip, KEYCODE.Up, lazy.layout.flip_up()),
    Key(KEYCODE.flip, KEYCODE.Down, lazy.layout.flip_down()),
    Key(KEYCODE.flip, KEYCODE.Left, lazy.layout.flip_left()),
    Key(KEYCODE.flip, KEYCODE.Right, lazy.layout.flip_right()),

    Key(KEYCODE.position, "f", lazy.window.toggle_floating(), desc="make float window"),
    Key(KEYCODE.flip, "f", lazy.layout.bring_to_front(), desc="window is maximized" ),
]

window_size_keys = [
    Key(KEYCODE.size, "m", lazy.layout.maximize(), desc="window is maximized"),
    Key([mod], "period", lazy.layout.normalize(), desc="Reset secondary windows size", ),
    Key(KEYCODE.size, "period", lazy.layout.reset(), desc="reset all window size"),

    Key(KEYCODE.size, "comma", lazy.layout.grow_main().when(layout="monadtall"), lazy.layout.grow_main().when(layout="monadwide"), lazy.layout.grow_main().when(layout="spiral"), desc="increase size", ),
    Key(KEYCODE.size, "minus", lazy.layout.shrink_main().when(layout="monadtall"), lazy.layout.shrink_main().when(layout="monadwide"), lazy.layout.shrink_main().when(layout="spiral"), desc="decrease size", ),
    Key(KEYCODE.size, KEYCODE.Up, lazy.layout.grow().when(layout="monadtall"), lazy.layout.grow().when(layout="monadwide"), lazy.layout.decrease_ratio().when(layout="spiral"), lazy.layout.grow_up().when(layout="bsp"), desc="Increase focused window size", ),
    Key(KEYCODE.size, KEYCODE.Down, lazy.layout.shrink().when(layout="monadtall"), lazy.layout.shrink().when(layout="monadwide"), lazy.layout.increase_ratio().when(layout="spiral"), lazy.layout.grow_down().when(layout="bsp"), desc="Decrease focused window size", ),
    Key(KEYCODE.size, KEYCODE.Left, lazy.layout.shrink().when(layout="monadtall"), lazy.layout.shrink().when(layout="monadwide"), lazy.layout.increase_ratio().when(layout="spiral"), lazy.layout.grow_left().when(layout="bsp"), desc="Decrease focused window size", ),
    Key(KEYCODE.size, KEYCODE.Right, lazy.layout.grow().when(layout="monadtall"), lazy.layout.grow().when(layout="monadwide"), lazy.layout.decrease_ratio().when(layout="spiral"), lazy.layout.grow_right().when(layout="bsp"), desc="Increase focused window size", ),
]

keys = configuration_keys + screen_keys + window_position_keys + window_size_keys

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        ]
    )

mouse = [
    Click([mod], "Button1", lazy.window.bring_to_front()),
    Drag([mod], "Button2", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size())
]
