import json

import DaVinciResolveScript as dvr_script

resolve = dvr_script.scriptapp("Resolve")

project_manager = resolve.GetProjectManager()

# return bool
# project_manager.OpenFolder("test_create_folder")
# res = project_manager.OpenFolder("test_level1")
# print(res)
# if res:
#     project = project_manager.CreateProject("test_level2_project")
#     project_manager.SaveProject()
#     print(dir(project))

# project_manager.GotoParentFolder()
# project = project_manager.LoadProject("test_py_rename")

# res = project_manager.ExportProject("test_py_rename", "D:/dafenqi/test_export/test_py_rename2.drp", True)

# project = project_manager.GetCurrentProject()

# media_pool = project.GetMediaPool()

# timeline_num = project.GetTimelineCount()

# timeline = project.GetTimelineByIndex(1)

# timeline = project.GetCurrentTimeline()

# timeline_name = timeline.GetName()

# timeline = project.GetTimelineByIndex(1)
# res = project.SetCurrentTimeline(timeline)

# gallery = project.GetGallery()

# project_name = project.GetName()

# res = project.SetName("test_py_rename2_g")

# preset_list = project.GetPresetList()

# res = project.SetPreset("系统配置")

# job_id_str = project.AddRenderJob()

# res = project.DeleteRenderJob("987c99d8-7a58-4665-a2f8-37cf60f97b92")

# res = project.DeleteAllRenderJobs()

# render_job_list = project.GetRenderJobList()

# render_preset_list = project.GetRenderPresetList()

# render_job_list = project.GetRenderJobList()
# print(render_job_list)

# res = project.StartRendering(["a365997d-37de-41a1-bdd3-101c86111a11"], False)

# res = project.StartRendering(False)

# res = project.StopRendering()

# res = project.LoadRenderPreset("YouTube - 1080p")

# res = project.SaveAsNewRenderPreset("YouTube - 1080p - custom")

# res = project.SetRenderSettings({"CustomName": "test_render_file_name"})

# res = project.GetRenderJobStatus("64b77004-425b-4809-9a89-3e561bf48326")

# res = project.GetSetting("Pixel")

# project.SetSetting("superScale", 1)
# res = project.GetSetting("superScale")

# render_format_list = project.GetRenderFormats()

# render_format_codecs_list = project.GetRenderCodecs("mp4")
#
# print(render_format_codecs_list)

# res = project.GetCurrentRenderFormatAndCodec()

# project.SetCurrentRenderFormatAndCodec("mp4", "H265_NVIDIA")
# res = project.GetCurrentRenderFormatAndCodec()

# res = project.GetCurrentRenderMode()

# res = project.SetCurrentRenderMode(1)
# print(res)

# resolution_list = project.GetRenderResolutions("mp4", "H265_NVIDIA")
# print(resolution_list)

# res = project.RefreshLUTList()
# print(res)


# media_storage = resolve.GetMediaStorage()
# mounted_volume_list = media_storage.GetMountedVolumeList()

# folder_list = media_storage.GetSubFolderList("E:\\DaVinci")

# file_list = media_storage.GetFileList("E:\\DaVinci\\test")

# res = media_storage.RevealInStorage("E:\\DaVinci\\test")

# res = media_storage.RevealInStorage("E:\\DaVinci\\test\\task_v001.mp4")

# item_list = media_storage.AddItemListToMediaPool("E:\\DaVinci\\add_media\\test_add.mov")

# item_list = media_storage.AddItemListToMediaPool("E:\\DaVinci\\add_media")


# item_list = media_storage.AddItemListToMediaPool(["E:\\DaVinci\\add_media\\test_add1.mov", "E:\\DaVinci\\add_media\\test_add2.mov"])
# item_list = media_storage.AddItemListToMediaPool(["E:\\DaVinci\\add_media1", "E:\\DaVinci\\add_media2"])

# project = project_manager.GetCurrentProject()
# media_pool = project.GetMediaPool()
# item_list = media_storage.AddItemListToMediaPool(["E:\\DaVinci\\add_media\\test_add1.mov", "E:\\DaVinci\\add_media\\test_add2.mov"])
#
# if len(item_list) > 0:
#     res = media_storage.AddClipMattesToMediaPool(item_list[0], ["E:\\DaVinci\\add_media\\test_add1.mov"], "left")
#     print(res)


# 获取当前项目返回 project 对象
# project = project_manager.GetCurrentProject()

# 获取 MediaPool 对象
# media_pool = project.GetMediaPool()

