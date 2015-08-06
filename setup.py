# -*- coding: utf-8 -*-
#

import setuptools
import os

def read_description():
  description = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
  return description

setuptools.setup(
    name = 'gunyanza',
    version = '0.0.1',
    author = 'Tasuku SUENAGA a.k.a. gunyarakun',
    author_email = 'tasuku-s-github@titech.ac',
    description = 'shogi AI with deep learning',
    long_description = read_description(),
    license = 'GPL3',
    keywords = 'shogi',
    url = 'https://github.com/gunyarakun/gunyanza',
    packages = [],
    scripts = [],
    test_suite = 'nose.collector',
    tests_require = ['nose>=1.0', 'mock'],
    install_requires: open('requirements.txt').read().splitlines(),
    classifiers = [
      'Development Status :: 2 - Pre-Alpha',
      'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'Topic :: Games/Entertainment :: Board Games',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
