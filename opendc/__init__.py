# -*- coding: utf-8 -*-
"""
Interact with opendc.

usage:
  opendc [--help | -h] [--version] [--debug] <command> [<args>...]

options:
  -h, --help  show this help.
  --version   show the version.
  --debug     show debug output.

commands:
  init       initialize a new opendc installation in the current directory.
  up         run template, machine, provision, client, config, pull, and helm commands.
  template   create provider specific files from templates.
  machine    create a new set of machines for opendc to be provisioned to.
  provision  provision opendc components on to the machines.
  client     install kubectl and helm clients locally.
  config     generate a local kubeconfig file.
  pull       pull opendc solution images to the Docker repository cache.
  helm       deploy Helm to the k8s cluster.
  sol        deploy opendc solutions to the k8s cluster.
  hosts      update the local /etc/hosts with opendc hosts and services.
  security   manage opendc security, i.e. ssh config, certificates, tokens, etc. [NOT IMPLEMENTED]
  upgrade    upgrade playbooks. [NOT IMPLEMENTED]
  start      start opendc machines. [NOT IMPLEMENTED]
  status     check status of services. [NOT IMPLEMENTED]
  stop       stop opendc machines. [NOT IMPLEMENTED]
  destroy    remove opendc machines. [NOT IMPLEMENTED]

environment variables:
  opendc_SHOW_STACK=False  show full stack of any caught exceptions. [NOT IMPLEMENTED]

examples:
  opendc init --provider vagrant
  opendc up
  opendc status
"""

import os
import sys
import logging
from docopt import docopt
from opendc.commands.init      import InitCmd
from opendc.commands.up        import UpCmd
from opendc.commands.template  import TemplateCmd
from opendc.commands.machine   import MachineCmd
from opendc.commands.provision import ProvisionCmd
from opendc.commands.client    import ClientCmd
from opendc.commands.config    import ConfigCmd
from opendc.commands.pull      import PullCmd
from opendc.commands.helm      import HelmCmd
from opendc.commands.sol       import SolCmd
from opendc.commands.hosts     import HostsCmd

logger      = logging.getLogger(__name__)
__author__  = 'Des Drury'
__email__   = 'des@drury-family.com'
__version__ = '0.0.22.alpha.1'
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
                version="opendc {}".format(__version__),
                options_first=True)

  if args['--debug']:
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
  else:
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
  logger.debug("opendc - args:\n{}".format(args))

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

  opendc_command = commands[command]()
  opendc_command.parse([command] + args['<args>'])
  opendc_command.run()
