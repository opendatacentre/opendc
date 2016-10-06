# -*- coding: utf-8 -*-
"""
Initialise a new k8sdc installation.

usage:
  k8sdc [--debug] init [--help | -h]  -p <provider>

options:
  -p, --provider=<provider>
                provider type. One of the following:
                  bare [NOT IMPLEMENTED]
                  vagrant
                  do [NOT IMPLEMENTED]
                  aws [NOT IMPLEMENTED]
                  federation [NOT IMPLEMENTED]
  -h, --help    show this help.
  --debug       show debug output.

example:
  k8sdc init -p vagrant
"""


import k8sdc
import os
import sys
import shutil
import logging
from docopt import docopt

logger = logging.getLogger(__name__)


class InitCmd(object):
  """Initialize a new k8sdc installation"""

  files       = ['site.yaml', 'LICENSE']
  directories = ['roles', 'group_vars', 'keys', 'utilities']
  providers   = ['vagrant', 'bare']

  def __init__(self, argv):
    super(InitCmd, self).__init__()

    args = docopt(__doc__, argv=argv)
    logger.debug("k8sdc init - args:\n{}".format(args))

    provider = args['--provider']
    if provider not in self.providers:
      logger.error("Unknown provider: {}".format(provider))
      logger.error("Permitted set is: \n\t{}".format(self.providers))
      print(__doc__)
      sys.exit(1)

    curdir = os.getcwd()

    logger.debug('provider: {}'.format(provider))
    logger.debug('curdir:   {}'.format(curdir))
    logger.debug('----------')
    logger.info("Copying files for provider: {}".format(provider))

    # Check curdir does not include a .k8sdc config file
    # TODO: or parent path
    if os.path.exists(os.path.join(curdir, '.k8sdc')):
      logger.error('Current directory already contains a \'.k8sdc\' file.')
      sys.exit(1)

    # Copy standard files
    for file in self.files:
      src = os.path.join(sys.prefix + '/k8sdc', file)
      logger.debug("Copying file: {}".format(file))
      shutil.copy2(src, curdir)
      logger.debug('----------')

    # Copy standard directories
    for directory in self.directories:
      src = os.path.join(sys.prefix + '/k8sdc', directory)
      logger.debug("Copying directory: {}".format(directory))
      k8sdc.copytree(src, os.path.join(curdir, directory))

    # TODO: Ensure keys have 0400 permissions!

    # Copy provider specific directory
    provider_dir = os.path.join('providers', provider)
    src = os.path.join(sys.prefix + '/k8sdc', provider_dir)
    logger.debug("Copying directory: {}".format(provider_dir))
    k8sdc.copytree(src, curdir)

    # create .k8sdc config file
    with open(os.path.join(curdir, '.k8sdc'), 'w'):
      os.utime(os.path.join(curdir, '.k8sdc'), None)
