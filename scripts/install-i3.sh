cd 
sudo touch /etc/pip.conf
sudo echo "[global]\nbreak-system-packages = true" >> /etc/pip.conf

mkdir Downloads Documents Picture
sudo pacman -S xorg xorg-xinit rofi i3 polybar polkit dunst lxsession xorg-apps dmenu gnome-keyring polkit-gnome nitrogen feh rofi 
cd
cp /etc/X11/xinitrc > ~/.xinitrc
cat <<TEST >> ".xinitrc"
exec i3 &
dunst &
lxsession
TEST
chmod +x .xinitrc
cp /etc/X11/xinit/xserverrc ~/.xserverrc
echo "exec /usr/bin/Xorg -nolisten tcp "$@" vt$XDG_VTNR >.xserverrc"
sudo systemctl start  polkit.service
sudo systemctl enable polkit.service
sudo systemctl status polkit.service
sudo reboot now
