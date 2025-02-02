category = "LF Nodes/Logic"

class SwitchInteger:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "on_true": ("INT", {"default": 0}),
                "on_false": ("INT", {"default": 0}),
                "boolean": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("INT",)
    CATEGORY = category
    FUNCTION = "integer_switch"

    def integer_switch(self, on_true: int, on_false: int, boolean: bool):
        return (on_true if boolean else on_false,)

NODE_CLASS_MAPPINGS = {
    "SwitchInteger": SwitchInteger,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "SwitchInteger": "Switch Integer",
}