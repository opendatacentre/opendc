# Overview

<hr>

## Capabilities

Are the things that an environment or application can do. such as.  Capabilities can be mixed and matched in many different services / environments.  For instance a productivity capability provided by the k8sdc productivity services might require a highly available SQL database.  Equally and application in a development environment might also require such a capability.  In fact a capability, such as logging may have many sub-capabilities.  There is no hard line.

## Solutions

Can be many solutions to a capability

## Services

Services are a collection of capabilities provided within a namespaces, such as kube-system. For instance k8sdc provides a number of default capabilities segmented into specific namespaces.  There are also a number of caoabilities provided by default by Kubernetes and these live in the kube-system namespace.  Services can be thought of as applications.

## Environments

Are a Kubernetes Namespace.  They are composed of services (groups of capabilities) and / or just capabilities.  Within this documentation environments and namespaces are synonomous for each other.

## Summary

The user is able to pick and choose the capabilities theyr require and compose them into applications / larger systems.