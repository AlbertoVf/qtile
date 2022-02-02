import subprocess
from libqtile.command import lazy
from libqtile import hook, qtile

from settings.manager import qtile_scripts
from settings.keys import keys
from settings.screen import *
from settings.widgets import *

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "focus"  # "smart"
wmname = "LG3D"


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


@hook.subscribe.startup_once
def start_once():
    subprocess.call([qtile_scripts + "/autostart.sh"])


@hook.subscribe.startup
def start_always():
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


@hook.subscribe.client_new
def set_floating(window):
    if window.window.get_wm_transient_for() or window.window.get_wm_type() in floating_types:
        window.floating = True
