# Digital Ocean k8sdc Setup

## pre-reqs

*Ansible 2.0.1.0*
*dopy 0.3.5*

```
$ pip install ansible==2.0.1.0
$ pip install dopy==0.3.5
```


## Install

Modify the `groups_vars/all.yml` file with your Digital Ocean token.

Create the Digital Ocean droplets.

```
$ ansible-playbook site.yml
```

Install k8sdc.

```
$ ansible-playbook ../../../site.yml -e "@group_vars/all.yml"
```

**Note**

If you want to re-install the Digital Ocean droplets you will need to empty the `inventory` file first.

```
 $ echo > inventory
 ```

**Note**

If you want to re-generate the SSH keys then remove them from the `keys/` directory.  Also remove the SSH public key from Digital Ocean.
