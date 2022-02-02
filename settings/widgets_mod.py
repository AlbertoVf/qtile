from libqtile import widget
from settings.manager import theme, font


widget_defaults = dict(
    font=font,
    fontsize=14,
    padding=8,
    margin=8,
    foreground=theme["foreground"],
    background=theme["background"],
)


def powerline(tx="", fg=theme["background"], bg=theme["background"]):
    return widget.TextBox(
        padding=-6,
        text=tx,
        foreground=fg,
        background=bg,
    )


def separator(fg=theme["color1"], bg=theme["background"], size=50):
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
        foreground=theme["color1"],
    )


def window_name():
    return widget.WindowName(
        font=f"{font} Bold Italic",
        format="{name}",
        max_chars=90,
        foreground=theme["active"],
    )


def group_box(this_screen_color, other_screen_color):
    return widget.GroupBox(
        fontsize=13,
        borderwidth=2,
        rounded=False,
        disable_drag=True,
        highlight_method="line",
        active=theme["active"],
        inactive=theme["inactive"],
        highlight_color=theme["background"],
        this_current_screen_border=this_screen_color,
        this_screen_border=this_screen_color,
        other_current_screen_border=other_screen_color,
        other_screen_border=other_screen_color,
    )
