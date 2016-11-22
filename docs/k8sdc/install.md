# Install
___

The **k8sdc** platform can be installed using a number of different [*Providers*](../providers/README.md).  The [`k8sdc`](../commands/k8sdc.md) command allows for all *Providers* to have a similar method of installation.
___


## Test environment

**k8sdc** is a new project and is still considered **experimental**.  As such testing has only been conducted with the Vagrant *Provider* on a limited set of environments.  The following software versions are known to work.

* macOS 10.12, CentOS 7.
* Python 2.7.11, 2.7.12.
* Ansible 2.1.2.0 (must be this version as 2.2 breaks certificate generation).
* Vagrant 1.8.7.
* Virtualbox 5.0.28, 5.1.8.

___


## Install the k8sdc command

The `k8sdc` command is implemented using Python.  It can be installed using `pip`.  

**Note**

It is probably best to use a seperate [Virtualenv](https://virtualenv.pypa.io/en/stable/) or [Pyenv](https://github.com/yyuu/pyenv) environment.

```
$ pip install k8sdc
```

The following dependancies will be installed along with `k8sdc`.

```
ansible==2.1.2.0
docopt>=0.6.2
Jinja2>=2.8
pprintpp>=0.2.3
```

**Note**

Ansible will also install a number of its own dependancies.
___


## Initialise k8sdc

Before installing **k8sdc**, a directory needs to be initialised with the files for a particular *Provider*.  The following example uses [Vagrant](https://www.vagrantup.com) as the *Provider*.

```
$ mkdir ~/k8sdc
$ cd ~/k8sdc
$ k8sdc init -p vagrant
```

**Note**

To install using the Vagrant *Provider* the following software versions must be installed.

* Vagrant 1.8.7
* Virtualbox 5.0.26 and above

___


## Edit the provider.yaml file

If you wish to change the install defaults then you can review and edit the `provider.yaml` file that has been created in the install root directory.

*TODO*
___


## Generate public / private key pair for admin user

You can generate your own public / private key pair for the admin user or make use of the sample ones provided.  The key pair can be found in the `keys/` directory of the install root.

*TODO*
___


## Install the base components

The simplest way to install the **k8sdc** base components is by using [`k8sdc up`](../commands/k8sdc_up.md).

```
$ k8sdc up
```

**Notes**

* The default installation directory for the `kubectl` and `helm` commands is in the `bin/` directory of the install root.
* The initial install will take some time as the *Solution* images are also pulled so that the *Solutions* can be installed much faster.

___


## Validate the install

Once `k8sdc up` has completed you should have a working installation of the **k8sdc** base components.  To test this use the following commands.

```
$ export KUBECONFIG=`pwd`/config/kubectl.kubeconfig
$ bin/kubectl get nodes
```

You should see the set of Kubernetes hosts, i.e.

```
NAME                STATUS    AGE
node1.vb.k8sdc.io   Ready     5m
node2.vb.k8sdc.io   Ready     5m
node3.vb.k8sdc.io   Ready     5m
```
___


## Install the Solutions

Once the **k8sdc** base components are installed the [*Solutions*](../reference/solution.md) can be installed.

```
$ k8sdc sol
```

Currently the following *Solutions* will be installed.

* [(cs1) Cluster Services](../reference/solutions/cs1_cluster_services.md)
* [(cm1) Cluster Management](../reference/solutions/cm1_cluster_management.md)
* [(dbs1) Distributed Block Storage](../reference/solutions/dbs1_distributed_block_storage.md)
* [(im1) Identity Management](../reference/solutions/im1_identity_management.md)
* [(hrp1) HTTP/S Reverse Proxy](../reference/solutions/hrp1_https_reverse_proxy.md)
* [(m1) Metrics](../reference/solutions/m1_metrics.md)
* [(jm1) Job Management](../reference/solutions/jm1_job_management.md)

___


## Modify the local hosts file

Once the **k8sdc** *Solutions* are installed the local `hosts` file can be updated so that the *Solution* web UIs are accessible on the installation machine.

```
$ sudo k8sdc hosts
```

**Note**

It is important to run the `k8sdc` command as `root`.
___


## Access the Solutions

Now you can access the web UIs of the *Solutions*  that provide one.


#### (cm1) Cluster Management

http://dashboard.k8sdc.io

#### (im1) Identity Management

http://keycloak.k8sdc.io

#### (m1) Metrics

http://grafana.k8sdc.io

http://prometheus.k8sdc.io

**Note**

Prometheus is currently non-functional.  

#### (jm1) Job Management

http://jenkins.k8sdc.io

**Note**

More integration work needs to be done.



