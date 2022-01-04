# ProjectManager对象

## 获取ProjectManager对象

| 方法                          | 说明            |
|-----------------------------|---------------|
| Resolve.GetProjectManager() | 通过Resolve对象获取 |

## ProjectManager.CreateProject(projectName)

- 返回 Project 对象 或 None

创建项目，如果项目名称（字符串）唯一则创建并返回项目对象，不唯一则返回None。

## ProjectManager.DeleteProject(projectName)

- 返回 Bool

删除当前文件夹下面的指定项目名的项目，注意只能删除当前未加载的项目。

## ProjectManager.LoadProject(projectName)

- 返回 Project 对象 或 None

加载指定项目名项目，如果存在指定项目名称（字符串）则返回项目对象，不存在返回None。

## ProjectManager.GetCurrentProject()

- 返回 Project

获取当前加载的项目对象。

## ProjectManager.SaveProject()

- 返回 Bool

使用自己的名称保存当前加载的项目。如果成功，则返回True。

## ProjectManager.CloseProject(project)

- 返回 Bool

> project 传参为 Project 对象？

关闭指定的项目而不保存。

## ProjectManager.CreateFolder(folderName)

- 返回 Bool

创建文件夹，文件夹名称必须唯一不存在。

## ProjectManager.DeleteFolder(folderName)

- 返回 Bool

删除指定的文件夹（如果存在）。如果成功则返回True。

## ProjectManager.GetProjectListInCurrentFolder()

- 返回 [project names...]

返回当前文件夹中项目名称的列表。

## ProjectManager.GetFolderListInCurrentFolder()

- 返回 [folder names...]

返回当前文件夹中文件夹名称的列表。

## ProjectManager.GotoRootFolder()

- 返回 Bool

打开数据库中的根文件夹。

## ProjectManager.GotoParentFolder()

- 返回 Bool

如果当前文件夹有父文件夹，则打开数据库中当前文件夹的父文件夹。

## ProjectManager.GetCurrentFolder()

- 返回 string

返回当前文件夹名称。

## ProjectManager.OpenFolder(folderName)

- 返回 string

以给定名称打开文件夹。

## ProjectManager.OpenFolder(folderName)

- 返回 Bool

以给定名称打开文件夹。

## ProjectManager.ImportProject(filePath)

- 返回 Bool

从提供的文件路径导入项目，如果成功则返回True。

## ProjectManager.ExportProject(projectName, filePath, withStillsAndLUTs=True)

- 返回 Bool

将项目导出到提供的文件路径，包括静帧和LUT（如果WithStillsAndLUT为True 默认情况下启用）。如果成功则返回True。

## ProjectManager.RestoreProject(filePath)

- 返回 Bool

从提供的文件路径恢复项目，如果成功则返回True。

## ProjectManager.GetCurrentDatabase()

- 返回 {dbInfo}

返回与当前数据库连接对应的字典（带有键“DbType”、“DbName”和可选的“IpAddress”）。

## ProjectManager.GetDatabaseList()

- 返回 [{dbInfo}]

返回与添加到解析的所有数据库相对应的字典项列表（带有键“DbType”、“DbName”和可选的“IpAddress”）

## ProjectManager.SetCurrentDatabase({dbInfo})

- 返回 Bool

将当前数据库连接切换到以下键指定的数据库，并关闭任何打开的项目。

| 参数名       | 字段类型   | 说明                                             |
|-----------|--------|------------------------------------------------|
| DbType    | string | 数据库类型 'Disk' 或者 'PostgreSQL'                   |
| DbName    | string | 数据库名                                           |
| IpAddress | string | PostgreSQL server的IP地址（字符串，可选键-默认为“127.0.0.1”） |
