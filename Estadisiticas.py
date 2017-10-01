
class Estadisticas:
    def getEstadisticas(self,cadena):
        if cadena == "":
            return [0]
        elif "," in cadena:
            return [2]
        else:
            return [1]
