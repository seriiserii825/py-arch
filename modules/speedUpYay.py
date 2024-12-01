import os
import subprocess
import sys
from rich import print

def modify_makepkg_file(makepkg_file_path, proc_numbr):
    # Read file contents
    if "MAKEFLAGS" in open(makepkg_file_path).read():
        with open(makepkg_file_path, 'r') as file:
            data = file.readlines()
        
        # Update lines
        updated_data = ""
        for line in data:
            updated_data += line.replace('#MAKEFLAGS="-j2"', f'MAKEFLAGS="-j{proc_numbr}"')
        
        # Write updated contents with sudo
        temp_file = '/tmp/makepkg_temp'
        with open(temp_file, 'w') as temp:
            temp.write(updated_data)
        
        # Use sudo to move the temp file to the original location
        subprocess.run(['sudo', 'mv', temp_file, makepkg_file_path], check=True)
        
        print("[green]MAKEFLAGS is now uncommented")
    else:
        print("[blue]MAKEFLAGS is already uncommented")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("[red]This script needs to be run as root or with sudo.")
        sys.exit(1)

    makepkg_file_path = '/etc/makepkg.conf'  # Replace with your actual file path
    # proc_numbr=$(nproc)
    proc_numbr = os.cpu_count()
    modify_makepkg_file(makepkg_file_path, proc_numbr)
