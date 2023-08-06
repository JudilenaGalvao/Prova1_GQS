from unittest import TestCase

import sys
sys.path.insert(0, '..')
from Lista_1.conexaoBD import *

BD = "TestBD.db"

class MockBD(TestCase):
    @classmethod
    def setUpClass(cls):
        con = conectar(BD)
        cursor = con.cursor()



        query_create_turma = """CREATE TABLE Turma (
                             id int NOT NULL PRIMARY KEY ,
                             nome text NOT NULL,
                             codigo text NOT NULL
                            )"""

        query_create_aluno = """CREATE TABLE Aluno (
                                          id int NOT NULL PRIMARY KEY ,
                                          nome text NOT NULL
                                        )"""

        query_create_media_aluno_turma  = """CREATE TABLE Media_aluno_turma (
                                          id int NOT NULL PRIMARY KEY ,
                                          id_turma int NOT NULL,
                                          id_aluno int NOT NULL,
                                          nota1 float NOT NULL,
                                          nota2 float NOT NULL,
                                          nota3 float NOT NULL,
                                          media float NOT NULL,
                                          FOREIGN KEY (id_turma) REFERENCES Turma(id),
                                          FOREIGN KEY (id_aluno) REFERENCES Aluno(id)
                                        )"""

        try:
            cursor.execute(query_create_turma)
            cursor.execute(query_create_aluno)
            cursor.execute(query_create_media_aluno_turma)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")


        query_insert_turma = """INSERT INTO Turma (id, nome, codigo) VALUES
                                    (1, 'POO', 'TAD0202'),
                                    (2, 'Circuitos_Digitais','TAD0202'),
                                    (3, 'Banco_de_Dados', 'TAD0203'),
                                    (4, 'Anatomia_Dental', 'TAD0201')"""

        query_insert_aluno = """INSERT INTO Aluno (id, nome) VALUES
                                            (1, 'Maria'),
                                            (2, 'Lucas'),
                                            (3, 'Pedro'),
                                            (4, 'Rebeca'),
                                            (5, 'Carla'),
                                            (6, 'Vinicius')"""

        query_insert_media_aluno_turma = """INSERT INTO Media_aluno_turma (id, id_turma, id_aluno, nota1, nota2, nota3, media) VALUES
                                                    (1, 3, 1, 8.7, 7.0, 9.0, 8.3),
                                                    (2, 3, 5, 10.0, 9.5, 10.0, 9.8),
                                                    (3, 3, 3, 7.0, 7.0, 7.0, 7.0),
                                                    (4, 3, 4, 5.1, 8.0, 5.0, 6.0),
                                                    (5, 3, 6, 4.0, 10.0, 10.0, 8.0),
                                                    (6, 1, 5, 7.7, 7.0, 8.4, 7.7),
                                                    (7, 1, 3, 9.7, 9.0, 9.4, 9.5),
                                                    (8, 2, 5, 3.0, 3.5, 10.0, 5.5),
                                                    (9, 2, 1, 10.0, 10.0, 10.0, 10.0),
                                                    (10, 2, 4, 6.9, 9.0, 9.0, 9.2)"""



        try:
            cursor.execute(query_insert_turma)
            cursor.execute(query_insert_aluno)
            cursor.execute(query_insert_media_aluno_turma)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na inserção de dados:", error)
        else:
            print("Inserção dos dados: OK")

        cursor.close()

        desconectar(con)

        testconfig ={
            'bd': BD
        }
        cls.mock_db_config = testconfig

    @classmethod
    def tearDownClass(cls):
        print("TearDown")
        con = conectar(BD)
        cursor = con.cursor()

        try:
            cursor.execute("DROP TABLE Turma")
            cursor.execute("DROP TABLE Aluno")
            cursor.execute("DROP TABLE Media_aluno_turma")
            con.commit()
            cursor.close()
            print("Removeu os dados das tabelas.")
        except sqlite3.Error as error:
            print("Banco de dados não existe. Erro na remoção do BD.", error)
        finally:
            desconectar(con)



