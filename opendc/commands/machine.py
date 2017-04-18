# -*- coding: utf-8 -*-
"""
Create a new set of machines for opendc to be provisioned to.

usage:
  opendc [--debug] machine [--help | -h]

options:
  -h, --help    show this help.
  --debug       show debug output.

example:
  opendc machine
"""

import logging
from docopt import docopt
from opendc.provider import get_provider

logger = logging.getLogger(__name__)


class MachineCmd(object):
  """Create a new set of machines for opendc to be provisioned to."""

  def parse(self, argv):
    args = docopt(__doc__, argv=argv)
    logger.debug("opendc provision - args:\n{}".format(args))

  def run(self):
    provider = get_provider()
    provider.create_machines()
