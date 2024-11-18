import os
from rich import print


def speedUpYay():
    makepkg_file_path="/etc/makepkg.conf"
    proc_numbr = os.cpu_count()
    print(f"[yellow]Number of processors: {proc_numbr}")
    if "MAKEFLAGS" in open(makepkg_file_path).read():
        with open(makepkg_file_path, 'r') as file:
            data = file.readlines()
        with open(makepkg_file_path, 'w') as file:
            for line in data:
                file.write(line.replace('#MAKEFLAGS="-j2"', 'MAKEFLAGS="-j'+str(proc_numbr)+'"'))
        print("MAKEFLAGS is now uncommented")
    else:
        print("MAKEFLAGS is already uncommented")
    
