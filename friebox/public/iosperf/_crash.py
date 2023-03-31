# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  _crash.py
@Time    :  2023/3/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""

from ._sync import Sync
import logging
from ._proto import LOG
from ._safe_socket import PlistSocketProxy


logger = logging.getLogger(LOG.main)

# Ref: https://github.com/libimobiledevice/libimobiledevice/blob/master/tools/idevicecrashreport.c

class CrashManager:
    def __init__(self, copy_conn: PlistSocketProxy):
        self._afc = Sync(copy_conn)
    
    @property
    def afc(self) -> Sync:
        return self._afc

    def preview(self):
        logger.info("List of crash logs")
        if self.afc.listdir("/"):
            self.afc.treeview("/")
        else:
            logger.info("No crashes")

    def remove_all(self):
        self._afc.rmtree("/")
        logger.info("Crash file purged from device")