from renpy.store import InputValue # type: ignore
import renpy # type: ignore

from ...utils.hex_color_ren import _validate_hex


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
        l = len(text)

        print(text)

        if l == 3 or l == 6:
            tmp = '#' + text
            try:
                _validate_hex(tmp)
                setattr(renpy.store, self._var_name, tmp)
            except:
                pass
        self._value = text
        renpy.restart_interaction()
