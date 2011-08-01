#!/usr/bin/env python
# -*- coding; utf-8 -*-

from setuptools import setup, find_packages

setup(name = "tagger",
        version = 0.5,
        description = "Tagger framework",
        long_description="Module for extracting tags from text documents.",
        author = "Alessandro Presta",
        author_email = "",
        url = "https://",
        packages = find_packages(),
        include_package_data = True,
        package_data = {
            '': ['*.pkl', 'conf/*.rst', 'doc/*', 'data/*', 'tests/*'],
        },
        license = 'NONE',
        platforms = 'Posix; MacOS X; Windows',
        classifiers = [ 'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Topic :: Text Processing',
        ],
        install_requires = [
            "lxml",
            "stemming",
        ],
    )
