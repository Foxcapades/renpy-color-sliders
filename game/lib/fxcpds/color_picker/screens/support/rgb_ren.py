import renpy # type: ignore
from renpy.store import InputValue # type: ignore

from ....color_utils.fox_color_ren import hex_to_fox_rgb

"""renpy
init python:
"""


class RGBPicker:

    def __init__(self, original: str):
        self._rgb = hex_to_fox_rgb(original)
        self._last = original

    @property
    def red(self):
        self._course_correction()
        return self._rgb.red

    @property
    def green(self):
        self._course_correction()
        return self._rgb.green

    @property
    def blue(self):
        self._course_correction()
        return self._rgb.blue

    @property
    def hex_string(self):
        self._course_correction()
        return self._rgb.hex

    def _course_correction(self):
        global _color_picker_color
        if _color_picker_color != self._last:
            self._rgb = hex_to_fox_rgb(_color_picker_color)
            self._last = _color_picker_color

    def _update_color(self):
        global _color_picker_color
        _color_picker_color = self._last = self.hex_string

    def set_red(self, value: int):
        self._rgb.set_red(value)
        self._update_color()
        renpy.restart_interaction()

    def set_green(self, value: int):
        self._rgb.set_green(value)
        self._update_color()
        renpy.restart_interaction()

    def set_blue(self, value: int):
        self._rgb.set_blue(value)
        self._update_color()
        renpy.restart_interaction()


class RGBPickerInputValue(InputValue):
    def __init__(self, picker: RGBPicker, value: str, setter: function):
        self.default = False

        self._value = value
        self._picker = picker
        self._setter = setter

    def get_text(self) -> str:
        return str(getattr(self._picker, self._value))

    def set_text(self, value):
        if value == "":
            self._setter(0)
        else:
            try:
                self._setter(int(value))
            except Exception as e:
                pass
