## Before archinstall

```
lsblk
cfdisk /dev/sda
delete all partitions

in /etc/pacman.conf uncomment #Color and change Paralel to 5
```

## connect to wifi

```
rfkill list
rfkill unblock wifi
ip link
ip link set wlan0 up
iwctl
device list
station wlan0 scan
station wlan0 get-networks
station wlan0 connect SSID(wait 5sec before quit)
quit
ping ya.ru
```

## archinstall

```
set disk configuration
choos networkmanager
```

## After archinstall and before reboot

<!-- sudo pacman -S linux-lts linux-lts-headers -->
```
sudo pacman -S linux-headers networkmanager broadcom-wl
sudo systemctl enable NetworkManager
```

## After reboot

```
nmcli device wifi list
nmcli device wifi connect SSID --ask
```

## start script
### install git and python
```
sudo pacman -S git python python-pip
```
### create dir and clone
```
mkdir -p ~/Documents/python
cd ~/Documents/python
git clone https://github.com/seriiserii825/py-arch.git
cd py-arch
./pip.sh 
select Install All
```

### run script
```
venv/bin/python main.py
```
