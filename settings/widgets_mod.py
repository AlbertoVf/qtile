import os
import socket
from libqtile import qtile, widget
from settings.shortcut import colors, font

widget_defaults = dict(
    font=font,
    fontsize=13,
    padding=4,
    foreground=colors["light"],
    background=colors["dark"],
)


def indicator(
    tx="{}",
    size=12,
    style=f"{font}",
    pad=8,
    mg=8,
    fg=colors["text"],
    bg=colors["color4"],
):
    return widget.CapsNumLockIndicator(
        fmt=tx,
        fontsize=size,
        font=style,
        padding=pad,
        margin=mg,
        foreground=fg,
        background=bg,
    )


def separator(tx="", fg=colors["dark"], bg=colors["dark"]):
    return widget.TextBox(
        font=F"{font}",
        text=tx,
        fontsize=40,
        padding=-6,
        foreground=fg,
        background=bg,
    )


def systray(size=22, bg=colors["dark"]):
    return widget.Systray(
        icon_size=size,
        margin=4,
        padding=8,
        background=bg,
    )


def groupbox(fontsize=14,
             border=0,
             highlight_method="text",
             bg=colors["dark"]):
    return widget.GroupBox(
        fontsize=fontsize,
        margin=4,
        padding=8,
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
