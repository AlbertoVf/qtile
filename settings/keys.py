from libqtile.config import Key, KeyChord, Click, Drag
from libqtile.command import lazy
from settings.screen import groups
from settings.manager import editor, terminal, fileManager, browser, mail

mod = "mod4"  # mod4 or mod = super key
keys = [
    # SUPER + FUNCTION KEYS
    Key([mod], "q", lazy.window.kill(), desc='Kill the focused window'),
    # SUPER + SHIFT KEYS
    Key([mod, "shift"], "q", lazy.window.kill(), desc='Kill the focused window'),
    # SUPER + CONTROL KEYS
    Key([mod, "control"], "r", lazy.restart(), desc='restart qtile'),
    Key([mod, "control"], "q", lazy.shutdown(), desc='Close session'),
    Key([mod, "control"], "Return", lazy.spawn(fileManager)),

    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),
    Key([mod], "space", lazy.next_layout()),
    # CHANGE FOCUS
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "Right", lazy.layout.right()),
    # WINDOWS STATE
    # Key([mod, "shift"], "n", lazy.layout.normalize()),
    Key([mod, "shift"], "m", lazy.layout.maximize()),
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    Key([mod, "shift"], "space", lazy.layout.flip(), lazy.layout.toggle_split()),

    # MOVE WINDOW
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.swap_down(),
        lazy.layout.flip_down(),
        ),
    Key([mod, "shift"], "Down",
        lazy.layout.shuffle_down(),
        lazy.layout.swap_down(),
        lazy.layout.flip_down(),
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.swap_up(),
        lazy.layout.flip_up(),
        ),
    Key([mod, "shift"], "Up",
        lazy.layout.shuffle_up(),
        lazy.layout.swap_up(),
        lazy.layout.flip_up(),
        ),
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        lazy.layout.swap_left(),
        lazy.layout.swap_column_left(),
        lazy.layout.flip_left(),
        ),
    Key([mod, "shift"], "Left",
        lazy.layout.shuffle_left(),
        lazy.layout.swap_left(),
        lazy.layout.swap_column_left(),
        lazy.layout.flip_left(),
        ),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        lazy.layout.swap_right(),
        lazy.layout.swap_column_right(),
        lazy.layout.flip_right(),
        ),
    Key([mod, "shift"], "Right",
        lazy.layout.shuffle_right(),
        lazy.layout.swap_right(),
        lazy.layout.swap_column_right(),
        lazy.layout.flip_right(),
        ),
    # SIZE WINDOWS
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        lazy.layout.section_down(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        lazy.layout.section_down(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        lazy.layout.section_up(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        lazy.layout.section_up(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
]

for i in groups:
    keys.extend([
        # CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift"], "Tab", lazy.screen.prev_group()),

        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

mouse = [
    Click(["mod"], "Button1", lazy.window.bring_to_front(), ),
    Drag(["mod"], "Button2", lazy.window.set_position_floating(),
         start=lazy.window.get_position(), ),
    Drag(["mod"], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
]
