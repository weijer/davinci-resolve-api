# Fusion对象

本对象不是 DaVinci Resolve 开发手册重点，手册没有说明该对象的方法，通过 dir() 函数打印观测。

```python
import DaVinciResolveScript as dvr_script

resolve = dvr_script.scriptapp("Resolve")

# return Bool
fusion = resolve.Fusion()

print(dir(fusion))
```

```
['ActionManager', 'AddConfig', 'AllowNetwork', 'AskQuit', 'BinManager', 'Bins', 'Build', 'CacheManager', 'ClearFileLog', 'ClearRecentCompList', 'Comp', 'Composition', 'Copy', 'CreateFloatingView', 'CreateMail', 'CurrentComp', 'CurrentFrame', 'CustomizeHotkeys', 'CustomizeToolbars', 'CustomizeToolbars', 'Cut', 'DeactivateLicense', 'Delete', 'DeselectAll', 'DoAction', 'DumpGLObjects', 'DumpGraphicsHardwareInfo', 'EditScript', 'Execute', 'FileLogging', 'FindReg', 'FontManager', 'GetActiveFrameIndex', 'GetActiveFrameIndex', 'GetActiveWndIndex', 'GetActiveWndIndex', 'GetAppInfo', 'GetArgs', 'GetCPULoad', 'GetClipboard', 'GetCompList', 'GetCurrentComp', 'GetData', 'GetData', 'GetEnv', 'GetFairlight', 'GetFrameNameIndex', 'GetGlobalPathMap', 'GetID', 'GetMainWindow', 'GetModifiers', 'GetMouseButtons', 'GetMousePos', 'GetNumRecentFiles', 'GetPrefs', 'GetPreviewList', 'GetRLMLicenseInfo', 'GetRecentCompList', 'GetRecentFileName', 'GetReg', 'GetRegAttrs', 'GetRegList', 'GetRegSummary', 'GetResolve', 'GetToolIcon', 'GetToolList', 'GetUILayout', 'GetVersion', 'GetWndNameIndex', 'HotkeyManager', 'InstallFile', 'IsConsoleShowing', 'IsNetworkAllowed', 'IsUIVisible', 'IsUIVisible', 'IsUtilityOpen', 'LoadComp', 'LoadPrefs', 'LoadRecentComp', 'MapPath', 'MapPathSegments', 'MenuManager', 'MouseX', 'MouseY', 'NewComp', 'NewFloatFrame', 'NewImageView', 'NewScript', 'NewTabbedFrame', 'OpenFile', 'OpenLibrary', 'OpenLibraryStudio', 'Paste', 'PasteSettings', 'Print', 'QueueAction', 'QueueComp', 'QueueManager', 'Quit', 'RemoveConfig', 'RenderManager', 'RequestDir', 'RequestFile', 'ReverseMapPath', 'RunScript', 'SavePrefs', 'SelectAll', 'SetActiveFrameIndex', 'SetActiveFrameIndex', 'SetActiveWndIndex', 'SetActiveWndIndex', 'SetBatch', 'SetClipboard', 'SetData', 'SetData', 'SetFusionApp', 'SetMasterApp', 'SetOnlyActiveComp', 'SetPrefs', 'SetUILayout', 'ShowAbout', 'ShowActions', 'ShowConsole', 'ShowHelp', 'ShowMenu', 'ShowPrefs', 'ShowUI', 'ShowUI', 'ShowWindow', 'Sleep', 'Test', 'ToggleBins', 'ToggleRenderManager', 'ToggleUtility', 'TriggerEvent', 'UIManager', 'UpdateMenus', 'Version', '_MasterApp_Active', '_Memory_Purge', '_NewComp', '_Output_Error', '_Output_Print']
```

