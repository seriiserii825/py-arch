from simple_term_menu import TerminalMenu
from rich import print

from modules import configPacman
from modules.chrome import chrome
from modules.installI3 import installI3
from modules.installYay import installYay
from modules.nvidia import nvidia
from modules.speedUpYay import speedUpYay

def menu():
    main_menu_title = "[green]Main Menu.\n  Press Q or Esc to quit. \n"
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_red", "bold")
    main_menu_style = ("bg_red", "fg_yellow")
    menu_list = [
            "Config pacman.conf",
            "Install yay",
            "Speed up yay",
            "Install i3",
            "Nvidia",
            "Chrome",
            "Git ssh",
            "Download xubuntu from git",
            "Zsh Oh-my-zsh",
            "nvm(node js)",
            "Neovim",
            "Nerd Fonts",
            "Locale",
            "Bash repos",
            "Gpg Pass",
            "Py repos",
            "Audio",
            "Bluetooth",
            "BrowserPass",
            "Apps",
            "Chrome extenstions",
            "Local wp",
            "Libre Office",
            "Smtp",
            "Docker",
            "Docker Compose",
            "Youtube",
            "Hyprland",
            "Exit"
            ]

    terminal_menu = TerminalMenu(
            title=main_menu_title,
            menu_entries=menu_list,
            menu_cursor_style=main_menu_cursor_style,
            menu_highlight_style=main_menu_style,
            menu_cursor=main_menu_cursor,
            cycle_cursor=True,
            clear_screen=True,
            )
    menu_entry_indices = terminal_menu.show()
    if menu_entry_indices is None:
        print("[red]You choose to quit the menu.")
    elif menu_entry_indices == 0:
        print("[blue]You choose to Config pacman.conf.")
        configPacman.configPacman()
    elif menu_entry_indices == 1:
        print("[blue]You choose to Install yay.")
        installYay()
    elif menu_entry_indices == 2:
        print("[blue]You choose to Speed up yay.")
        speedUpYay()
    elif menu_entry_indices == 3:
        print("[blue]You choose to Install i3.")
        installI3()
    elif menu_entry_indices == 4:
        print("[blue]You choose to Nvidia.")
        nvidia()
    elif menu_entry_indices == 5:
        print("[blue]You choose to Chrome.")
        chrome()
menu()
