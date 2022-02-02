from libqtile.config import Key, KeyChord
from libqtile.command import lazy
from libqtile.config import Click, Drag
from libqtile.command import lazy
from settings.screen import groups
from settings.manager import editor, terminal, fileManager, browser, mail

mod = "mod4"  # mod4 or mod = super key
keys = [
    # SUPER + FUNCTION KEYS
    Key([mod], "a", lazy.spawn("xfce4-appfinder")),
    Key([mod], "b", lazy.spawn("bitwarden-desktop")),
    Key([mod], "c", lazy.spawn("catfish")),
    Key([mod], "e", lazy.spawn(editor)),
    Key([mod], "f", lazy.spawn("firefox")),
    Key([mod], "g", lazy.spawn("gparted")),
    Key([mod], "i", lazy.spawn("idea")),
    Key([mod], "m", lazy.spawn("pragha")),
    Key([mod], "o", lazy.spawn("obs")),
    Key([mod], "p", lazy.spawn("pycharm")),
    Key([mod], "q", lazy.window.kill(), desc='Kill the focused window'),
    Key([mod], "s", lazy.spawn("pamac-manager")),
    Key([mod], "v", lazy.spawn("vlc --video-on-top")),
    Key([mod], "x", lazy.spawn("arcolinux-logout")),
    Key([mod], "z", lazy.spawn("zeal")),
    Key([mod], "F1", lazy.spawn(browser)),
    Key([mod], "F2", lazy.spawn(editor)),
    Key([mod], "F3", lazy.spawn("inkscape")),
    Key([mod], "F4", lazy.spawn("gimp")),
    Key([mod], "F5", lazy.spawn("meld")),
    Key([mod], "F6", lazy.spawn("vlc --video-on-top")),
    Key([mod], "F7", lazy.spawn("virtualbox")),
    Key([mod], "F8", lazy.spawn(fileManager)),
    Key([mod], "F9", lazy.spawn(mail)),
    Key([mod], "F10", lazy.spawn("spotify")),
    Key([mod], "F12", lazy.spawn("rofi -show run")),
    Key([mod], "Escape", lazy.spawn("xkill"), desc='Select window to kill'),
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "KP_Enter", lazy.spawn("gnome-calculator")),
    # SUPER + SHIFT KEYS
    Key([mod, "shift"], "q", lazy.window.kill(), desc='Kill the focused window'),
    # SUPER + CONTROL KEYS
    Key([mod, "control"], "r", lazy.restart(), desc='restart qtile'),
    Key([mod, "control"], "q", lazy.shutdown(), desc='Close session'),
    Key([mod, "control"], "Return", lazy.spawn(fileManager)),
    # ALT + ... KEYS
    Key(["mod1"], "Escape", lazy.spawn("xfce4-taskmanager")),
    Key(["mod1"], "F1", lazy.spawn("rofi -show window")),
    Key(["mod1"], "F2", lazy.spawn("rofi -show drun")),
    Key(["mod1"], "F3", lazy.spawn("rofi -show file-browser-extended")),
    Key(["mod1"], "F4", lazy.spawn("rofi -show ssh ")),

    KeyChord(["mod1"], "q", [
        Key([], "h", lazy.spawn(
            "rofi -show file-browser-extended -file-browser-dir ~/.config"
        )),
        Key([], "j", lazy.spawn(
            "rofi -show file-browser-extended -file-browser-dir ~/Git"
        )),
        Key([], "k", lazy.spawn(
            "rofi -show file-browser-extended -file-browser-dir ~/.screenlayout"
        )),
        Key([], "l", lazy.spawn(
            "rofi -show file-browser-extended -file-browser-dir ~/Proyectos"
        )),
    ]
    ),
    Key(["mod1"], "h", lazy.spawn(terminal + ' -e htop')),
    Key(["mod1"], "Left", lazy.spawn('variety -p')),
    Key(["mod1"], "Right", lazy.spawn('variety -n')),

    # SCREENSHOTS
    Key(["mod1"], "Print", lazy.spawn("xfce4-screenshooter")),
    Key(
        [], "Print",
        lazy.spawn(
            "scrot 'screenshot_%Y%m%d_%H%M%S.jpg' -e 'mv $f $$(xdg-user-dir SCREENSHOTS)'"
        ),
    ),
]

# Media keys
keys.extend([
    # INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),
    # INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn("amixer -q set Master 5%-"),
        lazy.spawn("amixer -q set Master unmuted")
    ),
    Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -q set Master 5%+"),
        lazy.spawn("amixer -q set Master unmuted")
    ),
    # MULTIMEDIA KEYS
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
]
)

# focus and screen
keys.extend([
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
    Key([mod, "shift"], "n", lazy.layout.normalize()),
    Key([mod, "shift"], "m", lazy.layout.maximize()),
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    Key([mod, "shift"], "space", lazy.layout.flip(), lazy.layout.toggle_split()),

    # MOVE WINDOW
    Key(
        [mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.swap_down(),
        lazy.layout.flip_down(),
    ),
    Key(
        [mod, "shift"], "Down",
        lazy.layout.shuffle_down(),
        lazy.layout.swap_down(),
        lazy.layout.flip_down(),
    ),
    Key(
        [mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.swap_up(),
        lazy.layout.flip_up(),
    ),
    Key(
        [mod, "shift"], "Up",
        lazy.layout.shuffle_up(),
        lazy.layout.swap_up(),
        lazy.layout.flip_up(),
    ),
    Key(
        [mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        lazy.layout.swap_left(),
        lazy.layout.swap_column_left(),
        lazy.layout.flip_left(),
    ),
    Key(
        [mod, "shift"], "Left",
        lazy.layout.shuffle_left(),
        lazy.layout.swap_left(),
        lazy.layout.swap_column_left(),
        lazy.layout.flip_left(),
    ),
    Key(
        [mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        lazy.layout.swap_right(),
        lazy.layout.swap_column_right(),
        lazy.layout.flip_right(),
    ),
    Key(
        [mod, "shift"], "Right",
        lazy.layout.shuffle_right(),
        lazy.layout.swap_right(),
        lazy.layout.swap_column_right(),
        lazy.layout.flip_right(),
    ),
    # SIZE WINDOWS
    Key(
        [mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        lazy.layout.section_down(),
    ),
    Key(
        [mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        lazy.layout.section_down(),
    ),
    Key(
        [mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        lazy.layout.section_up(),
    ),
    Key(
        [mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        lazy.layout.section_up(),
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
]
)

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
    ]
    )

mouse = [
    Click(
        ["mod"], "Button1",
        lazy.window.bring_to_front()
    ),
    Drag(
        ["mod"], "Button2",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        ["mod"], "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
]
