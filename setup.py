#!/usr/bin/env python
# coding: utf-8
#
# Licensed under MIT
#
import setuptools
from friebox import __version__

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    install_requires=['flask>=2.2.3', 'httpio>=0.3.0', 'requests>=2.28.2',
                      'logzero>=1.7.0', 'tidevice>=0.10.7', 'tqdm>=4.65.0', 'xlwt>=1.3.0',
                      'flask_socketio>=5.3.3', 'fire>=0.5.0'],
    version=__version__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="friebox - Real-time collection tool for Android/iOS performance data.",
    packages=setuptools.find_namespace_packages(include=["friebox", "friebox.*"], ),
    include_package_data=True
)
