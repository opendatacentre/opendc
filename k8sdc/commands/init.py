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
from logging import debug, error, info
from docopt import docopt
from pkg_resources import Requirement, resource_filename


class InitCmd(object):
  """Initialize a new k8sdc installation"""
  
  files       = ['site.yaml', 'LICENSE']
  directories = ['roles', 'group_vars', 'keys', 'utilities']
  providers   = ['vagrant', 'bare']


  def __init__(self):
    super(InitCmd, self).__init__()

    args = docopt(__doc__)
    debug("k8sdc init - args:\n{}".format(args))

    provider = args['--provider']
    if provider not in self.providers:
      error("Unknown provider: {}".format(provider))
      error("Permitted set is: \n\t{}".format(self.providers))
      print(__doc__)
      sys.exit(1)

    curdir = os.getcwd()

    debug('provider: {}'.format(provider))
    debug('curdir:   {}'.format(curdir))
    debug('----------')

    # Check curdir does not include a .k8sdc config file
    # TODO: or parent path
    if os.path.exists(os.path.join(curdir, '.k8sdc')):
      error('Current directory already contains a \'.k8sdc\' file.')
      sys.exit(1)

    info("Copying files for provider: {}".format(provider))

    # Copy standard files
    for file in self.files:
      src = resource_filename(Requirement.parse("k8sdc"),file)
      debug("Copying file: {}".format(file))
      shutil.copy2(src, curdir)
      debug('----------')

    # Copy standard directories
    for directory in self.directories:
      src = resource_filename(Requirement.parse("k8sdc"),directory)
      debug("Copying directory: {}".format(directory))
      k8sdc.copytree(src, os.path.join(curdir, directory))

    # TODO: Ensure keys have 0400 permissions!

    # Copy provider specific directory
    provider_dir = os.path.join('providers', provider)
    src = resource_filename(Requirement.parse("k8sdc"),provider_dir)
    debug("Copying directory: {}".format(provider_dir))
    k8sdc.copytree(src, curdir)

    # create .k8sdc config file
    with open(os.path.join(curdir, '.k8sdc'), 'w'):
      os.utime(os.path.join(curdir, '.k8sdc'), None)



    