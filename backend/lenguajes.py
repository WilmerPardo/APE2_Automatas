"""
lenguajes.py
------------
Algoritmos de operaciones sobre lenguajes formales.
Metodología de la práctica de Autómatas.
"""


def generar_cadenas(alfabeto: list[str], max_len: int):
    """
    Generar todas las cadenas sobre Σ hasta longitud n.
    """
    resultado = [""]   # cadena vacía (épsilon)
    nuevas    = [""]

    for _ in range(max_len):
        temp = []
        for cadena in nuevas:           # recorre las cadenas del nivel anterior
            for simbolo in alfabeto:    # agrega cada símbolo del alfabeto al final
                temp.append(cadena + simbolo)
        #temp = [cadena + simbolo for cadena in nuevas for simbolo in alfabeto] # forma compacta
        resultado.extend(temp)
        nuevas = temp

    # Eliminar duplicados manteniendo el orden
    final = []
    for elemento in resultado:
        if elemento not in final:
            final.append(elemento)
    return final


def pertenece(cadena: str, lenguaje: list[str]):
    for elemento in lenguaje:
        if elemento == cadena:
            return True
    return False


def union(L1: list[str], L2: list[str]):
    #unir L1 y L2 sin repetir elementos
    resultado = L1.copy()
    for elemento in L2:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado


def concatenacion(L1: list[str], L2: list[str]):
    #combinaciones entre L1 y l2
    resultado = []
    for x in L1:
        for y in L2:
            resultado.append(x + y)

    #eliminar duplicados
    final = []
    for elemento in resultado:
        if elemento not in final:
            final.append(elemento)
    return final


def kleene_star(L: list[str], max_iter: int):
    #Construir L* (cero o más repeticiones)
    resultado = [""]
    actual    = [""]

    for i in range(1, max_iter + 1): 
        nuevo = []                   
        for x in actual:                 
            for y in L:                  
                cadena = x + y           
                nuevo.append(cadena)     

        for elemento in nuevo:           
            if elemento not in resultado:    # SI elemento NO ESTÁ en resultado
                resultado.append(elemento)   # AGREGAR elemento A resultado

        actual = nuevo                   # actual ← nuevo

    return resultado


def kleene_plus(L: list[str], max_iter: int):
    #L+ sin ε
    ks = kleene_star(L, max_iter)
    resultado = []
    for elemento in ks:
        if elemento != "":
            resultado.append(elemento)
    return resultado


def analizar_crecimiento(L: list[str]):
    #contar numero de cadenas generadas
    crecimiento = []
    for i in range(1, 6):
        resultado = kleene_star(L, i)
        print(resultado)
        crecimiento.append({
            "iteracion": i,
            "cantidad": len(resultado)
        })

    return crecimiento
