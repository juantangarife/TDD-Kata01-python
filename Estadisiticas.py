
class Estadisticas:
    def getEstadisticas(self,cadena):
        if cadena == "":
            return [0,None]
        elif "," in cadena:
            numeros = cadena.split(",")
            minimo = int(numeros[0])
            for l in numeros:
                if minimo > int(l):
                    minimo = int(l)
            return [len(numeros), minimo]
        else:
            return [1,int(cadena)]


