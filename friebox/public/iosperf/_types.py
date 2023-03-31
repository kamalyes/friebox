# -*- coding:utf-8 -*-
# !/usr/bin/env python 3.9.11
"""
@File    :  _types.py
@Time    :  2023/3/7 15:21 PM
@Author  :  YuYanQing
@Version :  1.0
@Contact :  mryu168@163.com
@License :  (C)Copyright 2022-2026
@Desc    :  None
"""
import enum

class ConnectionType(str, enum.Enum):
    USB = "usb"
    NETWORK = "network"


class _BaseInfo:
    def _asdict(self) -> dict:
        """ for simplejson """
        return self.__dict__.copy()
    
    def __repr__(self) -> str:
        attrs = []
        for k, v in self.__dict__.items():
            attrs.append(f"{k}={v!r}")
        return f"<{self.__class__.__name__} " + ", ".join(attrs) + ">"


class DeviceInfo(_BaseInfo):
    udid: str
    device_id: int
    conn_type: ConnectionType
