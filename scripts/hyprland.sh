function installAll(){
  sudo pacman -Syu
  sudo pacman -S hyprland wofi waybar swaylock
  yay -S wlogout
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
