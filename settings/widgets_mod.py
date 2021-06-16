from libqtile import qtile, widget
from settings.shortcut import colors, font

widget_defaults = dict(
    font=font,
    fontsize=12,
    padding=4,
    margin=4,
    foreground=colors["light"],
    background=colors["dark"],
)


def powerline(tx="", fg=colors["dark"], bg=colors["dark"]):
    return widget.TextBox(
        padding=-6,
        foreground=fg,
        background=bg,
    )


def separator(fg=colors["grey"], bg=colors["dark"], size=50):
    return widget.Sep(
        padding=8,
        margin=8,
        foreground=fg,
        background=bg,
        size_percent=size,
    )


def systray(size=18, bg=colors["dark"]):
    return widget.Systray(
        icon_size=size,
        margin=8,
        padding=8,
        background=bg,
    )


def groupbox(fontsize=12,
             border=0,
             highlight_method="text",
             bg=colors["dark"]):
    return widget.GroupBox(
        fontsize=fontsize,
        borderwidth=border,
        disable_drag=True,
        rounded=False,
        highlight_method=highlight_method,
        active=colors["active"],
        inactive=colors["inactive"],
        highlight_color=colors["grey"],
        this_current_screen_border=colors["focus"],
        this_screen_border=colors["grey"],
        other_current_screen_border=colors["active"],
        other_screen_border=colors["inactive"],
        background=bg,
    )


def menu(fg=colors["color3"], bg=colors["dark"], size=22):
    return (widget.TextBox(
        text="",
        fontsize=size,
        padding=16,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn("rofi -show run"),
            "Button3": lambda: qtile.cmd_spawn("xfce4-appfinder"),
        },
        background=bg,
        foreground=fg,
    ), )
