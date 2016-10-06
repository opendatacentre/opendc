# -*- coding: utf-8 -*-
"""
Interact with k8sdc.

usage:
  k8sdc [--help | -h] [--version] [--debug] <command> [<args>...]

options:
  -h, --help  show this help.
  --version   show the version.
  --debug     show debug output.

commands:
  init       initialize a new k8sdc installation in the current directory.
  up         run machine, provision, app, client, config and hosts commands. [NOT IMPLEMENTED]
  machine    create a new set of machines for k8sdc to be provisioned to. [NOT IMPLEMENTED]
  provision  provision k8sdc components on to the machines. [NOT IMPLEMENTED]
  app        deploy k8sdc apps to the k8s cluster. [NOT IMPLEMENTED]
  client     install kubectl and helm clients locally. [NOT IMPLEMENTED]
  config     generate a local kubeconfig file. [NOT IMPLEMENTED]
  hosts      update /etc/hosts with k8sdc hosts and services. [NOT IMPLEMENTED]
  security   manage k8sdc security, i.e. ssh config, certificates, tokens, etc.  [NOT IMPLEMENTED]
  upgrade    upgrade playbooks. [NOT IMPLEMENTED]
  status     check status of services. [NOT IMPLEMENTED]
  destroy    remove k8sdc machines. [NOT IMPLEMENTED]

environment variables:
  K8SDC_SHOW_STACK=False  show full stack of any caught exceptions . [NOT IMPLEMENTED]

examples:
  k8sdc init --provider vagrant
  k8sdc status
"""


import os
import sys
import shutil
import logging
from docopt import docopt
from k8sdc.commands.init import InitCmd
from k8sdc.commands.provision import ProvisionCmd

logger      = logging.getLogger(__name__)
__author__  = 'Des Drury'
__email__   = 'des@drury-family.com'
__version__ = '0.0.7'
commands    = {'init'      : InitCmd,
               'up'        : '',
               'machine'   : '',
               'provision' : ProvisionCmd,
               'app'       : '',
               'client'    : '',
               'config'    : '',
               'hosts'     : '',
               'security'  : '',
               'upgrade'   : '',
               'status'    : '',
               'destroy'   : ''}


# Overide of shutil.copytree to cope with dest directory already existing
def copytree(src, dest, symlinks=False, ignore=None):
  logging.debug("src:  {}".format(src))
  logging.debug("dest: {}".format(dest))
  logging.debug('Copying files ...')
  if os.path.exists(dest):
    for item in os.listdir(src):
      s = os.path.join(src, item)
      d = os.path.join(dest, item)
      if os.path.isdir(s):
        shutil.copytree(s, d, symlinks, ignore)
      else:
        shutil.copy2(s, d)
  else:
    shutil.copytree(src, dest, symlinks, ignore)
  logging.debug('----------')


# main
def main():
  args = docopt(__doc__,
                version="k8sdc {}".format(__version__),
                options_first=True)

  if args['--debug']:
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
  else:
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
  logger.debug("k8sdc - args:\n{}".format(args))

  command = args['<command>']
  if command not in commands.keys():
    logger.error("Unknown command: {}".format(command))
    print(__doc__)
    sys.exit(1)

  commands[command]([command] + args['<args>'])
