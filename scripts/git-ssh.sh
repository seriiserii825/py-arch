read -p "${tmagenta}Start copyq, configure and after script end, will have sshkey in clipboard${treset}" -n 1 -r

echo "${tblue}Installing ssh git${treset}"

read -p "${tgreen}Enter email for git${treset}" email
read -p "${tblue}Enter name for git${treset}" name


ssh-keygen -t rsa -b 4096 -C "$email"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa

xclip -sel clip < ~/.ssh/id_rsa.pub

git config --global user.email "$email"
git config --global user.name "$name"

echo "${tgreen}Public key copied to clipboard, add it to github and bitbucket${treset}"
