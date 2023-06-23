from libqtile import qtile, widget

from .manager import theme, terminal, font, mail

widget_defaults = dict(
    font=font,
    fontsize=14,
    padding=8,
    margin=8,
    foreground=theme["foreground"],
    background=theme["background"]
)


def group_box(this_screen_color, other_screen_color):
    return widget.GroupBox(
        fontsize=13,
        borderwidth=2,
        rounded=False,
        disable_drag=True,
        font=f"{font} bold",
        highlight_method="line",
        active=theme["active"],
        inactive=theme["inactive"],
        highlight_color=theme["background"],
        this_current_screen_border=this_screen_color,
        this_screen_border=this_screen_color,
        other_current_screen_border=other_screen_color,
        other_screen_border=other_screen_color
    )


def init_widgets_list():
    widgets_list = [
        group_box(theme["color2"], theme["color3"]),
        widget.CurrentLayout(
            font=f"{font} Bold",
            foreground=theme["color1"]
        ),
        widget.WindowName(
            font=f"{font} Bold Italic",
            format="{name}",
            max_chars=90,
            foreground=theme["active"]
        ),
        widget.CapsNumLockIndicator(
            font=f"{font} Bold",
            fontsize=12,
            fmt="{}",
            foreground=theme["color4"]
        ),
        widget.Volume(
            font=f"{font}",
            fmt="\uf026 {}",
            foreground=theme["color3"],
            mouse_callbacks={
                "Button3": lambda: qtile.cmd_spawn("pavucontrol")
            }
        ),
        widget.Battery(
            font=f"{font} Bold",
            format=" 󱟠 {percent:2.0%}",
            update_interval=10,
            foreground=theme["color2"],
            background=theme["background"],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("xfce4-power-manager-settings"),
                "Button3": lambda: qtile.cmd_spawn("xfce4-taskmanager")
            }
        ),
        widget.CheckUpdates(
            font=f"{font} Bold",
            distro="Arch_checkupdates",
            execute=f"{terminal} -e sudo pacman -Syu",
            update_interval=1800,
            display_format="󱑥 {updates} Updates",
            colour_have_updates=theme["foreground"]
        ),
        widget.Clock(
            font=f"{font} Bold",
            format="󱪺 %c",
            foreground=theme["color1"],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(mail),
            }
        ),
        widget.Systray(
            icon_size=22,
            margin=8,
            padding=8
        )
    ]
    return widgets_list
