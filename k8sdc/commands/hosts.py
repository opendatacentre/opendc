# -*- coding: utf-8 -*-
"""
Update the local /etc/hosts with k8sdc hosts and services.

usage:
  k8sdc [--debug] hosts [--help | -h]

options:
  -h, --help    show this help.
  --debug       show debug output.

example:
  k8sdc hosts
"""

import logging
import os
from docopt import docopt
from k8sdc.utility import call_ansible

logger = logging.getLogger(__name__)


class HostsCmd(object):
  """Update the local /etc/hosts with k8sdc hosts and services."""

  def parse(self, argv):
    args = docopt(__doc__, argv=argv)
    logger.debug("k8sdc hosts - args:\n{}".format(args))

  def run(self):
    call_ansible(os.path.realpath(os.path.join(os.path.curdir, 'playbooks/hosts.yaml')))
