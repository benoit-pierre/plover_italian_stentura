#!/usr/bin/env python3

from setuptools import setup


setup(
    name = 'plover_italian_stentura',
    version = '0.5.2',
    description = 'Italian Stentura support for Plover',
    author = 'Benoit Pierre',
    author_email = 'benoit.pierre@gmail.com',
    license = 'GNU General Public License v2 or later (GPLv2+)',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires = [
        'plover>=4.0.0.dev0',
    ],
    setup_requires = [
        'setuptools-scm',
    ],
    tests_require = [
        'mock',
    ],
    py_modules = [
        'plover_italian_stentura',
    ],
    entry_points = '''

    [plover.machine]
    Stentura (Italian version) = plover_italian_stentura:ItalianStentura

    ''',
    zip_safe = True,
)
