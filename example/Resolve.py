#!/usr/bin/env python
import DaVinciResolveScript as dvr_script

resolve = dvr_script.scriptapp("Resolve")
fusion = resolve.Fusion()
print(type(fusion))
print(dir(fusion))
