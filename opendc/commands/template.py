# -*- coding: utf-8 -*-
"""
Create provider specific files from templates.

usage:
  opendc [--debug] template [--help | -h]

options:
  -h, --help    show this help.
  --debug       show debug output.

example:
  opendc template
"""

import logging
from docopt import docopt
from opendc.provider import get_provider

logger = logging.getLogger(__name__)


class TemplateCmd(object):
  """Create provider specific files from templates."""

  def parse(self, argv):
    args = docopt(__doc__, argv=argv)
    logger.debug("opendc template - args:\n{}".format(args))

  def run(self):
    provider = get_provider()
    provider.create_files()
