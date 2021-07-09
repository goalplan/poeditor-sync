#!/usr/bin/env python3
from setuptools import setup

try:
    long_description = open('README.md', 'r').read()
except:
    long_description = ''

setup(
    name='poeditor-sync',
    version='0.1',
    packages=['poeditor_sync'],
    py_modules=['cmd'],
    entry_points={
        'console_scripts': ['poeditor = poeditor_sync.cmd:poeditor'],
    },
    url='https://github.com/mick88/poeditor-sync',
    license='MIT',
    author='Michal Dabski',
    author_email='contact@michaldabski.com',
    install_requires=[
        'click',
        'poeditor',
        'pyyaml',
    ],
    description='Command line client for POEditor service',
    long_description_content_type='text/markdown',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    project_urls={
        'Source': 'https://github.com/mick88/poeditor-sync',
        'Tracker': 'https://github.com/mick88/poeditor-sync/issues',
    },
)
