from unittest import TestCase
import Practicas.Ejercicio_1 as e

class oruebas_ejercicio_1(TestCase):
    def test_Numero_Flotante(self):
        self.assertEqual(e.Numero_Flotante(-14),"El numero es negativo")
