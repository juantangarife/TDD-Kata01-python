from unittest import TestCase

from Estadisiticas import Estadisticas

class estadisticasTest(TestCase):
    def test_getEstadisticas_vacia(self):
        estadistica=Estadisticas().getEstadisticas("")
        self.assertEquals(estadistica[0],0,"Cadena vacia")

    def test_getEstadisticas_UnNumero(self):
        estadistica=Estadisticas().getEstadisticas("1")
        self.assertEquals(estadistica[0],1,"Con un numero")

    def test_getEstadisticas_DosNumeros(self):
        estadistica=Estadisticas().getEstadisticas("1,4")
        self.assertEquals(estadistica[0],2,"Con dos numeros")
