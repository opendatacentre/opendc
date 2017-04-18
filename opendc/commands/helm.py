# -*- coding: utf-8 -*-
"""
Deploy Helm to the k8s cluster.

usage:
  opendc [--debug] helm [--help | -h]

options:
  -h, --help    show this help.
  --debug       show debug output.

example:
  opendc helm
"""

import logging
import os
from docopt import docopt
from opendc.utility import call_ansible

logger = logging.getLogger(__name__)


class HelmCmd(object):
  """Install kubectl and helm clients locally."""

  def parse(self, argv):
    args = docopt(__doc__, argv=argv)
    logger.debug("opendc helm - args:\n{}".format(args))

  def run(self):
    call_ansible(os.path.realpath(os.path.join(os.path.curdir, 'playbooks/helm.yaml')))
