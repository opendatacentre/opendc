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
  up         run template, machine, provision, client, config, pull, and helm commands.
  template   create provider specific files from templates.
  machine    create a new set of machines for k8sdc to be provisioned to.
  provision  provision k8sdc components on to the machines.
  client     install kubectl and helm clients locally.
  config     generate a local kubeconfig file.
  pull       pull k8sdc solution images to the Docker repository cache.
  helm       deploy Helm to the k8s cluster.
  sol        deploy k8sdc solutions to the k8s cluster.
  hosts      update the local /etc/hosts with k8sdc hosts and services.
  security   manage k8sdc security, i.e. ssh config, certificates, tokens, etc. [NOT IMPLEMENTED]
  upgrade    upgrade playbooks. [NOT IMPLEMENTED]
  start      start k8sdc machines. [NOT IMPLEMENTED]
  status     check status of services. [NOT IMPLEMENTED]
  stop       stop k8sdc machines. [NOT IMPLEMENTED]
  destroy    remove k8sdc machines. [NOT IMPLEMENTED]

environment variables:
  K8SDC_SHOW_STACK=False  show full stack of any caught exceptions. [NOT IMPLEMENTED]

examples:
  k8sdc init --provider vagrant
  k8sdc up
  k8sdc status
"""

import os
import sys
import logging
from docopt import docopt
from k8sdc.commands.init      import InitCmd
from k8sdc.commands.up        import UpCmd
from k8sdc.commands.template  import TemplateCmd
from k8sdc.commands.machine   import MachineCmd
from k8sdc.commands.provision import ProvisionCmd
from k8sdc.commands.client    import ClientCmd
from k8sdc.commands.config    import ConfigCmd
from k8sdc.commands.pull      import PullCmd
from k8sdc.commands.helm      import HelmCmd
from k8sdc.commands.sol       import SolCmd
from k8sdc.commands.hosts     import HostsCmd

logger      = logging.getLogger(__name__)
__author__  = 'Des Drury'
__email__   = 'des@drury-family.com'
__version__ = '0.0.20'
commands    = {'init'      : InitCmd,
               'up'        : UpCmd,
               'template'  : TemplateCmd,
               'machine'   : MachineCmd,
               'provision' : ProvisionCmd,
               'client'    : ClientCmd,
               'config'    : ConfigCmd,
               'pull'      : PullCmd,
               'helm'      : HelmCmd,
               'sol'       : SolCmd,
               'hosts'     : HostsCmd,
               'security'  : '',
               'upgrade'   : '',
               'start'     : '',
               'status'    : '',
               'stop'      : '',
               'destroy'   : ''}


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

  if not args['<command>'] == 'init':
    provider_file = os.path.realpath(os.path.join(os.path.curdir, 'provider.yaml'))
    if not os.path.exists(provider_file):
      logger.error("Cannot find file 'provider.yaml' in current directory")
      sys.exit(1)

  if args['<command>'] in ['security', 'upgrade', 'start', 'status', 'stop', 'destroy']:
    logger.error("Command '{}' is not yet implemented".format(args['<command>']))
    sys.exit(1)

  k8sdc_command = commands[command]()
  k8sdc_command.parse([command] + args['<args>'])
  k8sdc_command.run()
