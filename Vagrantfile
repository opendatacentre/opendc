# -*- mode: ruby -*-
# vi: set ft=ruby :

unless Vagrant.has_plugin?("vagrant-hostmanager")
  raise 'vagrant-hostmanager plugin is required'
end

Vagrant.configure(2) do |config|

  config.vm.box = "box-cutter/fedora22"
  config.vm.box_version = "3.0.1"

  num_nodes = (ENV['NUM_NODES'] || 2).to_i

  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.manage_guest = false
  config.hostmanager.include_offline = true

  num_nodes.times do |n|
    node_index = n+1
    config.vm.define "node#{node_index}.k8sdc.io" do |node|
      node.vm.hostname = "node#{node_index}.k8sdc.io"
      node.vm.network :private_network, ip: "192.168.100.#{110 + n}"
      node.vm.provider "virtualbox" do |vbox|
        vbox.memory = 2048
        vbox.cpus = 2
        vbox.customize ["modifyvm", :id, "--nictype1", "virtio"]
        vbox.customize ["modifyvm", :id, "--nictype2", "virtio"]
      end
    end
  end

  config.vm.define "master.k8sdc.io" do |master|
    master.vm.hostname = "master.k8sdc.io"
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
          "k8sdc-masters"  => ["master.k8sdc.io"],
          "k8sdc-nodes"   => ["node1.k8sdc.io", "node2.k8sdc.io"],
          "etcd"        => ["master.k8sdc.io", "node1.k8sdc.io", "node2.k8sdc.io"],
          "fileserver"  => ["master.k8sdc.io"]
        }
      ansible.raw_ssh_args = ['-o ControlMaster=yes']
      ansible.raw_arguments = Shellwords.shellsplit(ENV['ANSIBLE_ARGS']) if ENV['ANSIBLE_ARGS']
    end
  end

end
