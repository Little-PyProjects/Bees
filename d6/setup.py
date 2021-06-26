from os import read
from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as req:
        contents = req.read()
        requirements = contents.split('\n')
    return requirements


setup(
    name='d6',
    version='0.0.2',
    packages=find_packages(),
    include_packge_data=True,
    install_requires=read_requirements(),
    entry_points="""
        [console_scripts]
        d6 = d6.cli:cli
    """
)
