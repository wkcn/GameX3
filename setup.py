#!/usr/bin/env python

from setuptools import find_packages, setup
from gamex.version import __version__

setup(
    name="GameX3",
    version=__version__,
    url='https://github.com/wkcn/GameX3',
    description='Experimental Game Engine',
    packages=find_packages(exclude=('examples', 'tests')),
    install_requires=[
        'numpy',
        'pygame',
    ],
    tests_require=[
        'nose',
    ],
)
