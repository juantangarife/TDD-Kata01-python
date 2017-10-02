class Estadisticas:
    def getEstadisticas(self, cadena):
        if cadena == "":
            return [0, None, None, None]
        else:
            numeros = cadena.split(",")
            primero = int(numeros[0])
            num_elementos = len(numeros)
            minimo = primero
            maximo = primero
            total = 0
            for l in numeros:
                num_l = int(l)
                if minimo > num_l:
                    minimo = num_l
                if maximo < num_l:
                    maximo = num_l
                total += num_l
            return [num_elementos, minimo, maximo, total/float(num_elementos)]


