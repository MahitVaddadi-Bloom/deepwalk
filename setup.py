#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages

# Read version from __init__.py
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'deepwalk', '__init__.py'), encoding='utf-8') as f:
    exec(f.read())

# Read README and HISTORY
with open('README.rst', encoding='utf-8') as readme_file:
    readme = readme_file.read()

try:
    with open('HISTORY.rst', encoding='utf-8') as history_file:
        history = history_file.read().replace('.. :changelog:', '')
except FileNotFoundError:
    history = ''

# Requirements
requirements = [
    'wheel>=0.30.0',
    'Cython>=0.29.0',
    'six>=1.15.0',
    'gensim @ file:///Users/L111376/Library/CloudStorage/OneDrive-EliLillyandCompany/Documents/GitHub/gensim',
    'scipy>=1.6.0',
    'psutil>=5.0.0',
    'networkx>=2.5',
    'numpy>=1.19.0',
]

test_requirements = [
    'pytest>=6.0',
    'pytest-cov',
]

setup(
    name='deepwalk',
    version=__version__,  # noqa: F821
    description='DeepWalk online learning of social representations.',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    author='Bryan Perozzi',
    author_email='bperozzi@cs.stonybrook.edu',
    url='https://github.com/phanein/deepwalk',
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'deepwalk = deepwalk.__main__:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3",
    zip_safe=False,
    keywords=['deepwalk', 'graph', 'embedding', 'network', 'machine learning'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    python_requires='>=3.8',
    project_urls={
        'Bug Tracker': 'https://github.com/phanein/deepwalk/issues',
        'Documentation': 'https://github.com/phanein/deepwalk',
        'Source Code': 'https://github.com/phanein/deepwalk',
    },
)
