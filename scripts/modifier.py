#!/usr/bin/env python3

import importlib.util
from pathlib import Path
import sys

PATH = Path(__file__).parent
LAST_OS_PATH = PATH / "last_os"
if not LAST_OS_PATH.exists():
    LAST_OS_PATH.write_text("")
if LAST_OS_PATH.read_text().strip() == sys.platform:
    sys.exit(0)
LAST_OS_PATH.write_text(sys.platform)


def import_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


for i in (PATH / "modifiers").rglob("*.py"):
    module = import_from_path(i.stem, i.absolute())
    if getattr(module, "to", None):
        try:
            module.to()
        except Exception as e:
            print(f"Error in {i.stem}: {e}")
    else:
        if sys.platform == "win32":
            try:
                module.to_windows()
            except Exception as e:
                print(f"Error in {i.stem}: {e}")
        elif sys.platform == "linux":
            try:
                module.to_linux()
            except Exception as e:
                print(f"Error in {i.stem}: {e}")
