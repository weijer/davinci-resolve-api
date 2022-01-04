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

## python脚本获取 Resolve 对象

### 加载 fusionscript 文件

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

### 获取 Resolve 对象

```python
import DaVinciResolveScript as dvr_script

resolve = dvr_script.scriptapp("Resolve")
```

## node.js 脚本获取 Resolve 对象

当前以 windows 环境为例，其他操作系统去 xxx\DaVinci Resolve\Support\Developer\Workflow Integrations\Examples\SamplePlugin 目录下找对应文件

> 调用 WorkflowIntegration.node 模块，代码无法脱离 DaVinci Resolve 对立运行，必须放在
> 
>  Mac OS X:
> 
>  "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Workflow Integration Plugins/"
> 
>  Windows:
> 
>  "%PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Support\Workflow Integration Plugins\"

### WorkflowIntegration module API

js要与Resolve交互，需要在你的js插件应用中使用 WorkflowIntegration.node Node.js 模块。 下面是与Resolve通信的WorkflowIntegration（模块）JavaScript API函数。

```javascript
const WorkflowIntegration = require('./WorkflowIntegration.node');
```

| 方法名                                      | 返回类型     | 说明                                                                                                                                |
|------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------|
| WorkflowIntegration.Initialize(pluginId) | Bool     | 如果初始化成功，则返回true，否则返回false。 pluginId 是从 manifest.xml 配置文件中读取的插件唯一 Id 字符串                                                           |
| WorkflowIntegration.GetResolve()         | Resolve  | 获取返回 Resolve 对象                                                                                                                   |
| WorkflowIntegration.RegisterCallback(callbackName, callbackFunc) | Bool | 如果输入回调名称/函数注册成功，则返回true，否则返回false </br>  callbackName 应为有效的支持回调字符串名称（具体请看下方支持回调函数列表）  </br> callbackFunc 应该是没有任何参数的有效JavaScript函数 |
| WorkflowIntegration.DeregisterCallback(callbackName) |Bool| 如果成功取消注册输入回调名称，则返回true，否则返回false                                                                                                  |
| WorkflowIntegration.CleanUp() |Bool| 如果清除成功，则返回true，否则返回false。这应该在插件应用程序退出时调用。                                                                                         |
| WorkflowIntegration.SetAPITimeout(valueInSecs)  |Bool| 默认情况下API不会超时。要启用超时，请在参数 valueInsenses 中设置一个非零正整数值。 </br>  将其设置为0将禁用超时。如果超时设置/重置成功，此函数将返回true。                                     |

### 支持回调函数列表

请注意，JavaScript API没有基于控制台的支持。

| 函数名 |
|-----|
|RenderStart|
|RenderStop|

### manifest.xml 配置文件

| 参数节点 | 说明       |
|-----|----------|
|Id| 插件唯一标识id |
|Name| 插件名称     |
|Version | 插件版本     |
|Description| 插件描述     |
|FilePath| js主入口文件  |

```xml
<?xml version="1.0" encoding="UTF-8"?>
<BlackmagicDesign>
    <Plugin>
        <Id>com.blackmagicdesign.resolve.sampleplugin</Id>
        <Name>Sample Plugin</Name>
        <Version>1.0</Version>
        <Description>Sample Plugin</Description>
        <FilePath>main.js</FilePath>
    </Plugin>
</BlackmagicDesign>
```
### Workflow Integration Plugins 插件文件目录结构

```
.
├── com.<company>.<plugin_name>    插件目录
│   ├── package.json               包信息
│   ├── main.js                    入口文件
│   ├── index.html                 html 文件
│   ├── manifest.xml               插件xml描述文件
│   ├── WorkflowIntegration.node   WorkflowIntegration node.js 模块
│   ├── node_modules               第三方npm包
│   │   └── <Node.js modules>
│   ├── js                         js 文件
│   │   └── <supporting js files>
│   ├── css                        css 文件
│   │   └──  <css files containing styling info>
│   ├── img                        img 图片资源文件
│   │   └──  <image files>
......
```

### 加载 Resolve 对象

```javascript
const WorkflowIntegration = require('./WorkflowIntegration.node');
isInitialized = WorkflowIntegration.Initialize('com.blackmagicdesign.resolve.sampleplugin');
if (isInitialized) {
    resolve = WorkflowIntegration.GetResolve();
}
```

## UI 组件

DaVinci Resolve 有三种写UI方式：

1. html+css 基于内置的 Electron 模块运行（类似微信小程序玩法了）
2. fusion.UIManager 内置提供了 fusion UI 组件
3. 使用第三方 PyQt（PySide）ui 组件

> 不推荐 fusion UI 组件，因为软件之间不通用直接 pass，感兴趣的自行去看官方文档
> 
> 至于 html+css 还是用 QT 来写 ui 看你司的人员技术实力
> 
> 个人更推荐使用 html+css 这种模式，在 vue.js 加持下写页面非常快，人员成本也相对较低