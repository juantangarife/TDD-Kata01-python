class Estadisticas:
    def getEstadisticas(self, cadena):
        if cadena == "":
            return [0, None, None, None]
        elif "," in cadena:
            numeros = cadena.split(",")
            minimo = int(numeros[0])
            maximo = int(numeros[0])
            for l in numeros:
                num_l = int(l)
                if minimo > num_l:
                    minimo = num_l
                if maximo < num_l:
                    maximo = num_l
            return [len(numeros), minimo, maximo]
        else:
            return [1, int(cadena), int(cadena)]


