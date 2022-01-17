# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision :shell, path: "docker_install.sh"
  config.vm.provision :shell, path: "compose_install.sh"
  config.vm.network :forwarded_port, host:8000, guest:8000
  config.vm.provision :file, source:"./", destination: "web_app"
  config.vm.provision :shell, path: "start.sh"
end
