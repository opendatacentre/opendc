# -*- coding: utf-8 -*-
"""
Install kubectl and helm clients locally.

usage:
  k8sdc [--debug] client [--help | -h]

options:
  -h, --help    show this help.
  --debug       show debug output.

example:
  k8sdc client
"""

import logging
import os
from docopt import docopt
from k8sdc.utility import call_ansible

logger = logging.getLogger(__name__)


class ClientCmd(object):
  """Install kubectl and helm clients locally."""

  def __init__(self, argv):
    super(ClientCmd, self).__init__()

    args = docopt(__doc__, argv=argv)
    logger.debug("k8sdc client - args:\n{}".format(args))

    client_yaml = os.path.realpath(os.path.join(os.path.curdir, 'playbooks/client.yaml'))
    call_ansible(client_yaml)
