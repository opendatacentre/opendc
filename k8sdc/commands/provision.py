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
import os
from docopt import docopt
from k8sdc.utility import call_ansible

logger = logging.getLogger(__name__)


class ProvisionCmd(object):
  """Provision k8sdc components on to a set of machines"""

  def parse(self, argv):
    args = docopt(__doc__, argv=argv)
    logger.debug("k8sdc provision - args:\n{}".format(args))

  def run(self):
    call_ansible(os.path.realpath(os.path.join(os.path.curdir, 'site.yaml')))
