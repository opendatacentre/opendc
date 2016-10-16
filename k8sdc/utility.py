# -*- coding: utf-8 -*-

import logging
import pprintpp
import os
import shlex
import shutil
import sys
import yaml
from subprocess import Popen, PIPE, STDOUT, CalledProcessError

logger = logging.getLogger(__name__)


# Overide of shutil.copytree to cope with dest directory already existing
def copytree(src, dest, symlinks=False, ignore=None):
  logger.debug("src:  {}".format(src))
  logger.debug("dest: {}".format(dest))
  logger.debug('Copying files ...')
  if os.path.exists(dest):
    for item in os.listdir(src):
      s = os.path.join(src, item)
      d = os.path.join(dest, item)
      if os.path.isdir(s):
        shutil.copytree(s, d, symlinks, ignore)
      else:
        shutil.copy2(s, d)
  else:
    shutil.copytree(src, dest, symlinks, ignore)
  logger.debug('----------')


def load_yaml_file(yaml_file):
  yaml_file = os.path.normpath(yaml_file)
  pp        = pprintpp.PrettyPrinter(indent=2)

  if not os.path.exists(yaml_file):
    logger.error("Unable to find yaml file: {}".format(yaml_file))
    sys.exit(1)

  logger.info("Loading yaml file: {}".format(yaml_file))
  with open(yaml_file, 'r') as yaml_file:
    contents = yaml.safe_load(yaml_file)

  logger.debug('Yaml file contents as a Python object:\n' + pp.pformat(contents))

  return contents


def execute(command):
  cmd     = shlex.split(command)
  process = Popen(cmd, stdout=PIPE, stderr=STDOUT)

  while True:
    nextline = process.stdout.readline()
    if nextline == '' and process.poll() is not None:
      break
    logger.info(nextline.rstrip())

  output     = process.communicate()[0]
  returncode = process.returncode

  if returncode == 0:
    return output
  else:
    raise CalledProcessError(returncode = returncode,
                             cmd        = command,
                             output     = output)
