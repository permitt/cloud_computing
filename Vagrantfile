# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/focal64"

  config.proxy.http     = "http://proxy.uns.ac.rs:8080"
  config.proxy.https    = "https://proxy.uns.ac.rs:8080"
  config.proxy.no_proxy = "localhost,127.0.0.1"


  config.vm.provision :docker

  config.vm.provision "file", source: "./", destination: "web_app"
end
