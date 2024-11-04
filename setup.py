from setuptools import find_packages, setup

exec(open('./gamex/version.py').read())

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
