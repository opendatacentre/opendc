# -*- coding: utf-8 -*-
"""
Initialise a new k8sdc installation.

usage:
  k8sdc [--debug] init [--help | -h]  -p <provider>

options:
  -p, --provider=<provider>
                provider type. One of the following:
                  bare
                  vagrant
                  do [NOT IMPLEMENTED]
                  aws [NOT IMPLEMENTED]
                  federation [NOT IMPLEMENTED]
  -h, --help    show this help.
  --debug       show debug output.

example:
  k8sdc init -p vagrant
"""

import os
import sys
import shutil
import logging
from docopt import docopt
from k8sdc.provider import providers
from k8sdc.utility import copytree

logger = logging.getLogger(__name__)


class InitCmd(object):
  """Initialize a new k8sdc installation"""

  files       = ['site.yaml', 'LICENSE', 'ansible.cfg']
  directories = ['roles', 'group_vars', 'host_vars', 'playbooks', 'keys', 'utilities']

  def parse(self, argv):
    args = docopt(__doc__, argv=argv)
    logger.debug("k8sdc init - args:\n{}".format(args))

    provider = args['--provider']
    if provider not in providers:
      logger.error("Unknown provider: {}".format(provider))
      logger.error("Permitted providers are: \n\t{}".format(providers.keys()))
      print(__doc__)
      sys.exit(1)
    self.provider = provider

  def run(self):
    curdir = os.getcwd()

    logger.debug('provider: {}'.format(self.provider))
    logger.debug('curdir:   {}'.format(curdir))
    logger.debug('----------')
    logger.info("Copying files for provider: {}".format(self.provider))

    # Check curdir does not include a provider.yaml file
    if os.path.exists(os.path.join(curdir, 'provider.yaml')):
      logger.error('Current directory already contains a \'provider.yaml\' file.')
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
      copytree(src, os.path.join(curdir, directory))

    # TODO: Ensure keys have 0400 permissions!

    # Copy provider specific directory
    provider_dir = os.path.join('providers', self.provider)
    src = os.path.join(sys.prefix + '/k8sdc', provider_dir)
    logger.debug("Copying directory: {}".format(provider_dir))
    copytree(src, curdir)
