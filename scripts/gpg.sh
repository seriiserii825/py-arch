current_user=$(whoami)

zip_file_path=/home/$current_user/Downloads/desene_animate.zip

if [ ! -f $zip_file_path ]; then
    echo "${tmagenta}$zip_file_path does not exist${treset}"
    exit 1
fi


sudo pacman -S pass unzip zip
cd ~/Downloads


pass init $current_user

unzip $zip_file_path -d /home/$current_user/Downloads/desene_animate

cd desene_animate

gpg --import private.key
gpg --import public.key

read -p "Insert git repo passwords, like git@bitbucket.org:seriiserii825/passwords.git" git_repo

if [ -z $git_repo ]; then
    git_repo=git@bitbucket.org:seriiserii825/passwords.git
fi

git clone $git_repo ~/Downloads/passwords

cd ~/.password-store
rm * -rf

cp -r ~/Downloads/passwords/* ~/.password-store
cp -r ~/Downloads/passwords/.git ~/.password-store

cd ~/.password-store

ln -s ~/xubuntu/alacritty ~/.config/alacritty
read -p "You need to edit the private key. Press enter to continue" edit

if [ -z $edit ]; then
    echo "${tmagenta}Edit private key${treset}"
    exit 1
fi


