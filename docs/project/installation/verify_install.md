# Verifying Installation

<hr>

Use the following instructions to validate that the install has succeeded.  The hostnames used are the default Vagrant ones, replace as appropriate.

```console
$ vagrant ssh master.k8sdc.io

$ sudo su -

$ kubectl get node
NAME           LABELS                                STATUS
node1.k8sdc.io   kubernetes.io/hostname=node1.k8sdc.io   Ready
node2.k8sdc.io   kubernetes.io/hostname=node2.k8sdc.io   Ready

$ kubectl run nginx --image=nginx --replicas=5
replicationcontroller "nginx" created
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
service "nginx" exposed

$ kubectl get svc nginx
NAME      CLUSTER_IP     EXTERNAL_IP   PORT(S)   SELECTOR    AGE
nginx     10.254.4.181   <none>        80/TCP    run=nginx   1m
```

Make a note of the assigned cluster IP address and log into node1.  This is required as only nodes running the kube-proxy service can access service IPs.

```console
$ vagrant ssh node1.k8sdc.io

$ curl 10.254.4.181
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