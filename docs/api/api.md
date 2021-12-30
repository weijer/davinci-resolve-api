# 基本API

下面介绍了一些常用的API函数（*）。与resolve对象一样，每个对象都可以检查其属性和函数。

## 主要对象列表

| 对象名           | 说明                           | 怎么获取                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resolve       | Resolve对象是通过Resolve编写脚本的基本起点 | 通过环境变量加载                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Fusion        | 该对象主要是开发Fusion模块相关功能         | Resolve.Fusion()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| MediaStorage  | 查询和处理媒体存储位置的对象               | Resolve.MediaStorage()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ProjectManager | 返回当前打开的数据库的项目管理器对象           | Resolve.ProjectManager()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Project       | 项目操作对象                       | ProjectManager.CreateProject(projectName)<br/>ProjectManager.LoadProject(projectName)<br/>ProjectManager.GetCurrentProject()                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| MediaPool | 媒体池操作对象                      | Project.GetMediaPool()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| MediaPoolItem | 媒体池单个对象                      | MediaStorage.AddTimelineMattesToMediaPool([paths])  <br/>  MediaPool.GetTimelineMatteList(Folder)  <br/>  MediaPool.ImportMedia([items...])  <br/> MediaPool.ImportMedia([{clipInfo}])   <br/> TimelineItem.GetMediaPoolItem()                                                                                                                                                                                                                                                                                                                                     |
| Timeline | 时间线操作对象                      | MediaPool.CreateEmptyTimeline(name)  <br/> MediaPool.CreateTimelineFromClips(name, clip1, clip2,...)  <br/> MediaPool.CreateTimelineFromClips(name, [clips])  <br/> MediaPool.CreateTimelineFromClips(name, [{clipInfo}]) <br/> MediaPool.ImportTimelineFromFile(filePath, {importOptions}) <br/> Timeline.DuplicateTimeline(timelineName)                                                                                                                                                                                                                         |
| TimelineItem | 时间线单个对象                      | MediaPool.AppendToTimeline(clip1, clip2, ...)  <br/> MediaPool.AppendToTimeline([clips]) <br/> MediaPool. AppendToTimeline([{clipInfo}, ...]) <br/>   Timeline.CreateCompoundClip([timelineItems], {clipInfo})  <br/> Timeline.CreateFusionClip([timelineItems])  <br/> Timeline.InsertGeneratorIntoTimeline(generatorName) <br/> Timeline.InsertFusionGeneratorIntoTimeline(generatorName) <br/> Timeline.InsertOFXGeneratorIntoTimeline(generatorName) <br/> Timeline.InsertTitleIntoTimeline(titleName) <br/> Timeline.InsertFusionTitleIntoTimeline(titleName) |
| Gallery | 画廊操作对象                       | Project.GetGallery()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| GalleryStill | 画廊静帧对象                       | Timeline.GrabStill() <br/> Timeline.GrabAllStills(stillFrameSource)  <br/> Timeline.GetStills()                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| GalleryStillAlbum | 画廊静帧专辑对象                     | Gallery.GetCurrentStillAlbum() <br/>   Gallery.GetGalleryStillAlbums()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Folder | 文件夹操作对象                      | MediaPool.GetRootFolder()   <br/> MediaPool.AddSubFolder(folder, name)  <br/>  MediaPool.GetCurrentFolder()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## 加载 fusionscript 文件

默认获取读取 RESOLVE_SCRIPT_LIB 系统环境变量，如果没有配置环境变量则会按照下面默认路径去加载：

> 当然你可以手动直接指认你当前 fusionscript 文件来得到 Resolve 模块

### DaVinciResolveScript.py 源码

**python2.x示例**

```python
import sys
import imp

script_module = None
try:
    import fusionscript as script_module
except ImportError:
    # Look for installer based environment variables:
    import os

    lib_path = os.getenv("RESOLVE_SCRIPT_LIB")
    if lib_path:
        try:
            script_module = imp.load_dynamic("fusionscript", lib_path)
        except ImportError:
            pass
    if not script_module:
        # Look for default install locations:
        ext = ".so"
        if sys.platform.startswith("darwin"):
            path = "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/"
        elif sys.platform.startswith("win") or sys.platform.startswith("cygwin"):
            ext = ".dll"
            path = "C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\"
        elif sys.platform.startswith("linux"):
            path = "/opt/resolve/libs/Fusion/"

        try:
            script_module = imp.load_dynamic("fusionscript", path + "fusionscript" + ext)
        except ImportError:
            pass

if script_module:
    sys.modules[__name__] = script_module
else:
    raise ImportError("Could not locate module dependencies")

```

**python3.5以上版本示例**
```python
import sys
from importlib import machinery


def load_dynamic(name, file_path):
    """
    Load an extension module.
    """
    loader = machinery.ExtensionFileLoader(name, file_path)
    spec = machinery.ModuleSpec(name=name, loader=loader, origin=file_path)
    return loader.create_module(spec)


script_module = None
try:
    import fusionscript as script_module
except ImportError:
    # Look for installer based environment variables:
    import os

    lib_path = os.getenv("RESOLVE_SCRIPT_LIB")

    if lib_path:
        try:
            script_module = load_dynamic("fusionscript", lib_path)
        except ImportError:
            pass
    if not script_module:
        # Look for default install locations:
        ext = ".so"
        if sys.platform.startswith("darwin"):
            path = "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/"
        elif sys.platform.startswith("win") or sys.platform.startswith("cygwin"):
            ext = ".dll"
            path = "C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\"
        elif sys.platform.startswith("linux"):
            path = "/opt/resolve/libs/Fusion/"

        try:
            script_module = load_dynamic("fusionscript", path + "fusionscript" + ext)
        except ImportError:
            pass

if script_module:
    sys.modules[__name__] = script_module
else:
    raise ImportError("Could not locate module dependencies")
```

## 获取 Resolve 对象

```python
import DaVinciResolveScript as dvr_script

resolve = dvr_script.scriptapp("Resolve")
```





