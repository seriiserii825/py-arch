import os


def nvidia():
    print("Use Nvidia or Nouveau driver? (1/2)")
    driver = input()
    if driver == "1":
        os.system("sudo pacman -S nvidia nvidia-utils nvidia-settings")
        os.system("sudo pacman -R libgl")
        os.system("sudo pacman -R libgl xf86-video-nouveau")
    elif driver == "2":
        os.system("sudo pacman -Rdds nvidia nvidia-utils")
        os.system("sudo pacman -S --asdeps libgl")
        os.system("sudo pacman -S libgl xf86-video-nouveau")
        print("Edit /etc/mkinitcpio.conf")
        print("Add MODULES=(nouveau)")
        print("Finish scrpt after editing")
        # sudo echo "MODULES=(nouveau)" >> /etc/mkinitcpio.conf
        # sudo nvim /etc/mkinitcpio.conf
        # add MODULES=(nouveau)
        # sudo mkinitcpio -p linux
    else:
        print("Invalid input")
        exit(1)
    os.system("sudo reboot now")
