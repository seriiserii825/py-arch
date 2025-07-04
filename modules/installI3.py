import os


def installI3():
    packages = [
        "xorg",
        "xorg-xinit",
        "rofi",
        "i3",
        "polybar",
        "mousepad",
        "dmenu",
        "nitrogen",
        "feh",
        "rsync",
        "tk",
    ]
    yay_packages = ["pulseaudio-control"]
    os.system("sudo pacman -S " + " ".join(packages))
    os.system("yay -S " + " ".join(yay_packages))
    os.system("cd")
    os.system("cp /etc/X11/xinitrc > ~/.xinitrc")
    text_to_insert = "exec i3 &\ndunst &\nlxsession"
    os.system(f'echo "{text_to_insert}" >> ~/.xinitrc')
    os.system("chmod +x .xinitrc")
    os.system("cp /etc/X11/xinit/xserverrc ~/.xserverrc")
    os.system("echo 'exec /usr/bin/Xorg -nolisten tcp \"$@\" vt$XDG_VTNR >.xserverrc'")
    os.system("sudo systemctl start polkit.service")
    os.system("sudo systemctl enable polkit.service")
    os.system("sudo systemctl status polkit.service")
    os.system("sudo pacman -S python-pynvim")
