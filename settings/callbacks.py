# MOUSE CALLBACKS

def mouse_app_finder(qtile):
    qtile.cmd_spawn('xfce4-appfinder')


def mouse_logout(qtile):
    qtile.cmd_spawn('arcolinux-logout')


def mouse_calendar(qtile):
    qtile.cmd_spawn('evolution --component=calendar')


def mouse_rofi(qtile):
    qtile.cmd_spawn('rofi -show run')

def mouse_power_manager(qtile):
    qtile.cmd_spawn('xfce4-power-manager-settings')
