from libqtile import layout, bar, qtile, widget
from libqtile.config import Screen, Group
from settings import theme, font, terminal, mail, config
from libqtile.lazy import lazy
from settings.float_rules import floating_rules

layout_theme = {
    "margin": [2, 1, 2, 1],
    "border_width": 1,
    "border_focus": theme.focus,
    "border_normal": theme.inactive,
    "border_on_single": True,
    "margin_on_single": 2,
    "single_margin": 2,
}

layouts = [
    layout.Bsp(**layout_theme),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(**layout_theme),
    layout.Max(**layout_theme),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        *floating_rules
    ],
    border_normal=theme.inactive,
    border_focus=theme.focus,
)

widget_defaults = dict(
    font=font,
    fontsize=13,
    padding=8,
    foreground=theme.foreground,
    background=theme.background,
)


def group(group_labels: list | str):
    group = []
    group_names = [str(f) for f in range(1, len(group_labels) + 1)]
    for i in range(len(group_names)):
        group.append(Group(name=group_names[i], label=group_labels[i]))
    return group


# * WIDGETS


def tool_box() -> widget.WidgetBox:
    return widget.WidgetBox(
        widgets=[
            widget.Volume(
                volume_app="pavucontrol",
                font=f"{font} Bold",
                mute_format="󰖁 OFF",
                unmute_format="󰕾 {volume}%",
                foreground=theme.color5,
                step=5,
                mouse_callbacks={
                    "Button1": lazy.widget["volume"].mute(),
                    "Button3": lazy.widget["volume"].run_app(),
                },
            ),
            widget.CheckUpdates(
                font=f"{font} Bold",
                distro="Arch_checkupdates",
                execute=f"{terminal} -e sudo pacman -Syu",
                update_interval=180,
                display_format="󰁇 {updates} Updates",
                colour_have_updates=theme.foreground,
            ),
            widget.Clock(
                font=f"{font} Bold",
                format=" %a %d/%m %H:%M",
                foreground=theme.color6,
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn("sh -c 'rofi -e \"$(cal -3)\"'"),
                    "Button3": lambda: qtile.cmd_spawn("sh -c 'rofi -e \"$(cal -y)\"'")
                },
            ),
            widget.Systray(icon_size=16),
            widget.Spacer(length=10),
        ],
        start_opened=True,
        fmt="󰣇",
        fontsize=24,
        foreground=theme.active,
        mouse_callbacks={
            "Button3": lambda: qtile.cmd_spawn("rofi -show drun"),
            "Button2": lambda: qtile.cmd_spawn(f"{config}/rofi/scripts/powermenu"),
        },
        close_button_location="right",
    )


def window_box(focused_group) -> widget.WidgetBox:
    return widget.WidgetBox(
        widgets=[
            widget.WindowName(
                font=f"{font} Bold Italic",
                format="{name}",
                width=bar.CALCULATED,
                max_chars=64,
                foreground=theme.focus,
            ),
            widget.Spacer(),
            widget.GroupBox(
                fontsize=16,
                rounded=False,
                disable_drag=True,
                font=f"{font} bold",
                highlight_method="text",
                active=theme.active,  # group with window
                inactive=theme.inactive,  # group without window
                highlight_color=theme.background,
                this_current_screen_border=focused_group,  # focused group
            ),
            widget.CurrentLayout(
                font=f"{font} Bold", foreground=theme.color4, fmt="[ {} ]"
            ),
        ],
        start_opened=True,
        fmt="󱂬",
        fontsize=20,
        foreground=theme.active,
        mouse_callbacks={
            "Button3": lambda: qtile.cmd_spawn("rofi -show window"),
        },
    )


def init_widgets_list():
    widgets_list = [
        widget.Spacer(length=10),
        window_box(theme.focus),
        widget.Spacer(length=bar.STRETCH),
        tool_box(),
        widget.Spacer(length=10),
    ]
    return widgets_list


def secondary_widgets_list():
    widgets_list = [
        window_box(theme.focus),
    ]
    return widgets_list


# * END WIDGETS

screens = [
    Screen(
        top=bar.Bar(
            widgets=init_widgets_list(),
            size=36,
            margin=[4, 4, 0, 4],
            opacity=0.80,
        )
    ),
    Screen(top=bar.Bar(widgets=secondary_widgets_list(), size=32)),
]

groups = group(["󱙝", "󰮯", "󰊠", "󱁂", "󰊠", ""])
# groups = group(["󰎤", "󰎧", "󰎪", "󰎭", "󰎱", "󰎳"])
# groups = group(""*6)
