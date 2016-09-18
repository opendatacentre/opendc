# Kubernetes {{kubernetes}}
___

[ Flow diagram of the order the task files are called. With decision nodes for the stat file checks. ] 

## Role Directory Layout

```
roles/kubernetes/
  ├── README.md
  ├── defaults/
  │   └── main.yml
  ├── files/
  │   ├── security/
  │   │   └── kube-gen-token.sh
  │   └── services/
  │       ├── kube-apiserver.service
  │       ├── kube-controller-manager.service
  │       ├── kube-proxy.service
  │       ├── kube-scheduler.service
  │       └── kubelet.service
  ├── handlers/
  │   └── main.yml
  ├── tasks/
  │   ├── basic_auth_users.yaml
  │   ├── certificates.yaml
  │   ├── download.yaml
  │   ├── main.yaml
  │   ├── master.yaml
  │   ├── node.yaml
  │   └── tokens.yaml
  └── templates/
      ├── config/
      │   ├── config.j2
      │   ├── kube-apiserver.j2
      │   ├── kube-controller-manager.j2
      │   ├── kube-proxy.j2
      │   ├── kube-scheduler.j2
      │   └── kubelet.j2
      └── kubeconfig/
          ├── kube-controller-manager.kubeconfig.j2
          ├── kube-proxy.kubeconfig.j2
          ├── kube-scheduler.kubeconfig.j2
          ├── kubectl.kubeconfig.j2
          └── kubelet.kubeconfig.j2
```

| Directory                 | Description                                |
| :------------------------ | :----------------------------------------- |
| **defaults/**             | blah, blah                                 |
| **files/security/**       | blah, blah                                 |
| **files/services/**       | blah, blah                                 |
| **handlers/**             | blah, blah                                 |
| **tasks/**                | blah, blah                                 |
| **templates/config/**     | blah, blah                                 |
| **templates/kubeconfig/** | blah, blah                                 |



## Masters {{masters}}

```
/etc/kubernetes/
  ├── certs/
  │   ├── k8sdc-ca.crt
  │   ├── kube_apiserver.crt
  │   ├── kube_apiserver.key
  │   ├── kube_controller_manager.crt
  │   └── kube_controller_manager.key
  ├── config/
  │   ├── config
  │   ├── kube-apiserver
  │   ├── kube-controller-manager
  │   └── kube-scheduler
  ├── kubeconfig/
  │   ├── kube-controller-manager.kubeconfig
  │   ├── kubectl.kubeconfig
  │   └── kube-scheduler.kubeconfig
  ├── tokens/
  │   ├── known_tokens.csv
  │   ├── system:controller_manager-master.k8sdc.io.token
  │   ├── system:kubectl-master.k8sdc.io.token
  │   └── system:scheduler-master.k8sdc.io.token
  └── users/
      └── known_users.csv

/usr/bin/
  ├── kube-apiserver
  ├── kube-controller-manager
  ├── kube-scheduler
  └── kubectl
```

| Directory        | Description                                |
| :--------------- | :----------------------------------------- |
| **certs**        | blah, blah                                 |

| Command          | Description                                |
| :--------------- | :----------------------------------------- |
| **kube-apiserver**  | (make the command name a link to the Kubernetes documentation page for the command) |

## Nodes {{nodes}}

```
/etc/kubernetes/
  ├── certs/
  │   └── k8sdc-ca.crt
  ├── config/
  │   ├── config
  │   ├── kubelet
  │   └── kube-proxy
  ├── kubeconfig/
  │   ├── kubelet.kubeconfig
  │   └── kube-proxy.kubeconfig
  └── tokens/
      ├── system:kubelet-node1.k8sdc.io.token
      └── system:kube-proxy-node1.k8sdc.io.token

/usr/bin/
  ├── kubelet
  ├── kube-proxy
  └── kubectl

/var/run/kubernetes/

/var/lib/kubelet/

```

| Directory        | Description                                |
| :--------------- | :----------------------------------------- |
| **certs**        | blah, blah                                 |

| Command          | Description                                |
| :--------------- | :----------------------------------------- |
| **kubelet**  | (make the command name a link to the Kubernetes documentation page for the command) |




## TODO {{todo}}

* I need the ability to generate tokens for new nodes without regenerating all the node tokens!!!! [`tokens.yaml`]