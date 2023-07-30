import renpy # type: ignore
from renpy.store import InputValue # type: ignore

from ...colors.cshsl_ren import CSHSL
from ...utils.hex_color_ren import _parse_hex


"""renpy
init python:
"""


class HSLPicker:
    def __init__(self, original: str):
        self._hsl = _parse_hex(original).to_hsl()
        self._last = original

    ############################################################################
    #
    #   Properties
    #
    ############################################################################

    @property
    def hue(self) -> int:
        self._course_correction()
        return self._hsl.hue

    @property
    def saturation(self) -> int:
        self._course_correction()
        return int(self._hsl.saturation * 100)

    @property
    def lightness(self) -> int:
        self._course_correction()
        return int(self._hsl.lightness * 100)

    @property
    def hex_string(self) -> str:
        self._course_correction()
        return self._hsl.to_rgb().hex_string

    ############################################################################
    #
    #   Internal Methods
    #
    ############################################################################

    def _course_correction(self):
        global _color_picker_color
        if _color_picker_color != self._last:
            self._hsl = _parse_hex(_color_picker_color).to_hsl()
            self._last = _color_picker_color
            print(_color_picker_color)

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
        self._hsl.set_hue(hue)
        self._update_color()
        renpy.restart_interaction()

    def set_saturation(self, saturation: int):
        if not (0 <= saturation <= 100):
            raise Exception("invalid saturation value")
        self._hsl.set_saturation(saturation / 100)
        self._update_color()
        renpy.restart_interaction()

    def set_lightness(self, lightness: int):
        if not (0 <= lightness <= 100):
            raise Exception("invalid lightness value")
        self._hsl.set_lightness(lightness / 100)
        self._update_color()
        renpy.restart_interaction()


class HSLPickerInputValue(InputValue):
    def __init__(self, picker: HSLPicker, value: str, setter: function):
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