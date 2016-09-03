# -*- coding: utf-8 -*-
"""
Initialise a new k8sdc installation.

usage:
  k8sdc init [--help | -h] -p <provider>

options:
  -p, --provider=<provider>  Provider.
                                vagrant
                                do
                                aws
  -h, --help                 show this help.
"""

import k8sdc
import os
from docopt import docopt
from pkg_resources import Requirement, resource_filename
from shutil import copytree, copy


class InitCmd(object):
  """docstring for ClassName"""
  
  def __init__(self, argv):
    super(InitCmd, self).__init__()

    args = docopt(__doc__)
    # print(args)

    provider = args['--provider']
    curdir = os.path.abspath(os.curdir)

    if provider == 'vagrant':
      # check for existence of vagrant command on path
      pass

    # check curdir does not include a .k8sdc config file
    if not os.path.exists(os.path.join(curdir, '.k8sdc')):
      providers_dir = resource_filename(Requirement.parse("k8sdc"),"providers")
      src = os.path.join(providers_dir, provider)
      k8sdc.copytree(src, curdir)
    else:
      raise Exception()


    # create .k8sdc config file


    