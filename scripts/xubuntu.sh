cd ~
git clone git@bitbucket.org:seriiserii825/xubuntu.git
cd ~/Documents
git clone git@github.com:seriiserii825/Knowledge-base_.git 

dir_path=~/.config/dunst
mkdir $dir_path
ln -s ~/xubuntu/dunstrc $dir_path/dunstrc

rm -rf ~/.config/i3
ln -s ~/xubuntu/i3 ~/.config/i3
ln -s ~/xubuntu/i3/polybar ~/.config/polybar
rm -rf ~/.config/alacritty
ln -s ~/xubuntu/alacritty ~/.config/alacritty
rm -rf ~/.config/vifm
ln -s ~/xubuntu/vifm ~/.config/vifm
rm /home/serii/.config/google-chrome/Default/Preferences
ln -s ~/xubuntu/Preferences /home/serii/.config/google-chrome/Default/Preferences
rm ~/.gitconfig
ln -s ~/xubuntu/.gitconfig ~/.gitconfig
