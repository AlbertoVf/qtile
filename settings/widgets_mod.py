from libqtile import widget
# from libqtile import qtile, widget
from settings.shortcut import font
from settings.themes import colors

widget_defaults = dict(
    font=font,
    fontsize=14,
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


def systray(size=18):
    return widget.Systray(
        icon_size=size,
        margin=8,
        padding=8,
    )


def current_layout():
    return widget.CurrentLayout(
        font=f"{font} Bold",
        foreground=colors["urgent"],
    )


def window_name():
    return widget.WindowName(
        font=f"{font} Bold Italic",
        format="{name}",
        max_chars=90,
        foreground=colors["focus"],
    )


def group_box(this_screen_color, other_screen_color):
    return widget.GroupBox(
        fontsize=13,
        borderwidth=2,
        rounded=False,
        disable_drag=True,
        highlight_method="line",
        active=colors["active"],
        inactive=colors["inactive"],
        highlight_color=colors["text"],
        this_current_screen_border=this_screen_color,
        this_screen_border=this_screen_color,
        other_current_screen_border=other_screen_color,
        other_screen_border=other_screen_color,
    )
