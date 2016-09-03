# -*- coding: utf-8 -*-
"""
Interact with k8sdc.

usage:
  k8sdc [--help | -h] [--version] <command> [<args>...]

options:
  -h, --help  show this help.
  --version   show the version.

commands:
  init       initialize a new k8sdc installation in the current directory.
  machine    create a new set of machines for k8sdc to be deployed to. [NOT IMPLEMENTED]
  provision  provision k8sdc to the machines. [NOT IMPLEMENTED]
  client     install kubectl and helm clients locally. [NOT IMPLEMENTED]
  config     generate a local kubeconfig file. [NOT IMPLEMENTED]
  hosts      update /etc/hosts with k8sdc hosts and services. [NOT IMPLEMENTED]
  security   manage k8sdc security, i.e. ssh config, certificates, tokens, etc.  [NOT IMPLEMENTED]
  upgrade    upgrade playbooks. [NOT IMPLEMENTED]
  status     check status of services. [NOT IMPLEMENTED]
  destroy    remove k8sdc machines. [NOT IMPLEMENTED]

examples:
  k8sdc init --provider vagrant
  k8sdc status
"""

import os
import shutil
from docopt import docopt
from k8sdc.commands.init import InitCmd

__author__  = 'Des Drury'
__email__   = 'des@drury-family.com'
__version__ = '0.0.3'


def copytree(src, dst, symlinks=False, ignore=None):
  for item in os.listdir(src):
    s = os.path.join(src, item)
    d = os.path.join(dst, item)
    if os.path.isdir(s):
      shutil.copytree(s, d, symlinks, ignore)
    else:
      shutil.copy2(s, d)


def main():
  args = docopt(__doc__, 
                version="k8sdc - version {}".format(__version__),
                options_first=True)

  argv = [args['<command>']] + args['<args>']
  if args['<command>'] == 'init':
    InitCmd(argv)