import os
from simple_term_menu import TerminalMenu
from rich import print

from modules import configPacman
from modules.chrome import chrome
from modules.gitSsh import gitSsh
from modules.installI3 import installI3
from modules.installYay import installYay
from modules.nvidia import nvidia
from modules.speedUpYay import speedUpYay

current_script_path = os.path.dirname(os.path.realpath(__file__))

def saveLastSelect(index):
    scripts_root_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{scripts_root_path}/last_select.txt", "w") as f:
        f.write(str(index))

def getLastSelect():
    scripts_root_path = os.path.dirname(os.path.realpath(__file__))
    if not os.path.exists(f"{scripts_root_path}/last_select.txt"):
        return 0
    with open(f"{scripts_root_path}/last_select.txt", "r") as f:
        file_content = f.read()
        file_content = file_content.strip()
        file_content = file_content.replace("\n", "")
        # file_content to int
        if not file_content.isdigit() or file_content == "0":
            return 0
        else:
            return int(file_content)

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
            "Android"
            ]

    get_last_select = getLastSelect()
    print(f"[green] Last select: {get_last_select}")
    print(f"[blue] Last select: {menu_list[get_last_select]}")
    input("Press Enter to continue...")

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
        saveLastSelect(0)
    else:
        saveLastSelect(menu_entry_indices)
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
    elif menu_entry_indices == 6:
        print("[blue]You choose to Git ssh.")
        gitSsh()
    elif menu_entry_indices == 7:
        print("[blue]You choose to Download xubuntu from git.")
        os.system(f"bash {current_script_path}/scripts/xubuntu.sh")
    elif menu_entry_indices == 8:
        print("[blue]You choose to Zsh Oh-my-zsh.")
        os.system(f"bash {current_script_path}/scripts/zsh.sh")
    elif menu_entry_indices == 9:
        print("[blue]You choose to nvm(node js).")
        print(f"current_script_path: {current_script_path}")
        os.system(f"bash {current_script_path}/scripts/nvm.sh")
    elif menu_entry_indices == 10:
        print("[blue]You choose to Neovim.")
        os.system(f"bash {current_script_path}/scripts/nvim.sh")
    elif menu_entry_indices == 11:
        print("[blue]You choose to Nerd Fonts.")
        os.system(f"bash {current_script_path}/scripts/nerd-fonts.sh")
    elif menu_entry_indices == 12:
        print("[blue]You choose to Locale.")
        os.system(f"bash {current_script_path}/scripts/locale.sh")
    elif menu_entry_indices == 13:
        print("[blue]You choose to Bash repos.")
        os.system(f"bash {current_script_path}/scripts/bash-repos.sh")
    elif menu_entry_indices == 14:
        print("[blue]You choose to Gpg Pass.")
        os.system(f"bash {current_script_path}/scripts/gpg.sh")
    elif menu_entry_indices == 15:
        print("[blue]You choose to Py repos.")
        os.system(f"bash {current_script_path}/scripts/py-repos.sh")
    elif menu_entry_indices == 16:
        print("[blue]You choose to Audio.")
        os.system(f"bash {current_script_path}/scripts/audio.sh")
    elif menu_entry_indices == 17:
        print("[blue]You choose to Bluetooth.")
        os.system(f"bash {current_script_path}/scripts/bluetooth.sh")
    elif menu_entry_indices == 18:
        print("[blue]You choose to BrowserPass.")
        os.system(f"bash {current_script_path}/scripts/browserpass.sh")
    elif menu_entry_indices == 19:
        print("[blue]You choose to Apps.")
        os.system(f"bash {current_script_path}/scripts/apps.sh")
    elif menu_entry_indices == 20:
        print("[blue]You choose to Chrome extenstions.")
        os.system(f"bash {current_script_path}/scripts/chrome-extensions.sh")
    elif menu_entry_indices == 21:
        print("[blue]You choose to Local wp.")
        os.system(f"bash {current_script_path}/scripts/local-by-flywheel.sh")
    elif menu_entry_indices == 22:
        print("[blue]You choose to Libre Office.")
        os.system(f"bash {current_script_path}/scripts/libre-office.sh")
    elif menu_entry_indices == 23:
        print("[blue]You choose to Smtp.")
        os.system(f"bash {current_script_path}/scripts/smtp.sh")
    elif menu_entry_indices == 24:
        print("[blue]You choose to Docker.")
        os.system(f"bash {current_script_path}/scripts/docker.sh")
    elif menu_entry_indices == 25:
        print("[blue]You choose to Docker Compose.")
        os.system(f"bash {current_script_path}/scripts/docker-compose.sh")
    elif menu_entry_indices == 26:
        print("[blue]You choose to Youtube.")
        os.system(f"bash {current_script_path}/scripts/youtube.sh")
    elif menu_entry_indices == 27:
        print("[blue]You choose to Hyprland.")
        os.system(f"bash {current_script_path}/scripts/hyprland.sh")
    elif menu_entry_indices == 28:
        print("[blue]You choose to Android.")
        os.system(f"bash {current_script_path}/scripts/android.sh")
        
menu()
