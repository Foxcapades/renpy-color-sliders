import renpy # type: ignore
from renpy.store import InputValue # type: ignore

from ....color_utils.fox_color_ren import hex_to_fox_rgb

"""renpy
init python:
"""


class HSVPicker:
    def __init__(self, original: str):
        self._hsv = hex_to_fox_rgb(original).to_hsv()
        self._last = original

    ############################################################################
    #
    #   Properties
    #
    ############################################################################

    @property
    def hue(self) -> int:
        self._course_correction()
        return self._hsv.hue

    @property
    def saturation(self) -> int:
        self._course_correction()
        return int(self._hsv.saturation * 100)

    @property
    def value(self) -> int:
        self._course_correction()
        return int(self._hsv.value * 100)

    @property
    def hex_string(self) -> str:
        self._course_correction()
        return self._hsv.hex

    ############################################################################
    #
    #   Internal Methods
    #
    ############################################################################

    def _course_correction(self):
        global _color_picker_color
        if _color_picker_color != self._last:
            self._hsv = hex_to_fox_rgb(_color_picker_color).to_hsv()
            self._last = _color_picker_color

    def _update_color(self):
        global _color_picker_color
        _color_picker_color = self._last = self.hex_string

    ############################################################################
    #
    #   Public Methods
    #
    ############################################################################

    def set_hue(self, hue: int):
        if not (0 <= hue < 360):
            raise Exception("invalid hue value")
        self._hsv.set_hue(hue)
        self._update_color()
        renpy.restart_interaction()

    def set_saturation(self, saturation: int):
        if not (0 <= saturation <= 100):
            raise Exception("invalid saturation value")
        self._hsv.set_saturation(saturation / 100)
        self._update_color()
        renpy.restart_interaction()

    def set_value(self, value: int):
        if not (0 <= value <= 100):
            raise Exception("invalid value value")
        self._hsv.set_value(value / 100)
        self._update_color()
        renpy.restart_interaction()


class HSVPickerInputValue(InputValue):
    def __init__(self, picker: HSVPicker, value: str, setter: function):
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