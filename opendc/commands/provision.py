# -*- coding: utf-8 -*-
"""
Provision opendc components on a set of machines.

usage:
  opendc [--debug] provision [--help | -h]

options:
  -h, --help    show this help.
  --debug       show debug output.

example:
  opendc provision
"""

import logging
import os
from docopt import docopt
from opendc.utility import call_ansible

logger = logging.getLogger(__name__)


class ProvisionCmd(object):
  """Provision opendc components on to a set of machines"""

  def parse(self, argv):
    args = docopt(__doc__, argv=argv)
    logger.debug("opendc provision - args:\n{}".format(args))

  def run(self):
    call_ansible(os.path.realpath(os.path.join(os.path.curdir, 'site.yaml')))
