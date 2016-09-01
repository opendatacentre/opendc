#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Interact with k8sdc.

usage:
  k8sdc 

options:
  -h, --help              show this help.
  --version               show the version.

examples:
  k8sdc init 
"""

from docopt import docopt

__VERSION__ = '0.0.1'


def main():
  arguments = docopt(__doc__, version="k8sdc - version {}".format(__VERSION__))


# MAIN
if __name__ == '__main__':
  main()