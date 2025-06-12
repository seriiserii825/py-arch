function installPip(){
  python3 -m venv venv
  source venv/bin/activate
  python3 -m pip install --upgrade pip
  python3 -m pip install -r requirements.txt
}

function cloneRepo(){
  local repo_name=$1
  local repo_url="git clone git@github.com:seriiserii825/$repo_name.git"
  local repos_folder="/home/$USER/Documents/python"
  cd $repos_folder
  if [ ! -d "$repo_name" ]; then
    echo "${tblue}Cloning $repo_name...${treset}"
    eval $repo_url
    cd $repo_name
    installPip
    cd $repos_folder
  else
    echo "${tmagenta}$repo_name already exists, skipping clone.${treset}"
  fi
}

repos_file_path="/home/$USER/xubuntu/zsh_modules/zsh_python"
# get all lines that start with "dir_path"
dir_paths=$(grep '^dir_path' $repos_file_path | cut -d '=' -f 2 | tr -d ' ')
# from the lines get the path after the equal sign and remove spaces
for dir_path in $dir_paths; do
  # remove """
  dir_path=$(echo $dir_path | tr -d '"')
  dir_name=$(basename "$dir_path")
  echo "${tblue}Processing directory: $dir_name${treset}"
  cloneRepo "$dir_name"
done

# py_private_url="/home/serii/Documents/python/py-private"
# if [ ! -d $py_private_url ]; then
#   git clone git@bitbucket.org:seriiserii825/py-private.git $py_private_url
#   cd $py_private_url
#   installPip
# fi
#
# wp_url="/home/serii/Documents/python/wp-python"
# if [ ! -d $wp_url ]; then
#   git clone git@github.com:seriiserii825/wp-python.git $wp_url
#   cd $wp_url
#   installPip
# fi
#
# py_scripts_url="/home/serii/Documents/python/python-scripts"
# if [ ! -d $py_scripts_url ]; then
#   git clone git@bitbucket.org:seriiserii825/python-scripts.git $py_scripts_url
#   cd $py_scripts_url
#   installPip
# fi
#
# py_parsing_url="/home/serii/Documents/python/py-parsing"
# if [ ! -d $py_parsing_url ]; then
#   git clone git@github.com:seriiserii825/py-parsing.git $py_parsing_url
#   cd $py_parsing_url
#   installPip
# fi
#
# py_pacman_path="/home/serii/Documents/python/py-pacman"
# if [ ! -d $py_pacman_path ]; then
#   git clone git@github.com:seriiserii825/py-pacman.git $py_pacman_path
#   cd $py_pacman_path
#   installPip
# fi
#
# py_scss_path="/home/serii/Documents/python/py-scss"
# if [ ! -d $py_scss_path ]; then
#   git clone git@github.com/seriiserii825/py-scss $py_scss_path
#   cd $py_scss_path
#   installPip
# fi
#
# py_clipboard_path="/home/serii/Documents/python/py-clipboard"
# if [ ! -d $py_clipboard_path ]; then
#   git clone git@github.com:seriiserii825/py-clipboard.git $py_clipboard_path
#   cd $py_clipboard_path
#   installPip
# fi
#
# py_commit_path="/home/serii/Documents/python/py-commit"
# if [ ! -d $py_commit_path ]; then
#   git clone git@github.com:seriiserii825/py-commit.git $py_commit_path
#   cd $py_commit_path
#   installPip
# fi
#
# py_vue_path="/home/serii/Documents/python/py-vue"
# if [ ! -d $py_vue_path ]; then
#   git clone git@github.com:seriiserii825/py-vue.git $py_vue_path
#   cd $py_vue_path
#   installPip
# fi
#
# py_lv_path="/home/serii/Documents/python/py-lv"
# if [ ! -d $py_lv_path ]; then
#   git clone git@github.com:seriiserii825/py-lv.git $py_lv_path
#   cd $py_lv_path
#   installPip
# fi
#
# rm -rf /home/serii/Documents/python/py-sync-settings
# py_sync_system_path="/home/serii/Documents/python/py-sync-settings"
# if [ ! -d $py_sync_system_path ]; then
#   git clone git@github.com:seriiserii825/py-sync-settings.git $py_sync_system_path
#   cd $py_sync_system_path
#   installPip
# fi
