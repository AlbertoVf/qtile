from libqtile import hook

@hook.subscribe.startup_once
def start_once():
    from settings import qtile_scripts
    from subprocess import call
    call([qtile_scripts + "/autostart.sh"])


@hook.subscribe.client_new
def set_floating(window):
    floating_types = ["notification", "toolbar", "splash", "dialog"]
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True
        window.center()
        window.keep_above(True)
