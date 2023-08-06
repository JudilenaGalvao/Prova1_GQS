def max_nota(lista_notas):

    if (len(lista_notas) == 0):
        return []

    resultado = []
    max_nota = lista_notas[0][1]

    for elem in lista_notas:

        if (elem[1] == max_nota):
            resultado.append(elem)

        elif (elem[1] > max_nota):
            max_nota = elem[1]
            resultado = []
            resultado.append(elem)

    return resultado