# 获取当前文件夹返回 folder 对象
# folder = media_pool.GetCurrentFolder()

# clip_list = folder.GetClipList()
# folder_name = folder.GetName()

# folder_list = folder.GetSubFolderList()
# print(folder_list)


# folder = media_pool.GetRootFolder()
# sub_folder = media_pool.AddSubFolder(folder, "test_sub_folder")

# timeline = media_pool.CreateEmptyTimeline("new_test_timeline")

# media_storage = resolve.GetMediaStorage()
# item_list = media_storage.AddItemListToMediaPool(["E:\\DaVinci\\add_media\\test_add1.mov", "E:\\DaVinci\\add_media\\test_add2.mov"])
# timeline_list = media_pool.AppendToTimeline(item_list)
# print(timeline_list)

# project = project_manager.GetCurrentProject()
# media_storage = resolve.GetMediaStorage()
#
# item_list = media_storage.AddItemListToMediaPool(["E:\\DaVinci\\add_media\\test_add1.mov", "E:\\DaVinci\\add_media\\test_add2.mov"])
# if len(item_list) > 0:
#     media_pool = project.GetMediaPool()
#     res = media_pool.AppendToTimeline([{
#         'mediaPoolItem': item_list[0],
#         'startFrame': 1,
#         'endFrame': 10,
#         'mediaType': 1
#     }])


# project = project_manager.GetCurrentProject()
# media_storage = resolve.GetMediaStorage()
#
# item_list = media_storage.AddItemListToMediaPool(["E:\\DaVinci\\add_media\\test_add1.mov", "E:\\DaVinci\\add_media\\test_add2.mov"])
# if len(item_list) > 0:
#     media_pool = project.GetMediaPool()
#     res = media_pool.CreateTimelineFromClips("new_timeline", [{
#         'mediaPoolItem': item_list[0],
#         'startFrame': 1,
#         'endFrame': 10,
#         'mediaType': 1
#     }])

# project = project_manager.GetCurrentProject()
# media_pool = project.GetMediaPool()
#
# res = media_pool.ImportTimelineFromFile("E:\\DaVinci\\timeline\\layout.edl", {
#     "timelineName": "import_timeline_test",
#     "importSourceClips": True,
#     "sourceClipsPath": "E:\\DaVinci\\add_media\\"
# })


# media_storage = resolve.GetMediaStorage()
# timeline = project.GetCurrentTimeline()

# res = media_pool.DeleteTimelines([timeline])

# folder = media_pool.GetCurrentFolder()
# print(folder)

# folder = media_pool.GetRootFolder()
# res = media_pool.SetCurrentFolder(folder)
# print(res)

# res = media_pool.ImportMedia(["E:\\DaVinci\\add_media\\test_add1.mov", "E:\\DaVinci\\add_media\\test_add2.mov"])
# folder = media_pool.GetCurrentFolder()
# clips = folder.GetClipList()
# res = media_pool.ExportMetadata("E:\\DaVinci\\csv\\test_csv2.csv", clips)
# print(res)


project = project_manager.GetCurrentProject()
timeline = project.GetCurrentTimeline()
timeline_name = timeline.GetName()

# print(timeline_name)

# res = timeline.SetName("timeline_new_name")

# start_frame_number = timeline.GetStartFrame()
# end_frame_number = timeline.GetEndFrame()
#
# audio_track_count = timeline.GetTrackCount("audio")
# video_track_count = timeline.GetTrackCount("video")
# subtitle_track_count = timeline.GetTrackCount("subtitle")
#
# first_video_track_items = timeline.GetItemListInTrack("video", 1)
# if first_video_track_items is not None:
#     for item in first_video_track_items:
#         print(item.GetName())

# data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
# json_str = json.dumps(data)
# res = timeline.AddMarker(100.0, "Sky", "marker_name", "marker_note", 100.0, json_str)

# res = timeline.AddMarker(220.0, "Red", "marker_name3", "marker_note3", 220.0, "test_tag2")
# markers = timeline.GetMarkers()
# markers_custom = timeline.GetMarkerByCustomData("test_tag2")

# data = [{'id': 111, 'assets': 'long', 'time_log': 3}]
# json_str = json.dumps(data)
# res = timeline.UpdateMarkerCustomData(220.0, json_str)

