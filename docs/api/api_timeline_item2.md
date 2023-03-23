# TimelineItem对象

## 获取TimelineItem对象

| 方法                                                       | 说明                   |
|----------------------------------------------------------|----------------------|
| Timeline.CreateCompoundClip([timelineItems], {clipInfo}) | 返回 TimelineItem 对象   |
| Timeline.CreateFusionClip([timelineItems])               | 返回 TimelineItem 对象   |
| GetItemListInTrack(trackType, index)                     | 返回 TimelineItem 对象列表 |
| GetCurrentVideoItem()                                    | 返回 TimelineItem 对象   |
| InsertGeneratorIntoTimeline(generatorName)               | 返回 TimelineItem 对象   |
| InsertFusionGeneratorIntoTimeline(generatorName))        | 返回 TimelineItem 对象   |
| InsertOFXGeneratorIntoTimeline(generatorName)            | 返回 TimelineItem 对象   |
| InsertTitleIntoTimeline(titleName)                       | 返回 TimelineItem 对象   |
| InsertFusionTitleIntoTimeline(titleName)                 | 返回 TimelineItem 对象   |

```python
import DaVinciResolveScript as dvr_script

resolve = dvr_script.scriptapp("Resolve")

# 获取 ProjectManager 对象
project_manager = resolve.GetProjectManager()

# 获取当前项目返回 project 对象
project = project_manager.GetCurrentProject()

# 获取当前激活的时间线
timeline = project.GetCurrentTimeline()

# 获取当前时间线video类型的轨道数量
track_count = timeline.GetTrackCount('video')

# 按索引选择指定的视频轨1
video_track_items = timeline.GetItemListInTrack('video', 1)
```

## TimelineItem.GetName()

- 返回 string

返回时间线项对象名称。

```python
# return string
timeline_item = timeline.GetCurrentVideoItem() 
item_name = timeline_item.GetName()
```

## TimelineItem.GetDuration()

- 返回 int

返回时间线项对象持续时间。

```python
# return int
timeline_item = timeline.GetCurrentVideoItem() 
item_duration = timeline_item.GetDuration()
```

## TimelineItem.GetEnd()

- 返回 int

返回时间线项对象时间线上的结束帧位置。

```python
# return int
timeline_item = timeline.GetCurrentVideoItem() 
item_end_frame = timeline_item.GetEnd()
```

## TimelineItem.GetFusionCompCount()

- 返回 int

返回与时间线项目关联的Fusion合成数。

```python
# return int
timeline_item = timeline.GetCurrentVideoItem() 
fusion_comp_count = timeline_item.GetFusionCompCount()
```

## TimelineItem.GetFusionCompByIndex(compIndex)

- 返回 fusionComp

返回基于给定索引的Fusion合成对象。1<=compIndex<=timelineItem.GetFusionCompCount()。

```python
# return fusionComp
timeline_item = timeline.GetCurrentVideoItem() 
fusion_comp_obj = timeline_item.GetFusionCompByIndex(1)
```

## TimelineItem.GetFusionCompNameList()

- 返回 [names...]

返回与时间线项目关联的Fusion合成名称的列表。

```python
# return [names...]
timeline_item = timeline.GetCurrentVideoItem() 
fusion_comp_name_list = timeline_item.GetFusionCompNameList()
```

## TimelineItem.GetFusionCompByName(compName)

- 返回 fusionComp

返回基于给定名称的Fusion合成对象。

```python
# return fusionComp
timeline_item = timeline.GetCurrentVideoItem() 
fusion_comp_obj = timeline_item.GetFusionCompByName('test')
```

![start_render_all_jobs](./../images/clip_offset.jpg)

## TimelineItem.GetLeftOffset()

- 返回 int

返回相对片段左边偏移量（剪辑后片段相当于原片段的起始帧）

```python
# return int
timeline_item = timeline.GetCurrentVideoItem() 
item_left_offset = timeline_item.GetLeftOffset()
```

## TimelineItem.GetRightOffset()

- 返回 int

相对片段右边偏移量（剪辑后片段相当于原片段的结束帧）

```python
# return int
timeline_item = timeline.GetCurrentVideoItem() 
item_right_offset = timeline_item.GetRightOffset()
```

## TimelineItem.GetStart()

- 返回 int

返回时间线项对象在时间线上的开始帧位置。

```python
# return int
timeline_item = timeline.GetCurrentVideoItem() 
item_start_frame = timeline_item.GetStart()
```