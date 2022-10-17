# Timeline对象

## 获取Timeline对象

| 方法                                                          | 说明                |
|-------------------------------------------------------------|-------------------|
| Project.GetTimelineByIndex(idx)                             | 通过索引号获取时间线对象      |
| Project.GetCurrentTimeline()                                | 获取当前激活的时间线对象      |
| MediaPool.CreateEmptyTimeline(name)                         | 媒体池创建空时间线，返回时间线对象 |
| MediaPool.CreateTimelineFromClips(name, clip1, clip2,...)   | 媒体池创建时间线，返回时间线对象  |
| MediaPool.CreateTimelineFromClips(name, [clips])            | 媒体池创建时间线，返回时间线对象  |
| MediaPool.CreateTimelineFromClips(name, [{clipInfo}])       | 媒体池创建时间线，返回时间线对象  |
| MediaPool.ImportTimelineFromFile(filePath, {importOptions}) | 媒体池导入时间线，返回时间线对象  |
| Timeline.DuplicateTimeline(timelineName)                    | 复制时间线，返回时间线对象     |

```python
import DaVinciResolveScript as dvr_script

resolve = dvr_script.scriptapp("Resolve")

# 获取 ProjectManager 对象
project_manager = resolve.GetProjectManager()

# 获取当前项目返回 project 对象
project = project_manager.GetCurrentProject()

# 获取 Timeline 对象
timeline = project.GetCurrentTimeline()
```

## Timeline.GetName()

- 返回 string

返回当前时间线的名称。

```python
# return string
timeline_name = timeline.GetName()
```

## Timeline.SetName(timelineName)

- 返回 Bool

设置当前时间线的名称，名称需要唯一，如果成功返回 True 反之 False。

```python
# return string
res = timeline.SetName("timeline_new_name")
```

## Timeline.GetStartFrame()

- 返回 int

获取当前时间线开始帧数。

![layout_preset](./../images/timeline_start_frame.jpg)

```python
# return int
start_frame_number = timeline.GetStartFrame()
```

## Timeline.GetEndFrame()

- 返回 int

获取当前时间线结束帧数。

```python
# return int
end_frame_number = timeline.GetEndFrame()
```

## Timeline.GetTrackCount(trackType)

- 返回 int

获取当前时间线对象上指定类型轨道的数量。

| 类型       | 说明  |
|----------|-----|
| audio    | 音频  |
| video    | 视频  |
| subtitle | 字幕  |

```python
# return int
audio_track_count = timeline.GetTrackCount("audio")
video_track_count = timeline.GetTrackCount("video")
subtitle_track_count = timeline.GetTrackCount("subtitle")
```

## Timeline.GetItemListInTrack(trackType, index)

- 返回 [items...]

获取当前时间线指定类型（audio，video，subtitle）和指定轨道索引（index 从1开始）的所有 TimelineItem 对象。

```python
# return [items...]
first_video_track_items = timeline.GetItemListInTrack("video", 1)
```

## Timeline.AddMarker(frameId, color, name, note, duration, customData)

- 返回 Bool

给指定时间线范围增加标记点数据。

| 参数         | 说明                                                                                                                                                             |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| frameId    | 起始帧，单位为秒                                                                                                                                                       |
| color      | 颜色 蓝色（Blue）,青色（Cyan），绿色（Green），黄色（Yellow），红色（Red），粉色（Pink），紫色（Purple），紫红（Fuchsia），玫红（Rose），淡紫（Lavender），淡蓝（Sky），亮绿（Mint），亮黄（Lemon），金色（Sand），深棕（Sand），乳白（Cream） |
| name       | 标记名称                                                                                                                                                           |
| note       | 标记描述                                                                                                                                                           |
| duration   | 标记持续时间，单位为秒                                                                                                                                                    |
| customData | 自定义数据，字符串类型，可以写入json字符串                                                                                                                                        |

```python
# return Bool
res = timeline.AddMarker(100.0, "Green", "marker_name", "marker_note", 100.0, "test_custom_data")

data = [{'id': 111, 'assets': 'long', 'time_log': 3}]
json_str = json.dumps(data)
res = timeline.AddMarker(100.0, "Sky", "marker_name", "marker_note", 100.0, json_str)
```

## Timeline.GetMarkers()

- 返回 {markers...}

返回当前时间线所有标记点字典，格式为(frameId -> {information})

```python
# return Bool
markers = timeline.GetMarkers()
# {100: {'color': 'Sky', 'duration': 100, 'note': 'marker_note', 'name': 'marker_name', 'customData': '[{"id": 111, "assets": "long", "time_log": 3}]'}}
```

## Timeline.GetMarkerByCustomData(customData)

- 返回 {markers...}

返回具有指定customData的第一个匹配标记的标记{information}。


