# 基本API

下面介绍了一些常用的API函数（*）。与resolve对象一样，每个对象都可以检查其属性和函数。

## 主要对象列表

| 对象名            | 说明                           | 怎么获取                                                            |
|----------------|------------------------------|-----------------------------------------------------------------|
| Resolve        | Resolve对象是通过Resolve编写脚本的基本起点 | 通过环境变量加载                                                        |
| Fusion         | 该对象主要是开发Fusion模块相关功能         | Resolve.Fusion()                                                |
| MediaStorage   | 查询和处理媒体存储位置的对象               | Resolve.MediaStorage()                                          |
| ProjectManager | 返回当前打开的数据库的项目管理器对象           | Resolve.ProjectManager()                                        |
| Project        | 项目操作对象                       | ProjectManager.CreateProject(projectName)<br/>ProjectManager.LoadProject(projectName)<br/>ProjectManager.GetCurrentProject() |
| MediaPool | | |
| MediaPoolItems | | |
| Timeline | | |
| TimelineItem | | |
| Gallery | | |
| GalleryStillAlbum | | |
| GalleryStill | | |
| Folder | | |