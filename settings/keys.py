from libqtile.config import Key, Click, Drag
from libqtile.lazy import lazy
from settings.screen import groups

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

    # CHANGE WORKSPACE
    Key([mod], "Tab", lazy.screen.next_group(), desc="change to next workspace/group"),
    Key([mod, "shift"], "Tab", lazy.screen.prev_group(), desc="change to previous workspace/group"),

    # CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up(), desc="change focus to up window"),
    Key([mod], "Down", lazy.layout.down(), desc="change focus to down window"),
    Key([mod], "Right", lazy.layout.right(), desc="change focus to right window"),
    Key([mod], "Left", lazy.layout.left(), desc="change focus to left window"),

    # WINDOWS STATE
    Key([mod, "shift"], "m", lazy.layout.maximize(), desc='window is maximized'),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc='make fullscreen window'),
    Key([mod, "shift"], "n", lazy.layout.reset(),lazy.layout.normalize(), desc="Reset window size"),
    Key([mod, "control"], "space", lazy.layout.flip(), lazy.layout.toggle_split(), desc="Change flip orientation. Main section"),
    Key([mod, "control"], "f", lazy.window.toggle_floating(), desc='make float window'),

    # windows position [monadtall+monadwide]
    Key([mod, "shift"], "Left", lazy.layout.swap_left(), lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right(), lazy.layout.shuffle_right()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), lazy.layout.shuffle_up()),
    # window position [bsp]
    Key([mod, "control"], "j", lazy.layout.flip_down()),
    Key([mod, "control"], "k", lazy.layout.flip_up()),
    Key([mod, "control"], "l", lazy.layout.flip_right()),
    Key([mod, "control"], "h", lazy.layout.flip_left()),
    # windows size [monadtall+monadwide / bsp]
    Key([mod, "control"], "Up", lazy.layout.grow(), lazy.layout.grow_up()), # aumentar ventana con foco
    Key([mod, "control"], "Right", lazy.layout.grow(), lazy.layout.grow_right()), # aumentar ventana con foco
    Key([mod, "control"], "Down", lazy.layout.shrink(), lazy.layout.grow_down()), # disminuir ventana con foco
    Key([mod, "control"], "Left", lazy.layout.shrink(), lazy.layout.grow_left()) # disminuir ventana con foco
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
