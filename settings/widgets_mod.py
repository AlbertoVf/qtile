from libqtile import widget
from settings.shortcut import colors, font

widget_defaults = dict(
    font=font,
    fontsize=13,
    padding=8,
    margin=8,
    foreground=colors["light"],
    background=colors["dark"],
)


def powerline(tx="", fg=colors["dark"], bg=colors["dark"]):
    return widget.TextBox(
        padding=-6,
        text=tx,
        foreground=fg,
        background=bg,
    )


def separator(fg=colors["urgent"], bg=colors["dark"], size=50):
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
