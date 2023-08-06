def media_turma_professor(lista):
    professores = []
    medias = []
    for mediaTurma in lista:
        if mediaTurma[1] not in professores:
            professores.append(mediaTurma[1])
            medias.append([0,0])

    for mediaTurma in lista:
        indice = professores.index(mediaTurma[1])
        medias[indice][0] += mediaTurma[2]
        medias[indice][1] += 1

    resultado = []
    for indice, professor in enumerate(professores):
        media = medias[indice][0]/medias[indice][1]
        resultado.append((professor, round(media, 2)))

    return resultado

