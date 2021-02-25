#!/usr/bin/python3

import os
from distutils.core import Distribution
from otr import __info__ as package_info
from setuptools import setup

Distribution.install_requires = None  # make distutils ignore this option that is used by setuptools when invoked from pip install

setup(
    name=package_info.__project__,
    version=package_info.__version__,

    description=package_info.__summary__,
    long_description=open('README').read(),
    license=package_info.__license__,
    url=package_info.__webpage__,

    author=package_info.__author__,
    author_email=package_info.__email__,

    platforms=["Platform Independent"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],

    packages=['otr'],
    provides=['otr'],
    install_requires=['gmpy2', 'zope.interface', 'application', 'cryptography']
)

