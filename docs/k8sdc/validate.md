# Validate
___


```
$ export KUBECONFIG=`pwd`/config/kubectl.kubeconfig
$ bin/kubectl get nodes
$ bin/helm init
$ bin/kubectl get po --all-namespaces
$ bin/helm install kubernetes-charts/alpine-0.1.0.tgz
$ bin/helm list
$ bin/kubectl get po
$ bin/kubectl exec -it whistful-rat-alpine /bin/sh
```