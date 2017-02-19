# Ansible Variables
___

This section lists the purpose of the Ansible variables found in the various locations of an **k8sdc** install.

___


## Global

The global variables live in the `group_vars/k8sdc.yaml` directory.


### Node

| Name            | Purpose        |
| :---------------| :--------------|
| `interface`     | This is the network interface to be used as the main interface when installing **k8sdc** on a node with multiple network interfaces. |
| `main_ip`       | This variable defines the IP address of the main interface to be used by the various system daemons on each node.  For example `etcd`, `flannel` and the `kubelet`. |
| `use_firewalld` | |
| `admin_user`    | |
| `admin_uid`     | |
| `admin_group`   | |
| `admin_gid`     | |
| `private_key`   | |
| `public_key`    | |
| `download_dir`  | |
| `timezone`      | |
| `install_pkgs`  | |
| `packages`      | |


### Kubernetes


| Name            | Purpose        |
| :---------------| :--------------|
| `cluster_name`  | |


## Provider

Each of the variables defined within the `k8sdc.yaml` file can be overriden by variables defined within the `provider.yaml`.