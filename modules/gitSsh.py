import pyperclip
import os
from rich import print
def gitSsh():
    os.system("sudo pacman -S openssh")
    ## run script ../scripts/git-ssh.sh
    root_scripts_path = os.path.dirname(os.path.abspath(__file__))
    print(f"root_scripts_path: {root_scripts_path}")

    # os.system(f"bash ../scripts/{current_script_path}/scripts/git-ssh.sh")
