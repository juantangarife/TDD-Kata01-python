from unittest import TestCase

from Estadisiticas import Estadisticas

class estadisticasTest(TestCase):
    def test_getEstadisticas(self):
        self.assertEquals(Estadisticas().getEstadisticas(""),0,"Cadena vacia")
