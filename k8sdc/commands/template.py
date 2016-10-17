# -*- coding: utf-8 -*-
"""
Create provider specific files from templates.

usage:
  k8sdc [--debug] template [--help | -h]

options:
  -h, --help    show this help.
  --debug       show debug output.

example:
  k8sdc template
"""

import logging
from docopt import docopt
from k8sdc.provider import get_provider

logger = logging.getLogger(__name__)


class TemplateCmd(object):
  """Create provider specific files from templates."""

  def parse(self, argv):
    args = docopt(__doc__, argv=argv)
    logger.debug("k8sdc template - args:\n{}".format(args))

  def run(self):
    provider = get_provider()
    provider.create_files()
