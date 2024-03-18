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

requirements = [
    'altgraph==0.17.4',
    'certifi==2024.2.2',
    'chardet==3.0.4',
    'googletrans==4.0.0rc1',
    'h11==0.9.0',
    'h2==3.2.0',
    'hpack==3.0.0',
    'hstspreload==2024.3.1',
    'httpcore==0.9.1',
    'httpx==0.13.3',
    'hyperframe==5.2.0',
    'idna==2.10',
    'packaging==24.0',
    'pygame==2.5.2',
    'pyinstaller==6.5.0',
    'pyinstaller-hooks-contrib==2024.3',
    'rfc3986==1.5.0',
    'sniffio==1.3.1',
]

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
