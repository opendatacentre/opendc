# -*- coding: utf-8 -*-
"""
Update the local /etc/hosts with opendc hosts and services.

usage:
  opendc [--debug] hosts [--help | -h]

options:
  -h, --help    show this help.
  --debug       show debug output.

example:
  opendc hosts
"""

import logging
import os
from docopt import docopt
from opendc.utility import call_ansible

logger = logging.getLogger(__name__)


class HostsCmd(object):
  """Update the local /etc/hosts with opendc hosts and services."""

  def parse(self, argv):
    args = docopt(__doc__, argv=argv)
    logger.debug("opendc hosts - args:\n{}".format(args))

  def run(self):
    call_ansible(os.path.realpath(os.path.join(os.path.curdir, 'playbooks/hosts.yaml')))
