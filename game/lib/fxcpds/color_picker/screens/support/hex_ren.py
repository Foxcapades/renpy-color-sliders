from renpy.store import InputValue # type: ignore
import renpy # type: ignore

from ....color_utils.fox_hex_utils_ren import fox_hex_is_valid, __is_hex_digit


"""renpy
init python:
"""


class HexInputValue(InputValue):
    def __init__(self, var_name: str):
        self.default = False

        self._var_name = var_name
        self._value = self._last = getattr(renpy.store, self._var_name)

    def get_text(self) -> str:
        attr = getattr(renpy.store, self._var_name)[1:]

        if attr == self._last:
            return self._value
        else:
            self._last = self._value = attr
            return attr

    def set_text(self, text: str):
        if fox_hex_is_valid(text):
            self._value = text

            l = len(text)
            if l == 3 or l == 6:
                setattr(renpy.store, self._var_name, '#' + text)

        renpy.restart_interaction()
