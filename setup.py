#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup, find_packages, Command
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

here = os.path.abspath(os.path.dirname(__file__))
readme = open('README.md').read()
history = open('HISTORY.md').read().replace('.. :changelog:', '')

install_requires = [
    'numpy'
]



setup(
    name='imSound',
    version='0.1.0',
    description='Pro',
    long_description=readme + '\n\n' + history,
    author='DataSounds',
    author_email='arnaldo@datasounds.org, luiz@datasounds.org',
    url='https://github.com/DataSounds/imSound',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=install_requires,
    license="BSD License",
    zip_safe=False,
    keywords='imSound',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: PSF License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
