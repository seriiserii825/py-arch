import os


def installAllApps():
    os.system("cd ~/Downloads")
    os.system("sudo pacman -S vi vifm python")
    os.system("sudo touch /etc/pip.conf")
    os.system("sudo echo '[global]\nbreak-system-packages = true' >> /etc/pip.conf")
    os.system("mkdir Downloads Documents Picture")
    packages= [
            "mousepad",
            "polkit",
            "dunst",
            "lxsession",
            "xorg-apps",
            "libnotify",
            "alacritty",
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
            "linux-firmware",
            "libmagick",
            "jpegoptim",
            "ttf-dejavu",
            "awesome-terminal-fonts",
            "woff2",
            "dosfstools"
            ]
    os.system("sudo pacman -S " + " ".join(packages))
    os.system("sudo systemctl start polkit.service")
    os.system("sudo systemctl enable polkit.service")
    os.system("sudo systemctl status polkit.service")
    os.system("sudo pacman -S python-pynvim")
