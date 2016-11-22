# -*- coding: utf-8 -*-
"""
Pull k8sdc solution images to the Docker repository cache.

usage:
  k8sdc [--debug] pull [<solution>] [--help | -h]

options:
  <solution>    is a specific solution images to pull.
  -h, --help    show this help.
  --debug       show debug output.

example:
  k8sdc pull
  k8sdc pull dbs1_distributed_block_storage
"""

import logging
import os
from docopt import docopt
from k8sdc.utility import call_ansible

logger = logging.getLogger(__name__)


class PullCmd(object):
  """Pull k8sdc solution images to the Docker repository cache."""

  tag = None

  def parse(self, argv):
    args = docopt(__doc__, argv=argv)
    logger.debug("k8sdc pull - args:\n{}".format(args))
    self.tag = args['<solution>']

  def run(self):
    if self.tag is not None:
      self.tag = [self.tag]

    call_ansible(os.path.realpath(os.path.join(os.path.curdir, 'playbooks/pull.yaml')), 
                 tag = self.tag )
