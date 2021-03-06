import sys
from importlib import machinery


def load_dynamic(name, file_path):
    """
    Load an extension module.
    """
    loader = machinery.ExtensionFileLoader(name, file_path)
    spec = machinery.ModuleSpec(name=name, loader=loader, origin=file_path)
    return loader.create_module(spec)


script_module = None
try:
    import fusionscript as script_module
except ImportError:
    # Look for installer based environment variables:
    import os

    lib_path = os.getenv("RESOLVE_SCRIPT_LIB")

    if lib_path:
        try:
            script_module = load_dynamic("fusionscript", lib_path)
        except ImportError:
            pass
    if not script_module:
        # Look for default install locations:
        ext = ".so"
        if sys.platform.startswith("darwin"):
            path = "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/"
        elif sys.platform.startswith("win") or sys.platform.startswith("cygwin"):
            ext = ".dll"
            path = "C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\"
        elif sys.platform.startswith("linux"):
            path = "/opt/resolve/libs/Fusion/"

        try:
            script_module = load_dynamic("fusionscript", path + "fusionscript" + ext)
        except ImportError:
            pass

if script_module:
    sys.modules[__name__] = script_module
else:
    raise ImportError("Could not locate module dependencies")
