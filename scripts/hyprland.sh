function installAll(){
  sudo pacman -Syu
  sudo pacman -S hyprland wofi waybar swaylock swaync dunst dosfstools hyprpicker
  sudo pacman -S copyq openssh xclip xsel jq bat wget curl gnome-keyring polkit-gnome 
  sudo pacman -S unzip zip linux-firmware libmagick jpegoptim
  yay -S wlogout hyprshot hyprpolkitagent
}

function symlinkAll(){
  cd ~/.config

  rm -rf swaylock
  rm -rf waybar
  rm -rf wlogout
  rm -rf wofi
  rm hypr/hyprlock.conf

  ln -s ~/xubuntu/hyprland/hypr/hyprlock.conf hypr/hyprlock.conf
  ln -s ~/xubuntu/hyprland/waybar
  ln -s ~/xubuntu/hyprland/wlogout
  ln -s ~/xubuntu/hyprland/wofi

  echo "go to hyprland.conf and add a source source = ~/.config/hypr/hypr.conf"
}

function setupMonitors(){
  hyprctl monitors
}

function installFonts(){
  sudo pacman -S ttf-font-awesome otf-font-awesome ttf-jetbrains-mono
}
select action in installAll symlinkAll setupMonitors Exit
do
  case $action in
    installAll)
      installAll
      ;;
    symlinkAll)
      symlinkAll
      ;;
    setupMonitors)
      setupMonitors
      ;;
    installFonts)
      installFonts
      ;;
    Exit)
      break
      ;;
  esac
done


# installAll

# mkdir -p ~/.config/wlogout
# sudo cp /etc/wlogout/layout ~/.config/wlogout/
# sudo cp /etc/wlogout/style.css ~/.config/wlogout/
