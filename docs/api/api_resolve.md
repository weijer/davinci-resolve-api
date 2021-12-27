# Resolve对象

## Resolve.Fusion()

返回 Fusion 对象，是Fusion脚本起点。

> 该对象主要是开发Fusion模块相关功能，不是本手册关注重点！

```python
#!/usr/bin/env python
import DaVinciResolveScript as dvr_script

resolve = dvr_script.scriptapp("Resolve")

# return Fusion object
fusion = resolve.Fusion()
```

## Resolve.GetMediaStorage()

返回要查询和处理媒体存储位置的 MediaStorage 对象。