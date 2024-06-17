from subprocess import call
from libqtile import hook

from settings.manager import qtile_scripts
from settings.keys import keys
from settings.screen import *

dgroups_key_binder         = None
dgroups_app_rules          = []
main                       = None
follow_mouse_focus         = True
bring_front_click          = True
cursor_warp                = False
auto_fullscreen            = True
focus_on_window_activation = "smart"
wmname                     = "LG3D"


@hook.subscribe.startup_once
def start_once():
    call([qtile_scripts + "/autostart.sh"])


@hook.subscribe.client_new
def set_floating(window):
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True
