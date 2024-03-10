#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from setuptools import find_packages, setup

package = 'Lucidream'

with open(os.path.join(package, '__init__.py'), 'rb') as f:
    init_py = f.read().decode('utf-8')

version = re.search(
    '^__version__ = [\'\"]([^\'\"]+)[\'\"]', init_py, re.MULTILINE
).group(1)
author = re.search(
    '^__author__ = [\'\"]([^\'\"]+)[\'\"]', init_py, re.MULTILINE
).group(1)
email = re.search(
    '^__email__ = [\'\"]([^\'\"]+)[\'\"]', init_py, re.MULTILINE
).group(1)

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

packages = find_packages()

setup(
    name='Lucidream',
    packages=packages,
    version=version,
    description='A engine to make lucid dreams like a game',
    long_description='Create games with multiples finals and a client interface, easly to use, multplatform',
    author=author,
    author_email=email,
    url='https://github.com/kinhosz/Lucidream',
    install_requires=requirements,
    license='MIT',
    keywords=['dev', 'web'],
    classifiers=[
       'Development Status :: 5 - Production/Stable',
       'License :: OSI Approved :: MIT License',
       'Programming Language :: Python :: 3',
    ],
)
