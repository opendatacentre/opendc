# Topology
___

*NOTE: This now needs a complete re-write*

The **k8sdc** platform topology is a simple Kubernetes master plus n x nodes topology.  As can seen below.

![k8sdc topology](../images/k8sdc_topology.png)

As k8sdc grows there will be additional node types that have specialised roles, even though they are still orchestrated by Kubernetes.  Such as for network storage, external load balancers, etc.

There will be a collection of namespaces to contain the k8sdc services.  Application environments can then be created in additonal namespaces.

The Kubernetes networking is configured using Flannel.

