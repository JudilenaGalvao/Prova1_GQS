def percentual_notas(lista):
        professores = []
        medias = []
        for mediaTurma in lista:
            if mediaTurma[1] not in professores:
                professores.append(mediaTurma[1])
                medias.append([0,0])

        for mediaTurma in lista:
            indice = professores.index(mediaTurma[1])
            if (mediaTurma[2] > 7):
                medias[indice][0] += 1
            medias[indice][1] += 1

        resultado = []
        for indice, professor in enumerate(professores):
            percentual = medias[indice][0]/medias[indice][1]
            resultado.append((professor, round(percentual*100, 2)))

        return resultado