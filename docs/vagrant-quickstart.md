# k8sdc Vagrant Quickstart

<hr>

## Pre-Reqs

k8sdc has been tested using the following products.

Ansible 1.9.2

Virtualbox 5.0.0

Vagrant 1.7.4 and vagrant-hostmanager 1.6.1 plugin

Mac OSX 10

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

Once Vagrant is complete test that Kubernetes is running.

```console
$ vagrant ssh master.kub.io

$ sudo su -

$ kubectl get node
NAME           LABELS                                STATUS
node1.kub.io   kubernetes.io/hostname=node1.kub.io   Ready
node2.kub.io   kubernetes.io/hostname=node2.kub.io   Ready

$ kubectl run nginx --image=nginx --replicas=5
CONTROLLER   CONTAINER(S)   IMAGE(S)   SELECTOR    REPLICAS
nginx        nginx          nginx      run=nginx   5
```

It will take a while for Docker to download the nginx container.  Periodically check if the pods have been launched.

```console
$ kubectl get po
NAME          READY     STATUS    RESTARTS   AGE
nginx-2gkxs   1/1       Running   0          1m
nginx-479e3   1/1       Running   0          1m
nginx-gm7m8   1/1       Running   0          1m
nginx-rtha7   1/1       Running   0          1m
nginx-xfm0b   1/1       Running   0          1m
```

Create a service endpoint for the pods.

```console
$ kubectl expose rc nginx --port=80 --target-port=80
NAME      LABELS      SELECTOR    IP(S)     PORT(S)
nginx     run=nginx   run=nginx             80/TCP

$ kubectl get se nginx
NAME      LABELS      SELECTOR    IP(S)           PORT(S)
nginx     run=nginx   run=nginx   10.254.105.42   80/TCP
```

Make a note of the assigned service IP address and log into node01.  This is required as only nodes running the kube-proxy service can access service IPs.

```console
$ vagrant ssh node1.kub.io

$ curl 10.254.105.42
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

You should see the Nginx home page.