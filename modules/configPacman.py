def configPacman():

    pacman_file_path="/etc/pacman.conf"

# uncomment Color with python
    if "#Color" in open(pacman_file_path).read():
      with open(pacman_file_path, 'r') as file:
        data = file.readlines()
      with open(pacman_file_path, 'w') as file:
        for line in data:
          file.write(line.replace('#Color', 'Color'))
      print("Color is now uncommented")

# uncomment ParallelDownloads with python
    if "#ParallelDownloads" in open(pacman_file_path).read():
        with open(pacman_file_path, 'r') as file:
            data = file.readlines()
        with open(pacman_file_path, 'w') as file:
            for line in data:
                file.write(line.replace('#ParallelDownloads', 'ParallelDownloads'))
        print("ParallelDownloads is now uncommented")


# # add mirrors with python

    if "js-webcoding" in open(pacman_file_path).read():
      print("mirror is already added")
    else:
        with open(pacman_file_path, 'a') as file:
            file.write("Server = https://mirror.js-webcoding.de/pub/archlinux/\$repo/os/\$arch\n")
            file.write("Server = https://mirror.f4st.host/archlinux/\$repo/os/\$arch\n")
            file.write("Server = https://archmirror.tomforb.es/\$repo/os/\$arch\n")
            file.write("Server = https://mirrors.kernel.org/archlinux/\$repo/os/\$arch\n")
            file.write("Server = https://lug.mtu.edu/archlinux/\$repo/os/\$arch\n")
            file.write("Server = https://mirrors.ocf.berkeley.edu/archlinux/\$repo/os/\$arch\n")
        print("mirror is now added")

