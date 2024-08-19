import sys
import folder_paths

custom_nodes = folder_paths.get_folder_paths("custom_nodes")
for dir in custom_nodes:
    if dir not in sys.path:
        print("Adding", dir, "to sys.path")
        sys.path.append(dir)

from .nodes.json import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
from .nodes.llm import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
from .nodes.logic import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
from .nodes.workflow import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