# customData = timeline.GetMarkerCustomData(220.0)
# res = timeline.DeleteMarkersByColor("All")
# res = timeline.AddMarker(200.0, "Sky", "marker_name", "marker_note", 200.0)
# print(res)
# res = timeline.DeleteMarkerAtFrame(100.0)
# current_timeline_code = timeline.GetCurrentTimecode()
# res = timeline.SetCurrentTimecode("01:00:20:00")
# current_video_item = timeline.GetCurrentVideoItem()
# current_clipThumbnail = timeline.GetCurrentClipThumbnailImage()
# res = timeline.SetTrackName("video", 1, "新视频")
# track_name = timeline.GetTrackName("video", 1)

# new_timeline = timeline.DuplicateTimeline()

# res = timeline.Export("D:/dafenqi/test_export/test_py_rename2.aaf", resolve.EXPORT_AAF, resolve.EXPORT_AAF_NEW)

# res = timeline.SetSetting("timelineFrameRate", "25")
# timeline_rate = timeline.GetSetting("timelineFrameRate")

# timeline_item = timeline.InsertGeneratorIntoTimeline("10 Step")

# timeline_item = timeline.InsertTitleIntoTimeline("Scroll")

# gallery_still = timeline.GrabStill()

# media_pool = project.GetMediaPool()
# media_pool_items = media_pool.ImportMedia(["E:\\DaVinci\\add_media\\test_add2.mov"])
#
# for media_pool_item in media_pool_items:
    # metadata = media_pool_item.GetMetadata("Keywords")
    # res = media_pool_item.SetMetadata({'Keywords': 'test2,test4'})
    #media_pool_item_id = media_pool_item.GetMediaId()

    #res = media_pool_item.AddMarker(10.0, "Green", "marker_name", "marker_note", 10.0, "test_custom_data")

    #media_pool_item_markers = media_pool_item.GetMarkers()

    #media_pool_item_marker = media_pool_item.GetMarkerByCustomData("test_custom_data")
    #res = media_pool_item.UpdateMarkerCustomData(10.0, "test_custom_data2")
    # media_pool_item_marker = media_pool_item.GetMarkerByCustomData("test_custom_data2")

    # res = media_pool_item.AddFlag("Blue")
    # color_list = media_pool_item.GetFlagList()
    # res = media_pool_item.ClearFlags("Blue")
    # color = media_pool_item.GetClipColor()
    # res = media_pool_item.SetClipColor("Lime")
    # res = media_pool_item.ClearClipColor()
    # item_property = media_pool_item.GetClipProperty()

    # res = media_pool_item.ReplaceClip("E:\\DaVinci\\add_media\\test_add.mov")
    # print(res)

# 获取Gallery对象
# gallery = project.GetGallery()
# gallery_still_album = gallery.GetCurrentStillAlbum()
# # album_name = gallery.GetAlbumName(gallery_still_album)
#
# # res = gallery.SetAlbumName(gallery_still_album, "test_album_name")
#
# gallery_stills = gallery_still_album.GetStills()
# for gallery_still in gallery_stills:
#     label = gallery_still_album.GetLabel(gallery_still)
#     res = gallery_still_album.SetLabel(gallery_still, "test_new_label")
#     print(res)
#
# res = gallery_still_album.ExportStills(gallery_stills, "E:\\DaVinci\\add_media", "to_", "jpg")

# 获取当前时间线video类型的轨道数量
track_count = timeline.GetTrackCount('video')

# 按索引选择指定的视频轨
video_track_items = timeline.GetItemListInTrack('video', 2)

for item in video_track_items:
    # 返回当前片段相对于媒体的起点帧数
    l_offset = item.GetLeftOffset()
    # 返回当前片段相对于媒体的结束帧数
    r_offset = item.GetRightOffset()

    # print(l_offset)
    # print(r_offset)


timeline_item = timeline.GetCurrentVideoItem()
if timeline_item is not None:
    item_name = timeline_item.GetName()
    item_duration = timeline_item.GetDuration()
    item_end_frame = timeline_item.GetEnd()
    fusion_comp_count = timeline_item.GetFusionCompCount()
    item_left_offset = timeline_item.GetLeftOffset()
    item_right_offset = timeline_item.GetRightOffset()
    item_start_frame = timeline_item.GetStart()

    # timeline_item.SetProperty('Pan', -4.0)
    # pan_val = timeline_item.GetProperty('Pan')

    # timeline_item.SetProperty('Tilt', -4.0)
    # tilt_val = timeline_item.GetProperty('Tilt')

    # timeline_item.SetProperty('ZoomY', 1)
    # zoomx_val = timeline_item.GetProperty('ZoomY')

    # timeline_item.SetProperty('CropLeft', 0)
    # zoom_gang_val = timeline_item.GetProperty('DynamicZoomEase')
