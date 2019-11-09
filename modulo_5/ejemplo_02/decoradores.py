def puntos_dobles(funcion):
    def envoltorio(puntaje, puntaje_extra):
        puntaje_extra *= 2
        return funcion(puntaje, puntaje_extra)
    return envoltorio


def incrementa_puntos(puntaje, extra):
    return puntaje + extra


def incrementa(puntaje, extra):
    return (puntaje + extra) * 0.1


# Internamente hace esto
nueva_funcion = puntos_dobles(incrementa_puntos)

print(incrementa_puntos(100, 50))
print(incrementa(100, 50))
