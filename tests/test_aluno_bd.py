from MockDB import MockBD

import sys
sys.path.insert(0, '..')

from Prova_1.queries_aluno_bd import *


class TestAlunoDB(MockBD):

    def test_aluno_Media(self):
        codigo = "TAD0203"
        retorno_1 = [(9.8,)]
        self.assertEqual(ler_aluno_Media_9(self.mock_db_config.get('bd'), codigo), retorno_1)

        #Turma que não tem nenhum aluno cadastrado
        codigo = "TAD0201"
        retorno_2 = [(None,)]
        self.assertEqual(ler_aluno_Media_9(self.mock_db_config.get('bd'), codigo), retorno_2)

        #Turma que não existe
        codigo = "TAD0200"
        retorno_2 = [(None,)]
        self.assertEqual(ler_aluno_Media_9(self.mock_db_config.get('bd'), codigo), retorno_2)



    def test_aluno_turma(self):
        codigo = "Carla"
        retorno_1 = [('Banco_de_Dados', 9.8,), ('POO', 7.7,), ('Circuitos_Digitais', 5.5)]
        self.assertEqual(ler_aluno_turma(self.mock_db_config.get('bd'), codigo), retorno_1)

        # aluno que não esta cadastra em nenhuma turma
        codigo = "Lucas"
        retorno_2 = []
        self.assertEqual(ler_aluno_turma(self.mock_db_config.get('bd'), codigo), retorno_2)

        # aluno que não esta cadastrado
        codigo = "Bruno"
        retorno_3 = []
        self.assertEqual(ler_aluno_turma(self.mock_db_config.get('bd'), codigo), retorno_3)



    def test_quant_turma(self):
        nome = "Carla"
        retorno_1 = [(3,)]
        self.assertEqual(ler_quant_turma(self.mock_db_config.get('bd'), nome), retorno_1)

        #Aluno não esta em nenhuma turma
        nome = "Lucas"
        retorno_2 = [(0,)]
        self.assertEqual(ler_quant_turma(self.mock_db_config.get('bd'), nome), retorno_2)

        #Aluno não esta matriculado
        nome = "Felipe"
        retorno_3 = [(0,)]
        self.assertEqual(ler_quant_turma(self.mock_db_config.get('bd'), nome), retorno_3)

