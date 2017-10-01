from unittest import TestCase

from Estadisiticas import Estadisticas

class estadisticasTest(TestCase):
    def test_getEstadisticas(self):
        estadistica=Estadisticas().getEstadisticas("")
        self.assertEquals(estadistica[0],0,"Cadena vacia")
