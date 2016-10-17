# -*- coding: utf-8 -*-
"""
Generate a local kubeconfig file.

usage:
  k8sdc [--debug] config [--help | -h]

options:
  -h, --help    show this help.
  --debug       show debug output.

example:
  k8sdc config
"""

import logging
import os
from docopt import docopt
from k8sdc.utility import call_ansible

logger = logging.getLogger(__name__)


class ConfigCmd(object):
  """Generate a local kubeconfig file."""

  def parse(self, argv):
    args = docopt(__doc__, argv=argv)
    logger.debug("k8sdc config - args:\n{}".format(args))

  def run(self):
    call_ansible(os.path.realpath(os.path.join(os.path.curdir, 'playbooks/config.yaml')))
