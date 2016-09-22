# Install
___

The **k8sdc** platform can be installed using a number of different [*Providers*](../providers/README.md).  The [`k8sdc`](../commands/k8sdc.md) command allows for all *Providers* to have a similar method of installation.
___


## Install the k8sdc command

The `k8sdc` command is implemented using Python 2.7.  It can be installed using `pip`.  

**Note**

It is probably best to use a seperate [Virtualenv](https://virtualenv.pypa.io/en/stable/) or [Pyenv](https://github.com/yyuu/pyenv) environment.

```
$ pip install k8sdc
```

The following dependancies will be installed along with `k8sdc`.

```
ansible>=2.1.1.0
docopt>=0.6.2
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
___


## Edit the .k8sdc file


___


## Install k8sdc

The simplest way to install **k8sdc** is by using [`k8sdc up`](../commands/k8sdc_up.md).

```
$ k8sdc up
```
___


## Validate the install

The next thing you will want to do is [validate](validate.md) that **k8sdc** has installed correctly.
