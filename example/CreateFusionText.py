import DaVinciResolveScript as dvr_script

resolve = dvr_script.scriptapp("Resolve")

project_manager = resolve.GetProjectManager()
project = project_manager.GetCurrentProject()
timeline = project.GetCurrentTimeline()

video_track_count = timeline.GetTrackCount("video")
first_video_track_items = timeline.GetItemListInTrack("video", 1)

for item in first_video_track_items:

    if item.GetFusionCompCount() < 1:
        item.AddFusionComp()

    fusion_comp = item.GetFusionCompByIndex(1)

    # 查找文本节点
    text_node_exit = fusion_comp.FindToolByID("TextPlus")

    if not text_node_exit:
        # 不存在文本节点才能创建

        # 创建一个“Text”节点
        text_node = fusion_comp.AddTool("TextPlus")

        # 创建一个“Merge”节点
        merge_node = fusion_comp.AddTool("Merge")

        # 设置文本属性

        # 文本内容
        text_node.StyledText = "EP001-Shot001"

        # 文本字体大小
        text_node.Size = 0.05

        # 文本字体
        text_node.Font = "Microsoft YaHei"

        # 文本位置
        text_node.Center = [0.02, 0.05]

        # 文本对齐模式 -1 为左对齐
        text_node.HorizontalLeftCenterRight = -1

        # 连接节点
        media_in = fusion_comp.FindToolByID("MediaIn")
        media_out = fusion_comp.FindToolByID("MediaOut")
        merge_node.FindMainInput(1).ConnectTo(media_in.FindMainOutput(1))
        merge_node.FindMainInput(2).ConnectTo(text_node.FindMainOutput(1))
        media_out.FindMainInput(1).ConnectTo(merge_node.FindMainOutput(1))

