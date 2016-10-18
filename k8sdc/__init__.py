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
  up         run template, machine, provision, app (not yet!), client, config and hosts (not yet!) commands.
  template   create provider specific files from templates.
  machine    create a new set of machines for k8sdc to be provisioned to.
  provision  provision k8sdc components on to the machines.
  app        deploy k8sdc apps to the k8s cluster. [NOT IMPLEMENTED]
  client     install kubectl and helm clients locally.
  config     generate a local kubeconfig file.
  hosts      update the local /etc/hosts with k8sdc hosts and services. [NOT IMPLEMENTED]
  security   manage k8sdc security, i.e. ssh config, certificates, tokens, etc. [NOT IMPLEMENTED]
  upgrade    upgrade playbooks. [NOT IMPLEMENTED]
  status     check status of services. [NOT IMPLEMENTED]
  destroy    remove k8sdc machines. [NOT IMPLEMENTED]

environment variables:
  K8SDC_SHOW_STACK=False  show full stack of any caught exceptions . [NOT IMPLEMENTED]

examples:
  k8sdc init --provider vagrant
  k8sdc status
"""

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
from k8sdc.commands.hosts     import HostsCmd

logger      = logging.getLogger(__name__)
__author__  = 'Des Drury'
__email__   = 'des@drury-family.com'
__version__ = '0.0.10'
commands    = {'init'      : InitCmd,
               'up'        : UpCmd,
               'template'  : TemplateCmd,
               'machine'   : MachineCmd,
               'provision' : ProvisionCmd,
               'app'       : '',
               'client'    : ClientCmd,
               'config'    : ConfigCmd,
               'hosts'     : HostsCmd,
               'security'  : '',
               'upgrade'   : '',
               'status'    : '',
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

  k8sdc_command = commands[command]()
  k8sdc_command.parse([command] + args['<args>'])
  k8sdc_command.run()
