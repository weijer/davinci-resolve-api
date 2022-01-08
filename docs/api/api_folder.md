# Folder对象

## 获取Folder对象

| 方法                                   | 说明                  |
|--------------------------------------|---------------------|
| MediaPool.GetRootFolder()            | 获取根文件夹返回 folder 对象  |
| MediaPool.AddSubFolder(folder, name) | 添加子文件夹返回 folder 对象  |
| MediaPool.GetCurrentFolder()         | 获取当前文件夹返回 folder 对象 |

```python
import DaVinciResolveScript as dvr_script

resolve = dvr_script.scriptapp("Resolve")

# 获取 ProjectManager 对象
project_manager = resolve.GetProjectManager()

# 获取当前项目返回 project 对象
project = project_manager.GetCurrentProject()

# 获取 MediaPool 对象
media_pool = project.GetMediaPool()

# 获取根文件夹返回 folder 对象
folder = media_pool.GetRootFolder()

# 添加子文件夹返回 folder 对象 
folder = media_pool.AddSubFolder("E:\\DaVinci\\test", "sub")

# 获取当前文件夹返回 folder 对象
folder = media_pool.GetCurrentFolder()

```

## Folder.GetClipList()

- 返回 [clips...]

返回文件夹中clips（items）对象列表。

```python
# return [paths...]
clip_list = folder.GetClipList()
```

## Folder.GetName()

- 返回 string

返回媒体文件夹名称。

```python
# return string
folder_name = folder.GetName()
```

## Folder.GetSubFolderList()

- 返回 [folders...]

返回文件夹中的子文件夹 folder 对象列表。

```python
# return string
folder_list = folder.GetSubFolderList()
```