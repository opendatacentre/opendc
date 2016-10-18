# -*- coding: utf-8 -*-
"""
Run template, machine, provision, app (not yet!), client, config and hosts commands.

usage:
  k8sdc [--debug] up [--help | -h]

options:
  -h, --help    show this help.
  --debug       show debug output.

example:
  k8sdc up
"""

import logging
from docopt import docopt
from k8sdc.commands.template  import TemplateCmd
from k8sdc.commands.machine   import MachineCmd
from k8sdc.commands.provision import ProvisionCmd
from k8sdc.commands.client    import ClientCmd
from k8sdc.commands.config    import ConfigCmd
from k8sdc.commands.hosts     import HostsCmd

logger = logging.getLogger(__name__)


class UpCmd(object):
  """Run template, machine, provision, app (not yet!), client, config and hosts commands."""

  def parse(self, argv):
    args = docopt(__doc__, argv=argv)
    logger.debug("k8sdc up - args:\n{}".format(args))

  def run(self):
    TemplateCmd().run()
    MachineCmd().run()
    ProvisionCmd().run()
    ClientCmd().run()
    ConfigCmd().run()
    # HostsCmd().run()
