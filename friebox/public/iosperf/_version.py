# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  _version.py
@Time    :  2023/3/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import pkg_resources
from ._proto import PROGRAM_NAME
try:
    __version__ = pkg_resources.get_distribution(PROGRAM_NAME).version
except pkg_resources.DistributionNotFound:
    __version__ = "unknown"