from libqtile.config import Key, Click, Drag
from libqtile.lazy import lazy
from settings.screen import groups

mod = "mod4"  # mod4 or mod = super key

configuration_keys = [
    Key([mod], "q", lazy.window.kill(), desc="Kill the focused window"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill the focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Close session"),
]
screen_keys = [
    Key([mod], "period", lazy.next_screen(), desc="show next screen"),
    Key([mod], "comma", lazy.prev_screen(), desc="show previous screen"),
    Key([mod], "space", lazy.next_layout(), desc="change layout"),
    Key([mod], "Tab", lazy.screen.next_group(), desc="change to next workspace/group"),
    Key([mod, "shift"], "space", lazy.prev_layout(), desc="change layout"),
    Key([mod, "shift"], "Tab", lazy.screen.prev_group(), desc="change to previous workspace/group", ),
    Key([mod], "Up", lazy.layout.up(), desc="change focus to up window"),
    Key([mod], "Down", lazy.layout.down(), desc="change focus to down window"),
    Key([mod], "Right", lazy.layout.right(), lazy.layout.up().when(layout="spiral"), desc="change focus to right window", ),
    Key([mod], "Left", lazy.layout.left(), lazy.layout.down().when(layout="spiral"), desc="change focus to left window", ),
    Key([mod, "shift"], "m", lazy.layout.maximize(), desc="window is maximized"),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc="make fullscreen window", ),
    Key([mod, "shift"], "n", lazy.layout.reset(), lazy.layout.normalize(), desc="Reset window size", ),
    Key([mod, "control"], "space", lazy.layout.flip(), lazy.layout.toggle_split(), desc="Change flip orientation. Main section", ),
    Key([mod, "control"], "f", lazy.window.toggle_floating(), desc="make float window"),
]
window_position_keys=[
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up().when(layout="monadwide"), lazy.layout.shuffle_up().when(layout="spiral"), lazy.layout.shuffle_up().when(layout="bsp"), lazy.layout.flip_up().when(layout="bsp"), desc="Move focused window Up", ),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down().when(layout="monadwide"), lazy.layout.shuffle_down().when(layout="bsp"), lazy.layout.flip_down().when(layout="bsp"), lazy.layout.shuffle_down().when(layout="spiral"), desc="Move focused window Down", ),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left().when(layout="monadtall"), lazy.layout.flip_left().when(layout="bsp"), lazy.layout.shuffle_down().when(layout="spiral"), desc="Move focused window to Left", ),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right().when(layout="monadtall"), lazy.layout.flip_right().when(layout="bsp"), lazy.layout.shuffle_up().when(layout="spiral"), desc="Move focused window to Right", ),
]
window_size_keys = [
    Key([mod, "control"], "Up", lazy.layout.grow().when(layout="monadwide"), lazy.layout.grow_up().when(layout="bsp"), desc="Increase focused window size", ),
    Key([mod, "control"], "Down", lazy.layout.shrink().when(layout="monadwide"), lazy.layout.grow_down().when(layout="bsp"), desc="Increase focused window size", ),
    Key([mod, "control"], "Left", lazy.layout.shrink().when(layout="monadtall"), lazy.layout.shrink_main().when(layout="spiral"), lazy.layout.grow_left().when(layout="bsp"), desc="Increase focused window size", ),
    Key([mod, "control"], "Right", lazy.layout.grow().when(layout="monadtall"), lazy.layout.grow_main().when(layout="spiral"), lazy.layout.grow_right().when(layout="bsp"), desc="Increase focused window size", ),
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
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
]
