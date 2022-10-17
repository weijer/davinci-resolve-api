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

# res = timeline.SetName("timeline_new_name")

start_frame_number = timeline.GetStartFrame()
end_frame_number = timeline.GetEndFrame()

audio_track_count = timeline.GetTrackCount("audio")
video_track_count = timeline.GetTrackCount("video")
subtitle_track_count = timeline.GetTrackCount("subtitle")

first_video_track_items = timeline.GetItemListInTrack("video", 1)
if first_video_track_items is not None:
    for item in first_video_track_items:
        print(item.GetName())

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
json_str = json.dumps(data)
res = timeline.AddMarker(100.0, "Sky", "marker_name", "marker_note", 100.0, json_str)

markers = timeline.GetMarkers()
print(markers)
