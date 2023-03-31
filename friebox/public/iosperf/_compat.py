# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  _compat.py
@Time    :  2023/3/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from functools import lru_cache

cache = lru_cache(maxsize=None)