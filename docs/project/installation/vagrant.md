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

Once the Vagrant command completes, k8sdc will begin pulling down the Docker images required to build the services.  This will take some time (at least 20 minutes).  Once this is done you can test the installation uisng either of the following guides.

* [Verifying Installation](verify_install.md)

* [Accessing Services](services.md)


## Important Note

Please see the [Vagrant Restart Fix](../../reference/utilities.md#vagrant_restart_fix) for details about restarting k8sdc when using Vagrant.