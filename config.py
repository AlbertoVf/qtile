import subprocess
from libqtile.command import lazy
from libqtile import hook

from settings.path import qtile_scripts
from settings.groups import groups
from settings.keys import keys
from settings.screen import screens
from settings.layout import *
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
    home = os.path.expanduser("~")
    subprocess.call([qtile_scripts + "/autostart.sh"])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True


# @hook.subscribe.client_new
# def assign_app_group(client):
#     d = {
#         "1": ["vivaldi-stable", "brave-browser", "bitwarden", "discord", "slack"],
#         "2": ["code", "emacs", "neovim", "pycharm", "IDEA"],
#         "3": ["Alacritty", "tilix", "termite", "GitAhead", "alacritty"],
#         "4": ["VirtualBox Manager", "VirtualBox Machine", "Vmplayer", ],
#         "5": ["evolution", "notion"],
#         "6": ["pamac-manager", "stacer"],
#         "7": ["vlc", "spotify", "pragha"],
#     }
#     wm_class = client.window.get_wm_class()[0]
#     for i in range(len(d)):
#         if wm_class in list(d.values())[i]:
#             group = list(d.keys())[i]
#             client.togroup(group)
#             client.group.cmd_toscreen()
