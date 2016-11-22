#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from k8sdc import __version__, __author__, __email__
import os
from collections import namedtuple


def add_data_files(directory, data_files):
  DataFiles = namedtuple('DataFiles', ['directory', 'files'])
  for root, dirnames, filenames in os.walk(directory):
    if len(filenames) > 0:
      files = DataFiles('k8sdc/' + root, [])
      for filename in filenames:
        files[1].append(os.path.join(root, filename))
      data_files.append(files)


data_files = []
data_files.append(('k8sdc', ['site.yaml', 'LICENSE', 'ansible.cfg']))
add_data_files('providers', data_files)
add_data_files('roles', data_files)
add_data_files('group_vars', data_files)
add_data_files('host_vars', data_files)
add_data_files('playbooks', data_files)
add_data_files('keys', data_files)
add_data_files('charts', data_files)

with open('README.rst') as readme_file:
  long_description = readme_file.read()

with open('requirements.txt') as requirements_file:
  requirements = requirements_file.read().split()


setup(name             = 'k8sdc',
      version          = __version__,
      description      = 'k8sdc',
      long_description = long_description,
      keywords         = ['k8sdc'],
      author           = __author__,
      author_email     = __email__,
      url              = 'https://github.com/desdrury/k8sdc',
      license          = 'GNU General Public License v2 (GPLv2)',
      classifiers      = ['Development Status :: 3 - Alpha',
                          'Environment :: Console',
                          'Intended Audience :: System Administrators',
                          'Intended Audience :: Developers',
                          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                          'Natural Language :: English',
                          'Programming Language :: Python :: 2.7'],
      packages         = find_packages(),
      data_files       = data_files,
      scripts          = ['bin/k8sdc'],
      install_requires = requirements)
