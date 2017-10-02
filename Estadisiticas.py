
class Estadisticas:
    def getEstadisticas(self,cadena):
        if cadena == "":
            return [0,None]
        elif "," in cadena:
            numeros = cadena.split(",")
            if int(numeros[0]) < int(numeros[1]):
                minimo = int(numeros[0])
            else:
                minimo = int(numeros[1])
            return [len(numeros), minimo]
        else:
            return [1,int(cadena)]


