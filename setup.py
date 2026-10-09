#!/usr/bin/python3

import os
from setuptools import setup


class PackageInfo(object):
    # read otr/__info__.py without importing the otr package: its __init__
    # imports gmpy2 and cryptography, which need not be installed to build
    def __init__(self, info_file):
        with open(info_file) as f:
            exec(f.read(), self.__dict__)
        self.__dict__.pop('__builtins__', None)


package_info = PackageInfo(os.path.join('otr', '__info__.py'))

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

