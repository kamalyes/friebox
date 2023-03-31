<p align="center">
<a href="#">
<img src="./friebox/static/images/logo.svg" alt="friebox" width="150">
</a>

</p>
<p align="center">
<a href="https://pypi.org/project/friebox/" target="__blank"><img src="https://img.shields.io/pypi/v/friebox" alt="friebox preview"></a>
<a href="https://pypistats.org/packages/friebox" target="__blank"><img src="https://img.shields.io/pypi/dm/friebox"></a>
<br>
</p>

## 🔎简介

friebox - Android/iOS性能数据的实时采集工具。

我们致力于解决低效、繁琐的测试执行问题，我们的目标是在【Simple Test In friebox】

## 📦环境

- 安装 Python 3.10 + [**Download**](https://www.python.org/downloads/)
- 更新adb包（选择性）<https://developer.android.google.cn/studio/releases/platform-tools?hl=zh_cn>
 Windows版本：<https://dl.google.com/android/repository/platform-tools-latest-windows.zip>
 Mac版本：<https://dl.google.com/android/repository/platform-tools-latest-windows.zip>
 Linux版本：<https://dl.google.com/android/repository/platform-tools-latest-linux.zip>

💡 如果Windows用户需要测试iOS，请先安装Itunes.

- Apple官网：<https://www.apple.com.cn/itunes/>
- Windows版本：<https://apps.microsoft.com/store/detail/itunes/9PB2MZ1ZMB1S?hl=zh_CN&gl=cn&cid=appledotcom&rtc=1&activetab=pivot%3Aoverviewtab>
- Mac版本：https://support.apple.com/kb/dl1977?locale=zh_CN

## 📥安装

```shell
pip install -U friebox # 默认
pip install -i  https://mirrors.ustc.edu.cn/pypi/web/simple -U friebox # 镜像
```

💡 如果你的网络无法通过 [pip install -U friebox] 下载, 可以尝试使用镜像下载，但是可能不是最新版本.

## 🚀启动friebox

```shell
python -m friebox # 默认
python -m friebox --host={ip} --port={port} # 自定义
```

## 🏴󠁣󠁩󠁣󠁭󠁿使用python收集

```python
from friebox.public.apm import APM
# friebox version >= 1.0.0
apm = APM(pkgName='com.bilibili.app.in',deviceId='ca6bd5a5',platform='Android', surfaceview=True, noLog=True)
# apm = APM(pkgName='com.bilibili.app.in', platform='iOS') only supports one device
# surfaceview： False = gfxinfo (Developer - GPU rendering mode - adb shell dumpsys gfxinfo)
# noLog : False (Save test data to log file)
cpu = apm.collectCpu() # %
memory = apm.collectMemory() # MB
flow = apm.collectFlow(wifi=True) # KB
fps = apm.collectFps() # HZ
battery = apm.collectBattery() # level:% temperature:°C current:mA voltage:mV power:w
gpu = apm.collectGpu() # % only supports ios
```

## 🏴󠁣󠁩󠁣󠁭󠁿使用API收集

### 后台启动服务

```shell
# friebox version >= 2.1.5
macOS/Linux: nohup python -m friebox &
Windows: start /min python -m friebox &
```

### 获取请求数据

```shell
Android: http://{ip}:{port}/apm/collect?platform=Android&deviceid=ca6bd5a5&pkgname=com.bilibili.app.in&target=cpu
iOS: http://{ip}:{port}/apm/collect?platform=iOS&pkgname=com.bilibili.app.in&target=cpu
target in ['cpu','memory','network','fps','battery','gpu']
```

## 🔥功能

- **无需ROOT/越狱:** Android设备无需ROOT，iOS设备无需越狱。高效解决Android & iOS性能测试分析难题。

- **数据完整性:** 可提供FPS、Jank、CPU、GPU、Memory、Battery 、Network等性能参数，这些您都可以轻松获得。

- **美观的报告看板:** 报告看板，您可以随时随地存储、可视化、编辑、管理和下载使用任何版本的friebox收集的所有测试数据。

- **好用的监控设置:** 支持在监控过程中设置告警值、收集时长、访问其他PC机器的移动设备。

- **比对模式:** 支持两台移动设备同时对比测试。
🌱2-devices: 使用两台不同的设备测试同一个app。
🌱2-apps: 使用两台配置相同的设备测试两个不同的app。

## 终端

- windows: PowerShell
- macOS：iTerm2 (<https://iterm2.com/>)

## 💕感谢

- <https://github.com/alibaba/taobao-iphone-device>
- <https://github.com/smart-test-ti/SoloX>
