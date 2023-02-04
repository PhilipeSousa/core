"""Test Home Assistant enum utils."""

from enum import auto
import unittest

import pytest

from homeassistant.backports.enum import StrEnum

class TestStrEnum(unittest.TestCase):
    class Cor(StrEnum):
        VERMELHO = "vermelho"
        VERDE = "verde"
        AZUL = "azul"

    def teste_str_enum(self):
        self.assertEqual(str(self.Cor.VERMELHO), "vermelho")
        self.assertEqual(repr(self.Cor.VERMELHO), "<Cor.VERMELHO: 'vermelho'>")

        with self.assertRaises(ValueError):
            _ = self.Cor(123)

    def teste_entrada_nao_suportada_(self):
        with self.assertRaises(TypeError) as context:
            class Cor(StrEnum):
                VERMELHO = 1

        self.assertEqual(str(context.exception), "1 não é uma string")

    def testa_auto_nao_eh_suportado(self):
        with self.assertRaises(TypeError) as context:
            class Cor(StrEnum):
                VERMELHO = auto()

        self.assertEqual(str(context.exception), "auto() não é suportado por essa implementação")
