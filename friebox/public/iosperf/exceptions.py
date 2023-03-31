# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  exceptions.py
@Time    :  2023/3/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
__all__ = [
    'MuxError', 'MuxReplyError', 'MuxVersionError', 'MuxServiceError', 'ServiceError',
    'IPAError'
]

from ._proto import UsbmuxReplyCode


class MuxError(Exception):
    """ Mutex error """
    pass


class IPAError(Exception):
    pass


class MuxReplyError(MuxError):
    def __init__(self, number: int):
        self.reply_code = UsbmuxReplyCode(number)
        super().__init__(self.reply_code)


class MuxVersionError(MuxError):
    pass


class ServiceError(MuxError):
    pass


class MuxServiceError(ServiceError):
    pass
