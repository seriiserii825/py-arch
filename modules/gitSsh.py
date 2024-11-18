import pyperclip
import os
from rich import print
def gitSsh():
    os.system("sudo pacman -S openssh")
    os.system("ssh-keygen -t rsa -b 4096 -C \"seriiburduja@mail.com")
    os.system("eval \"$(ssh-agent -s)\"")
    os.system("ssh-add ~/.ssh/id_rsa")
    #
    pyperclip.copy(open("~/.ssh/id_rsa.pub").read())
    print("[green]Public key copied to clipboard")
    os.system("git config --global user.email \"seriiburduja@gmail.com\"")
    os.system("git config --global user.name \"Serii\"")
    os.system("sudo pacman -S lazygit")
    os.system("cd ~/Downloads")
    os.system("git clone https://github.com/fboender/multi-git-status.git")
    os.system("cd multi-git-status")
    os.system("sudo make install")

    print("[green]Public key copied to clipboard, add it to github and bitbucket")
