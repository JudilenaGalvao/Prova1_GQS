from Prova_1.alunoMaiorNota import *
from Prova_1.media_Professor import *
from Prova_1.percentual_nota import *
import unittest


class TestAlunoMaior(unittest.TestCase):

    def test_aluno_Maior_Nota(self):

        situacao1 = [('Carla', 9.7), ('Danilo', 6.7), ('Daniel', 3.4), ('Alice', 9.7), ('Flavio', 5.7), ('Silvia', 4.4)]
        self.assertEqual(max_nota(situacao1), [('Carla', 9.7), ('Alice', 9.7)])

        situacao2 = [('Carla', 9.0), ('Danilo', 6.7), ('Daniel', 3.4), ('Alice', 9.7), ('Flavio', 5.7), ('Silvia', 4.4)]
        self.assertEqual(max_nota(situacao2), [('Alice', 9.7)])

        situacao3 = []
        self.assertEqual(max_nota(situacao3), [])



    def test_media(self):

        situacao1 = [('TAD0055', 1, 9.7), ('TAD0010', 2, 6.7), ('TAD0105', 3, 3.4), ('TAD0105', 1, 4.4), ('TAD0105', 2, 7.1), ('TAD0027', 2, 9.7), ('TAD0202', 3, 5.7), ('TAD0001', 3, 4.4)]

        r_esperado1 = [(1, 7.05), (2, 7.83), (3, 4.5)]
        self.assertEqual(media_turma_professor(situacao1), r_esperado1)


        situacao2 = []

        r_esperado2 = []
        self.assertEqual(media_turma_professor(situacao2), r_esperado2)



    def test_percentual(self):
        situacao1 = [('TAD0055', 1, 9.7), ('TAD0010', 2, 6.7), ('TAD0105', 3, 3.4), ('TAD0105', 1, 4.4), ('TAD0105', 2, 7.1), ('TAD0027', 2, 9.7), ('TAD0202', 3, 5.7), ('TAD0001', 3, 4.4)]

        r_esperado1 = [(1, 50), (2, 66.67), (3, 0)]
        self.assertEqual(percentual_notas(situacao1), r_esperado1)


        situacao2 = []

        r_esperado2 = []
        self.assertEqual(percentual_notas(situacao2), r_esperado2)
