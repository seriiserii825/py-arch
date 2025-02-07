sudo systemctl start docker.service
systemctl status docker.service
sudo docker version
sudo usermod -aG docker $USER
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
sudo chmod 666 /var/run/docker.sock
current_user=$(whoami)
sudo usermod -aG docker $current_user
sudo chmod 666 /var/run/docker.sock
newgrp docker
