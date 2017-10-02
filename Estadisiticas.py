
class Estadisticas:
    def getEstadisticas(self,cadena):
        if cadena == "":
            return [0,None]
        else:
            numeros = cadena.split(",")
            return [len(numeros)]
