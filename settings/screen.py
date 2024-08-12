from libqtile import layout, bar, qtile, widget
from libqtile.config import Screen, Group, Match
from settings.manager import Theme, theme, font, console, mail
from libqtile.lazy import lazy

floating_types = ["notification", "toolbar", "splash", "dialog"]

layout_theme = {
    "margin": 4,
    "border_width": 2,
    "border_focus": theme[Theme.active],
    "border_normal": theme[Theme.inactive],
}

layouts = [
    layout.Bsp(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Max(**layout_theme),
    # layout.Matrix(**layout_theme, columns=2),
    # layout.Spiral(**layout_theme, main_pane="left", clockwise=False),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Password_Entry"),
        Match(title="Calculadora"),
        Match(wm_class="file-roller")

    ],
    border_normal=theme[Theme.inactive],
    border_focus=theme[Theme.active],
)

widget_defaults = dict(
    font=font,
    fontsize=13,
    padding=8,
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


def group_box(this_screen_color):
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
        # this_screen_border=this_screen_color,
    )


def init_widgets_list():
    widgets_list = [
        group_box(theme[Theme.color3]),
        widget.CurrentLayout(
            font=f"{font} Bold", foreground=theme[Theme.color4], fmt="[ {} ]"
        ),
        widget.WindowName(
            font=f"{font} Bold Italic",
            format="{name}",
            max_chars=128,
            foreground=theme[Theme.active],
        ),
        widget.Volume(
            volume_app="pavucontrol",
            font=f"{font} Bold",
            mute_format="󰖁 OFF",
            unmute_format="󰕾 {volume}%",
            foreground=theme[Theme.color5],
            mouse_callbacks={
                "Button1": lazy.widget["volume"].mute(),
                "Button3": lazy.widget["volume"].run_app(),
            },
        ),
        widget.CheckUpdates(
            font=f"{font} Bold",
            distro="Arch_checkupdates",
            execute=f"{console} -e sudo pacman -Syu",
            update_interval=1800,
            display_format="󰁇 {updates} Updates",
            colour_have_updates=theme[Theme.foreground],
        ),
        widget.Clock(
            font=f"{font} Bold",
            format="󱁳 %c",
            foreground=theme[Theme.color6],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(mail),
            },
        ),
        widget.Systray(icon_size=22, margin=8, padding=8),
    ]
    return widgets_list


# * END WIDGETS

screens = [Screen(top=bar.Bar(widgets=init_widgets_list(), size=28))]

groups = group(["󱙝", "󰮯", "󰊠", "󰊠", "󰊠"])
