# -*- coding: utf-8 -*-
"""
Provision k8sdc components on a set of machines.

usage:
  k8sdc [--debug] provision [--help | -h]

options:
  -h, --help    show this help.
  --debug       show debug output.

example:
  k8sdc provision
"""

import logging
from docopt import docopt
from collections import namedtuple
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory

logger = logging.getLogger(__name__)


class ProvisionCmd(object):
  """Provision k8sdc components on to a set of machines"""

  def __init__(self, argv):
    super(ProvisionCmd, self).__init__()

    args = docopt(__doc__, argv=argv)
    logger.debug("k8sdc provision - args:\n{}".format(args))

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader, variable_manager)
    variable_manager.set_inventory(inventory)

    Options = namedtuple('Options',
                         ['listtags',
                          'listtasks',
                          'listhosts',
                          'syntax',
                          'connection',
                          'module_path',
                          'forks',
                          'remote_user',
                          'private_key_file',
                          'ssh_common_args',
                          'ssh_extra_args',
                          'sftp_extra_args',
                          'scp_extra_args',
                          'become',
                          'become_method',
                          'become_user',
                          'verbosity',
                          'check'])

    options = Options(listtags=False,
                      listtasks=False,
                      listhosts=False,
                      syntax=False,
                      connection='ssh',
                      module_path="",
                      forks=100,
                      remote_user='vagrant',
                      private_key_file=None,
                      ssh_common_args=None,
                      ssh_extra_args=None,
                      sftp_extra_args=None,
                      scp_extra_args=None,
                      become=True,
                      become_method='sudo',
                      become_user='root',
                      verbosity=2,
                      check=False)

    pbex = PlaybookExecutor(playbooks=['site.yaml'],
                            inventory=inventory,
                            variable_manager=variable_manager,
                            loader=loader,
                            options=options,
                            passwords={})

    results = pbex.run()
    print(results)
