from os import path

home = path.expanduser("~")
qtile_path = path.join(home, '.config', 'qtile')
qtile_scripts = path.join(qtile_path, "scripts")
qtile_themes = path.join(qtile_path, "themes")

# nerd fonts https://www.nerdfonts.com/cheat-sheet
font = "FantasqueSansMono Nerd Font"
editor = "code"  # Code editor (code-oss/nvim/vim/code)
terminal = "alacritty"  # Terminal (alacritty/tilix/termite)
fileManager = "thunar"  # File Manager (nautilus/thunar/polo)
browser = "brave"  # Web Browser (brave/vivaldi-stable/firefox)
mail = "evolution"  # Mail Client (evolution)
