# -*- coding: utf-8 -*-
"""
Run template, machine, provision, app (not yet!), client, config and hosts commands.

usage:
  opendc [--debug] up [--help | -h]

options:
  -h, --help    show this help.
  --debug       show debug output.

example:
  opendc up
"""

import logging
from docopt import docopt
from opendc.commands.template  import TemplateCmd
from opendc.commands.machine   import MachineCmd
from opendc.commands.provision import ProvisionCmd
from opendc.commands.client    import ClientCmd
from opendc.commands.config    import ConfigCmd
from opendc.commands.pull      import PullCmd
from opendc.commands.helm      import HelmCmd

logger = logging.getLogger(__name__)


class UpCmd(object):
  """Run template, machine, provision, client, config, pull, helm, sol and hosts commands."""

  def parse(self, argv):
    args = docopt(__doc__, argv=argv)
    logger.debug("opendc up - args:\n{}".format(args))

  def run(self):
    TemplateCmd().run()
    MachineCmd().run()
    ProvisionCmd().run()
    ClientCmd().run()
    ConfigCmd().run()
    PullCmd().run()
    HelmCmd().run()

