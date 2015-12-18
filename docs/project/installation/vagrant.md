# Vagrant Installation

<hr>

## Pre-Reqs

k8sdc has been tested using the following products.

* Ansible 1.9.2

* Virtualbox 5.0.0

* Vagrant 1.7.4 and vagrant-hostmanager 1.6.1 plugin

* Mac OSX 10

**Note**

* The Macs that have tested the install have had 16GB RAM.  However, k8sdc should run in 8GB if not running any large programs.


## Instructions


Start the installation process.

**Notes**

* It will take some time to download the base box and installation binaries. 

* The vagrant-hostmanager plugin will ask for your admin password.  This is so that your local `/etc/hosts` file can be updated with the Kubernetes hostnames.

```console
$ vagrant up
```

If for any reason the Vagrant provisioning fails due to a timeout then rerun the provisioning with the following command.

```console
$ vagrant provision
```

Once the Vagrant command completes test that Kubernetes is running.

[Verifying Installation](/project/installation/verify_install/)