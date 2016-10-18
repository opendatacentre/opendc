# -*- coding: utf-8 -*-
import logging
import os
import sys
from jinja2 import Environment, FileSystemLoader
from k8sdc.utility import execute, load_yaml_file

logger = logging.getLogger(__name__)


def get_provider():
  yaml_file = os.path.realpath(os.path.join(os.path.curdir, 'provider.yaml'))
  if not os.path.exists(yaml_file):
    logger.error("Cannot find file: {}".format(yaml_file))
    sys.exit(1)

  provider_data = load_yaml_file(yaml_file)
  provider_name = provider_data.keys()[0]

  if provider_name not in providers.keys():
    logger.error("Unknown provider in 'provider.yaml': {}".format(provider_name))
    logger.error("Permitted providers are: \n\t{}".format(providers.keys()))
    sys.exit(1)
  logger.debug("Provider: {}".format(provider_name))

  provider = providers[provider_name](provider_data)
  provider.validate()

  return provider


class Provider(object):
  """This Class is the parent for all Provider Classes"""

  def __init__(self, provider_data):
    provider_data['cwd'] = os.path.realpath(os.path.curdir)
    self.provider_data = provider_data

  def create_files(self):
    logger.debug("[* create_files *]")
    for template in self.templates:
      logger.debug("[ {} ]".format(template))
      template_dir  = os.path.realpath(os.path.join(os.path.curdir, 'templates/'))
      template_file = os.path.join(template_dir, template)
      output_file   = os.path.realpath(os.path.join(os.path.curdir, self.templates[template]))

      logger.debug("Template file: {}".format(template_file))
      logger.debug("Output file:   {}".format(output_file))

      env      = Environment(loader=FileSystemLoader(template_dir))
      template = env.get_template(os.path.basename(template_file))
      output   = template.render(self.provider_data)

      logger.debug("Rendered output:\n{}\n".format(output))
      logger.info("Writing file: {}".format(output_file))

      with open(output_file, "w") as dest:
        dest.write(output)


class BareProvider(Provider):
  """This Class provides functionality for the Bare Provider"""

  templates = {'inventory.j2'   : 'inventory'}

  def validate(self):
    # Validate provider_data using Schema
    pass

  def create_machines(self):
    logger.error("Machines must already exist for the Bare Provider")

  def destroy_machines(self):
    logger.error("Machines cannot be destroyed by the Bare Provider")


class VagrantProvider(Provider):
  """This Class provides functionality for the Vagrant Provider"""

  templates = {'Vagrantfile.j2' : 'Vagrantfile',
               'inventory.j2'   : 'inventory'}

  def validate(self):
    # Validate provider_data using Schema
    pass

  def create_machines(self):
    """Create Vagrant machines"""
    logger.info("Creating machines")
    vagrantfile = os.path.realpath(os.path.join(os.path.curdir, 'Vagrantfile'))
    if not os.path.exists(vagrantfile):
      logger.error("Cannot find file: {}".format(vagrantfile))
      logger.error("Are you sure that \'k8sdc template\' has been run?")
      sys.exit(1)
    execute("vagrant up --no-provision")

  def destroy_machines(self):
    """Destroy Vagrant machines"""
    pass


providers = {'bare'    : BareProvider,
             'vagrant' : VagrantProvider}
