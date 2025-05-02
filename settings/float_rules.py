from libqtile.config import Match

title_rules = [
    Match(title=x) for x in [
        "Password_Entry",
        "Bluetooth",
        "mpv",
        "pinentry"
    ]
]

class_rules = [
    Match(wm_class=x) for x in [
        "ssh-askpass",
        "qalculate-gtk",
        "file-roller",
        "blueman-manager",
        "xfce4-clipman-history",
    ]
]

floating_rules = [ *title_rules, *class_rules ]
