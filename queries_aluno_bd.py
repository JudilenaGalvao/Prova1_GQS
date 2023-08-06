from Prova_1.conexaoBD import *


#1- Maior media ja vista em uma turma de codigo TAD203
def ler_aluno_Media_9(bd, codigo):
    query = "SELECT MAX(mt.media) " \
                      "FROM Media_aluno_turma mt, Turma t " \
                      "WHERE mt.id_turma = t.id AND " \
                      "t.codigo LIKE ?"
    return ler_bd(bd, query, ('%'+codigo+'%',))



#2-nomes das turmas e media que o aluno pertence
def ler_aluno_turma(bd, nome):
    query = "SELECT t.nome, mt.media " \
            "FROM Aluno a, Turma t, Media_aluno_turma mt " \
            "WHERE mt.id_turma = t.id AND " \
            "mt.id_aluno = a.id AND " \
            "a.nome LIKE ?"
    return ler_bd(bd, query, ('%'+nome+'%',))


#3-Quantidade de turmas cursada por um aluno
def ler_quant_turma(bd, nome):
    query = "SELECT COUNT(*) " \
            "FROM Aluno a, Turma t, Media_aluno_turma mt " \
            "WHERE mt.id_turma = t.id AND " \
            "mt.id_aluno = a.id AND " \
            "a.nome = ?"
    return ler_bd(bd, query, (nome,))










