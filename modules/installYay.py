import os
from rich import print
def installYay():
    if os.system("yay --version") == 0:
        print("[blue]Yay is already installed")
        return
    os.system("mkdir ~/Downloads")
    os.system("cd ~/Downloads")
    os.system("sudo pacman -S --needed git base-devel")
    os.system("git clone https://aur.archlinux.org/yay.git")
    os.system("cd yay && makepkg -si")
    os.system("sudo pacman -S sddm")
    os.system("sudo systemctl enable sddm.service")
    print("[blue]Yay is now installed")

