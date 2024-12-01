import pyperclip
import os
from rich import print
def gitSsh():
    os.system("sudo pacman -S openssh")
    ## run script ../scripts/git-ssh.sh
    current_script_path = os.path.dirname(os.path.realpath(__file__))
    print(f"current_script_path: {current_script_path}")
    os.system(f"bash {current_script_path}/scripts/git-ssh.sh")
