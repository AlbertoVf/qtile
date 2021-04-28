from libqtile.config import Click, Drag
from libqtile.command import lazy
from settings.shortcut import mod


mouse = [
    Drag(
        [mod],
        "Button2",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button1", lazy.window.bring_to_front()),
]
