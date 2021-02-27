from libqtile.config import Screen
from libqtile import bar
from settings.widgets import *

widget_screen1 = init_widgets_list3()
widget_screen2 = init_widgets_list3()


def init_screens():
    return [
        Screen(top=bar.Bar(widgets=widget_screen1, size=24)),
        Screen(top=bar.Bar(widgets=widget_screen2, size=24)),
    ]


screens = init_screens()
