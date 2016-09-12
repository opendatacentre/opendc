# Utilities
___

*NOTE: This now needs a complete re-write*

There are a number of utility scripts provide by k8sdc.  This section details them.
___


## Vagrant Restart Fix

When the Vagrant managed k8sdc nodes are restarted some of the required services do not automatically come back up.  This is a a known Vagrant issue with the rpcbind service and it does not happen when using Digital Ocean.  To remedy this the `vagrant_restart_fix.sh` should be run after each restart of Vagrant.

```console
$ cd utilities

$ ./vagrant_restart_fix.sh
```


## Hosts File Setup

This utility sets up the local `/etc/hosts` file to include the k8sdc services FQDNs. 

**Note**, you will be asked for your root password.

```console
$ cd utilities

$ ./hosts_file_setup.sh
```
