#!/bin/bash

sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo docker-compose --version



# compose_release() {
#   curl --silent "https://api.github.com/repos/docker/compose/releases/latest"   #@|
#   grep -Po '"tag_name": "\K.*?(?=")'
# }

# if ! [ -x "$(command -v docker-compose)" ]; then
#   curl -L https://github.com/docker/compose/releases/download/$(compose_release)/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && chmo


# sudo wget --output-document=/usr/local/bin/docker-compose "https://github.com/docker/compose/releases/download/$(wget --quiet --output-document=- https://api.github.com/repos/docker/compose/releases/latest | grep --perl-regexp --only-matching '"tag_name": "\K.*?(?=")')/run.sh"
# sudo chmod +x /usr/local/bin/docker-compose
# sudo wget --output-document=/etc/bash_completion.d/docker-compose "https://raw.githubusercontent.com/docker/compose/$(docker-compose version --short)/contrib/completion/bash/docker-compose"#
#printf '\nDocker Compose installed successfully\n\n'
