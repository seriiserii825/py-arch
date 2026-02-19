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

repos_file_path="/home/$USER/dotfiles/zsh_modules/zsh_python"
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
