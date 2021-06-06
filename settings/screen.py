from libqtile.config import Screen
from libqtile import bar
from settings.widgets import init_widgets_list, init_widgets_list01

widget_screen1 = init_widgets_list()
widget_screen2 = init_widgets_list01()


def init_screens():
    return [
        Screen(top=bar.Bar(widgets=widget_screen1, size=28)),
        Screen(top=bar.Bar(widgets=widget_screen2, size=28)),
    ]


screens = init_screens()
