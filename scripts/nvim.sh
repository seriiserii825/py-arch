read -p "Do you already installed nvm, npm and yarn? (y/n) " -n 1 -r

if [[ $REPLY =~ ^[Nn]$ ]]
then
    echo "Please install nvm, npm and yarn first."
    echo "nvm install 18.19.0"
    echo "nvm use 18.19.0"
    echo "npm install -g yarn"
    exit 1
fi

sudo pacman -S neovim
mkdir ~/Documents/Apps
git clone git@github.com:seriiserii825/nvim-coc.git ~/Documents/Apps/nvim
ln -s ~/Documents/Apps/nvim ~/.config/nvim


# echo '[global]\nbreak-system-packages = true' | sudo tee -a /etc/pip.conf > /dev/null
# pip install pynvim
#
