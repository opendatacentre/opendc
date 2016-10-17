# -*- coding: utf-8 -*-
"""
Create a new set of machines for k8sdc to be provisioned to.

usage:
  k8sdc [--debug] machine [--help | -h]

options:
  -h, --help    show this help.
  --debug       show debug output.

example:
  k8sdc machine
"""

import logging
import os
import sys
from docopt import docopt
from k8sdc.utility import load_yaml_file
from k8sdc.provider import BareProvider, VagrantProvider

logger = logging.getLogger(__name__)


class MachineCmd(object):
  """Create a new set of machines for k8sdc to be provisioned to."""

  providers = {'bare'    : BareProvider,
               'vagrant' : VagrantProvider}

  def __init__(self, argv):
    super(MachineCmd, self).__init__()

    args = docopt(__doc__, argv=argv)
    logger.debug("k8sdc provision - args:\n{}".format(args))

    # yaml_file = '/Users/desdrury/Sites/Citopro/k8sdc/providers/vagrant/provider.yaml'
    yaml_file = os.path.realpath(os.path.join(os.path.curdir, 'provider.yaml'))
    provider_data = load_yaml_file(yaml_file)
    provider_name = provider_data.keys()[0]

    if provider_name not in self.providers.keys():
      logger.error("Unknown provider in 'provider.yaml': {}".format(provider_name))
      logger.error("Permitted providers are: \n\t{}".format(self.providers))
      print(__doc__)
      sys.exit(1)
    logger.debug("Provider: {}".format(provider_name))

    provider = self.providers[provider_name](provider_data)
    provider.validate()
    provider.create_files()
    provider.create_machines()
