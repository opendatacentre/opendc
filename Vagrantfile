# -*- mode: ruby -*-
# vi: set ft=ruby :

unless Vagrant.has_plugin?("vagrant-hostmanager")
  raise 'vagrant-hostmanager plugin is required'
end

Vagrant.configure(2) do |config|

  config.vm.box = "box-cutter/fedora22"

  num_nodes = (ENV['NUM_NODES'] || 2).to_i

  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.include_offline = true

  num_nodes.times do |n|
    node_index = n+1
    config.vm.define "node#{node_index}.kub.io" do |node|
      node.vm.hostname = "node#{node_index}.kub.io"
      node.vm.network :private_network, ip: "192.168.100.#{110 + n}"
      node.vm.provider "virtualbox" do |vbox|
        vbox.memory = 1024
        vbox.cpus = 2
        vbox.customize ["modifyvm", :id, "--nictype1", "virtio"]
        vbox.customize ["modifyvm", :id, "--nictype2", "virtio"]
      end
    end
  end

  config.vm.define "master.kub.io" do |master|
    master.vm.hostname = "master.kub.io"
    master.vm.network :private_network, ip: "192.168.100.100"
    master.vm.provider "virtualbox" do |vbox|
      vbox.memory = 1024
      vbox.cpus = 2
      vbox.customize ["modifyvm", :id, "--nictype1", "virtio"]
      vbox.customize ["modifyvm", :id, "--nictype2", "virtio"]
    end
    master.vm.provision "ansible" do |ansible|
      ansible.playbook = "site.yml"
      ansible.limit = 'all'
      ansible.groups = {
          "all-nodes"   => ["master.kub.io", "node1.kub.io", "node2.kub.io"]
          "kub-master"  => ["master.kub.io"],
          "kub-nodes"   => ["node1.kub.io", "node2.kub.io"],
          "etcd"        => ["master.kub.io", "node1.kub.io", "node2.kub.io"]
        }
      ansible.raw_arguments = Shellwords.shellsplit(ENV['ANSIBLE_ARGS']) if ENV['ANSIBLE_ARGS']
    end
  end

end
