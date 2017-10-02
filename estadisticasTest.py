from unittest import TestCase
from Estadisiticas import Estadisticas


class estadisticasTest(TestCase):
    def test_getEstadisticas_vacia(self):
        estadistica = Estadisticas().getEstadisticas("")
        self.assertEqual(estadistica[0], 0, "Cadena vacia - Num. elementos")
        self.assertEqual(estadistica[1], None, "Cadena vacia - Minimo")
        self.assertEqual(estadistica[2], None, "Cadena vacia - Maximo")
        self.assertEqual(estadistica[3], None, "Cadena vacia - Promedio")

    def test_getEstadisticas_UnNumero(self):
        estadistica = Estadisticas().getEstadisticas("5")
        self.assertEqual(estadistica[0], 1, "Con un numero - Num. elementos")
        self.assertEqual(estadistica[1], 5, "Con un numero - Minimo")
        self.assertEqual(estadistica[2], 5, "Con un numero - Maximo")
        self.assertEqual(estadistica[3], 5, "Con un numero - Promedio")

    def test_getEstadisticas_DosNumeros(self):
        estadistica = Estadisticas().getEstadisticas("4,1")
        self.assertEqual(estadistica[0], 2, "Con dos numeros - Num. elementos")
        self.assertEqual(estadistica[1], 1, "Con dos numeros - Minimo")
        self.assertEqual(estadistica[2], 4, "Con dos numeros - Maximo")
        self.assertEqual(estadistica[3], 2.5, "Con dos numeros - Promedio")

    def test_getEstadisticas_NNumeros(self):
        estadistica = Estadisticas().getEstadisticas("5,4,8,5,2")
        self.assertEqual(estadistica[0], 5, "Con N numeros - Num. elementos")
        self.assertEqual(estadistica[1], 2, "Con N numeros - Minimo")
        self.assertEqual(estadistica[2], 8, "Con N numeros - Maximo")
        self.assertEqual(estadistica[3], 4.8, "Con N numeros - Promedio")
