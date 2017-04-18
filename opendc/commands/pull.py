# -*- coding: utf-8 -*-
"""
Pull opendc solution images to the Docker repository cache.

usage:
  opendc [--debug] pull [<solution>] [--help | -h]

options:
  <solution>    is a specific solution images to pull.
  -h, --help    show this help.
  --debug       show debug output.

example:
  opendc pull
  opendc pull dbs1_distributed_block_storage
"""

import logging
import os
from docopt import docopt
from opendc.utility import call_ansible

logger = logging.getLogger(__name__)


class PullCmd(object):
  """Pull opendc solution images to the Docker repository cache."""

  tag = None

  def parse(self, argv):
    args = docopt(__doc__, argv=argv)
    logger.debug("opendc pull - args:\n{}".format(args))
    self.tag = args['<solution>']

  def run(self):
    if self.tag is not None:
      self.tag = [self.tag]

    call_ansible(os.path.realpath(os.path.join(os.path.curdir, 'playbooks/pull.yaml')), 
                 tag = self.tag )
