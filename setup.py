# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2018-02-28 14:44:05
# @Last Modified 2018-02-28
# @Last Modified time: 2018-04-18 09:55:54

from distutils.core import setup
import sys

version = '2018.4.24'

setup(
  name = 'better',
  packages = ['better'], # this must be the same as the name above
  install_requires = [],
  version = version,
  description = 'Python builtins, just better.',
  author = 'Cody Kochmann',
  author_email = 'kochmanncody@gmail.com',
  url = 'https://github.com/CodyKochmann/better',
  download_url = 'https://github.com/CodyKochmann/better/tarball/{}'.format(version),
  keywords = ['better', 'repr', 'enhanced'],
  classifiers = [],
)
