# -*- coding: utf-8 -*-

import logging
import pprintpp
import os
import shlex
import shutil
import sys
import yaml
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from collections import namedtuple
from subprocess import Popen, PIPE, STDOUT, CalledProcessError

logger = logging.getLogger(__name__)


# Overide of shutil.copytree to cope with dest directory already existing
def copytree(src, dest, symlinks=False, ignore=None):
  logger.debug("src:  {}".format(src))
  logger.debug("dest: {}".format(dest))
  logger.debug('Copying files ...')
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
  logger.debug('----------')


def load_yaml_file(yaml_file):
  yaml_file = os.path.normpath(yaml_file)
  pp        = pprintpp.PrettyPrinter(indent=2)

  if not os.path.exists(yaml_file):
    logger.error("Unable to find yaml file: {}".format(yaml_file))
    sys.exit(1)

  logger.info("Loading yaml file: {}".format(yaml_file))
  with open(yaml_file, 'r') as yaml_file:
    contents = yaml.safe_load(yaml_file)

  logger.debug('Yaml file contents as a Python object:\n' + pp.pformat(contents))

  return contents


def execute(command):
  cmd     = shlex.split(command)
  process = Popen(cmd, stdout=PIPE, stderr=STDOUT)

  while True:
    nextline = process.stdout.readline()
    if nextline == '' and process.poll() is not None:
      break
    logger.info(nextline.rstrip())

  output     = process.communicate()[0]
  returncode = process.returncode

  if returncode == 0:
    return output
  else:
    raise CalledProcessError(returncode = returncode,
                             cmd        = command,
                             output     = output)


def call_ansible(yaml_file, become=False):
  """Call Ansible with a playbook."""

  variable_manager = VariableManager()
  loader           = DataLoader()
  inventory        = Inventory(loader, variable_manager)
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
                    connection='',
                    module_path='',
                    forks=100,
                    remote_user='',
                    private_key_file=None,
                    ssh_common_args=None,
                    ssh_extra_args=None,
                    sftp_extra_args=None,
                    scp_extra_args=None,
                    become=become,
                    become_method='sudo',
                    become_user='root',
                    verbosity=2,
                    check=False)

  pbex = PlaybookExecutor(playbooks=[yaml_file],
                          inventory=inventory,
                          variable_manager=variable_manager,
                          loader=loader,
                          options=options,
                          passwords={})

  logger.debug("Calling Ansible with yaml file: {}".format(yaml_file))
  result = pbex.run()
  if result:
    logger.error("An error occured whilst executing the Ansible Playbook.")
