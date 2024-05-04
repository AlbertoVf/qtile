from libqtile import layout, bar, qtile, widget
from libqtile.config import Screen, Group, Match
from .manager import theme, Theme, terminal, font, mail

floating_types = ["notification", "toolbar", "splash", "dialog"]
layout_theme = {
    "margin"        : 4,
    "border_width"  : 2,
    "border_focus"  : theme[Theme.active],
    "border_normal" : theme[Theme.inactive],
}
layouts = [
    layout.Bsp(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
]
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
    ],
    border_normal=theme[Theme.inactive],
    border_focus=theme[Theme.active],
)
widget_defaults = dict(
    font=font,
    fontsize=13,
    padding=8,
    margin=8,
    foreground=theme[Theme.foreground],
    background=theme[Theme.background],
)


def group(group_labels):
    group = []
    group_names = [str(f) for f in range(1, len(group_labels) + 1)]
    for i in range(len(group_names)):
        group.append(Group(name=group_names[i], label=group_labels[i]))
    return group


# * WIDGETS


def group_box(this_screen_color, other_screen_color):
    return widget.GroupBox(
        fontsize=16,
        borderwidth=2,
        rounded=False,
        disable_drag=True,
        font=f"{font} bold",
        highlight_method="text",
        active=theme[Theme.active],
        inactive=theme[Theme.inactive],
        highlight_color=theme[Theme.background],
        this_current_screen_border=this_screen_color,
        this_screen_border=this_screen_color,
        other_current_screen_border=other_screen_color,
        other_screen_border=other_screen_color,
    )


def init_widgets_list():
    widgets_list = [
        group_box(theme[Theme.color2], theme[Theme.color3]),
        widget.CurrentLayout(font=f"{font} Bold", foreground=theme[Theme.color1]),
        widget.WindowName(
            font=f"{font} Bold Italic",
            format="{name}",
            max_chars=90,
            foreground=theme[Theme.active],
        ),
        widget.CapsNumLockIndicator(
            font=f"{font} Bold", fmt="{}", foreground=theme[Theme.color4]
        ),
        widget.Volume(
            font=f"{font} Bold",
            fmt="󰕾 {}",
            foreground=theme[Theme.color3],
            mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
        ),
        widget.Battery(
            font=f"{font} Bold",
            format="󰂋 {percent:2.0%}",
            update_interval=10,
            foreground=theme[Theme.color2],
            background=theme[Theme.background],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("xfce4-power-manager-settings"),
                "Button3": lambda: qtile.cmd_spawn("xfce4-taskmanager"),
            },
        ),
        widget.CheckUpdates(
            font=f"{font} Bold",
            distro="Arch_checkupdates",
            execute=f"{terminal} -e sudo pacman -Syu",
            update_interval=1800,
            display_format="󰁇 {updates} Updates",
            colour_have_updates=theme[Theme.foreground],
        ),
        widget.Clock(
            font=f"{font} Bold",
            format="󱁳 %c",
            foreground=theme[Theme.color1],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(mail),
            },
        ),
        widget.Systray(icon_size=22, margin=8, padding=8),
    ]
    return widgets_list


# * END WIDGETS

screens = [Screen(top=bar.Bar(widgets=init_widgets_list(), size=28))]

groups = group(["󰮯", "󱙝", "󰊠", "󰊠"])
