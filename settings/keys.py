from libqtile.config import Key
from libqtile.command import lazy
from settings.shortcut import mod, mod1, editor, terminal, fileManager, browser
from settings.groups import groups

keys = [
    # SUPER + FUNCTION KEYS
    Key([mod], "b", lazy.spawn("bitwarden")),
    Key([mod], "d", lazy.spawn("drawio")),
    Key([mod], "e", lazy.spawn(editor)),
    Key([mod], "g", lazy.spawn("gparted")),
    Key([mod], "i", lazy.spawn("eclipse")),
    Key([mod], "k", lazy.spawn("krita")),
    Key([mod], "m", lazy.spawn("pragha")),
    Key([mod], "o", lazy.spawn("obs")),
    Key([mod], "p", lazy.spawn("eclipse")),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "s", lazy.spawn("pamac-manager")),
    Key([mod], "t", lazy.spawn("timeshift")),
    Key([mod], "v", lazy.spawn("vlc --video-on-top")),
    Key([mod], "x", lazy.spawn("arcolinux-logout")),
    Key([mod], "Escape", lazy.spawn("xkill")),
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "KP_Enter", lazy.spawn("gnome-calculator")),
    Key([mod], "F1", lazy.spawn(browser)),
    Key([mod], "F2", lazy.spawn(editor)),
    Key([mod], "F3", lazy.spawn("inkscape")),
    Key([mod], "F4", lazy.spawn("gimp")),
    Key([mod], "F5", lazy.spawn("meld")),
    Key([mod], "F6", lazy.spawn("vlc --video-on-top")),
    Key([mod], "F7", lazy.spawn("virtualbox")),
    Key([mod], "F8", lazy.spawn(fileManager)),
    Key([mod], "F9", lazy.spawn("evolution")),
    Key([mod], "F10", lazy.spawn("spotify")),
    Key([mod], "F11", lazy.spawn("rofi -show run -fullscreen")),
    Key([mod], "F12", lazy.spawn("rofi -show run")),
    # SUPER + SHIFT KEYS
    Key([mod, "shift"], "Return", lazy.spawn(fileManager)),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "control"], "r", lazy.restart()),
    # ALT + ... KEYS
    Key(["mod1"], "Escape", lazy.spawn("xfce4-taskmanager")),
    Key(["mod1"], "F1", lazy.spawn("rofi -show window")),
    # Key(["mod1"], "F2", lazy.spawn("ulauncher")),
    Key(["mod1"], "F2", lazy.spawn("rofi -show drun")),
    Key(["mod1"], "F3", lazy.spawn("rofi -show file-browser-extended")),
    Key(["mod1"], "F4", lazy.spawn("rofi -show ssh")),
    Key(["mod1"], "F5", lazy.spawn("rofi -show run")),
    Key(["mod1"], "Print", lazy.spawn("xfce4-screenshooter")),
    # SCREENSHOTS
    Key(
        [],
        "Print",
        lazy.spawn(
            "scrot 'screenshot_%Y%m%d_%H%M%S.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'"
        ),
    ),
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
    # Switch focus of monitors
    Key(
        [mod],
        "period",
        lazy.next_screen(),
    ),
    Key(
        [mod],
        "comma",
        lazy.prev_screen(),
    ),
    # Change Window to specific monitor
    Key([mod, "shift"], "period", lazy.to_screen(0)),
    Key([mod, "shift"], "comma", lazy.to_screen(1)),
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
        [mod, "control"],
        "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"],
        "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        lazy.layout.section_up(),
    ),
    Key(
        [mod, "control"],
        "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        lazy.layout.section_up(),
    ),
    Key(
        [mod, "control"],
        "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        lazy.layout.section_down(),
    ),
    Key(
        [mod, "control"],
        "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        lazy.layout.section_down(),
    ),
    # FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        lazy.layout.swap_right()),
    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left(),
        lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right(),
        lazy.layout.shuffle_right()),
]

for i in groups:
    keys.extend([
        # CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])
