#!/bin/bash

INVENTORY=${INVENTORY:-../.vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory}

#ansible-playbook ../site.yml 
ansible kub-master -m setup -i $INVENTORY