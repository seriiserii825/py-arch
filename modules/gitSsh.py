import os


def gitSsh():
    ROOT_DIR = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
    # if not installed openssh
    if os.system("ssh -V") != 0:
        os.system("sudo pacman -S openssh")
    os.system(f"bash {ROOT_DIR}/scripts/git-ssh.sh")
