init python:
    def _color_picker_preview_cb(st, at, **kwargs):
        global _color_picker_color
        return (Solid(_color_picker_color), 0.0)

default _color_picker_color = "#9cb9cb"
default _color_picker_tab = "RGB"

image _color_picker_preview = DynamicDisplayable(_color_picker_preview_cb)
