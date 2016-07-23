#!/bin/bash

INVENTORY=${INVENTORY:-../.vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory}

#ansible-playbook ../site.yml 
ansible k8sdc-master -m setup -i $INVENTORY