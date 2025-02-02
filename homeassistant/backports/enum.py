"""Enum backports from standard lib."""
from __future__ import annotations

from enum import Enum
from typing import Any, TypeVar

_StrEnumSelfT = TypeVar("_StrEnumSelfT", bound="StrEnum")

class StrEnum(str, Enum):
    def __str__(self):
        return self.value

    def __new__(
        cls: type[_StrEnumSelfT], value: str, *args: Any, **kwargs: Any
    ) -> _StrEnumSelfT:

        if not isinstance(value, str):
            raise TypeError(f"{value!r} não é uma string")
        return super().__new__(cls, value, *args, **kwargs)

    def _generate_next_value_(
        name: str, start: int, count: int, last_values: list[Any]
    ) -> Any:
        raise TypeError("auto() não é suportado por essa implementação")
