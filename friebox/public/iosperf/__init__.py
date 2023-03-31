# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  __init__.py
@Time    :  2023/3/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from ._device import BaseDevice as Device
from ._usbmux import Usbmux, ConnectionType
from ._perf import Performance, DataType
from .exceptions import *
from ._proto import PROGRAM_NAME
from loguru import logger


logger.disable(PROGRAM_NAME)