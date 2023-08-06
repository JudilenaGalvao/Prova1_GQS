import sqlite3

def conectar(bd):
    try:
        sqliteConnection = sqlite3.connect(bd)
        cursor = sqliteConnection.cursor()
        print("BD criado e conexao bem sucedida.")

        sqlite_select_Query = "select sqlite_version();"
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        print("Versão do SQLite: ", record)
        cursor.close()
        return sqliteConnection

    except sqlite3.Error as error:
        print("Erro ao se conectar ao SQLite.", error)

def desconectar(conexao):
    if conexao:
        conexao.close()
        print("A conexão foi finalizada.")

def ler_bd(bd, query, params=None):
    print("Ler BD")
    try:
        con = conectar(bd)
        cursor = con.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        resultado = cursor.fetchall()
        cursor.close()
        desconectar(con)
        return resultado
    except sqlite3.Error as error:
        print("Erro selecionando os valores.", error)

def escrever_bd(bd, query, params=None):
    print("Escrever BD")
    try:
        con = conectar(bd)
        cursor = con.cursor()
        cursor.execute(query, params)
        con.commit()
        cursor.close()
        desconectar(con)
        return True
    except sqlite3.Error as error:
        print("Erro inserindo os valores.", error)

# con = conectar("MeuBD.db")
# desconectar(con)
