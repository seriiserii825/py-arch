import os


def installI3():
    os.system("cd ~/Downloads")
    os.system("sudo pacman -S vi vifm python")
    os.system("sudo touch /etc/pip.conf")
    os.system("sudo echo '[global]\nbreak-system-packages = true' >> /etc/pip.conf")
    os.system("mkdir Downloads Documents Picture")
    packages= [
            "xorg",
            "xorg-xinit",
            "rofi",
            "i3",
            "polybar",
            "mousepad",
            "polkit",
            "dunst",
            "lxsession",
            "xorg-apps",
            "libnotify",
            "alacritty",
            "dmenu",
            "copyq",
            "openssh",
            "xclip",
            "rofimoji",
            "xsel",
            "jq",
            "bat",
            "wget",
            "curl",
            "gnome-keyring",
            "polkit-gnome",
            "unzip",
            "zip",
            "nitrogen",
            "feh",
            "linux-firmware",
            "libmagick",
            "jpegoptim",
            "ttf-dejavu",
            "awesome-terminal-fonts",
            "woff2",
            "dosfstools"
            ]
    os.system("sudo pacman -S " + " ".join(packages))
    os.system("cd")
    os.system("cp /etc/X11/xinitrc > ~/.xinitrc")
    text_to_insert= "exec i3 &\ndunst &\nlxsession"
    os.system(f'echo "{text_to_insert}" >> ~/.xinitrc')
    os.system("chmod +x .xinitrc")
    os.system("cp /etc/X11/xinit/xserverrc ~/.xserverrc")
    os.system("echo 'exec /usr/bin/Xorg -nolisten tcp \"$@\" vt$XDG_VTNR >.xserverrc'")
    os.system("sudo systemctl start polkit.service")
    os.system("sudo systemctl enable polkit.service")
    os.system("sudo systemctl status polkit.service")
    os.system("sudo pacman -S python-pynvim")
