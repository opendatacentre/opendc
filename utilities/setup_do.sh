#!/bin/bash
# This script creates a new Git repository with the correct layout for k8sdc to be deployed
# to Digital Ocean

# Code this so that it doscovers the path of the command then removes the k8sdc/utilities/setup_do.sh part
# before adding the k8sdc_do part.
GIT_REPO=${GIT_REPO:-../../k8sdc_do}

# echo $GIT_REPO

# Only create a GIT repo if a command line flag is set
[ ! -d $GIT_REPO ] && 
  echo INFO: Git repo does not exist.  Creating. && 
  git init $GIT_REPO &&
  FRESH_REPO=1

[ -n "$FRESH_REPO" ] &&
  echo INFO: Copying template files
  # Copy files



