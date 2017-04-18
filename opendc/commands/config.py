# -*- coding: utf-8 -*-
"""
Generate a local kubeconfig file.

usage:
  opendc [--debug] config [--help | -h]

options:
  -h, --help    show this help.
  --debug       show debug output.

example:
  opendc config
"""

import logging
import os
from docopt import docopt
from opendc.utility import call_ansible

logger = logging.getLogger(__name__)


class ConfigCmd(object):
  """Generate a local kubeconfig file."""

  def parse(self, argv):
    args = docopt(__doc__, argv=argv)
    logger.debug("opendc config - args:\n{}".format(args))

  def run(self):
    call_ansible(os.path.realpath(os.path.join(os.path.curdir, 'playbooks/config.yaml')))
