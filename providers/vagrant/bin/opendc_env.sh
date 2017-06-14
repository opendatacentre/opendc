#!/bin/bash

export PATH=`pwd`/bin:$PATH
export KUBECONFIG=`pwd`/config/kubectl.kubeconfig
alias k=`pwd`/bin/kubectl
alias kubectl=`pwd`/bin/kubectl
alias h=`pwd`/bin/helm
alias helm=`pwd`/bin/helm
alias kt=`pwd`/bin/kubetail