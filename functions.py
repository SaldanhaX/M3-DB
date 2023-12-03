import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="gc"
    )

def create_tables():
    with connect() as conn:
        cursor = conn.cursor()
        with open('createDB.sql', 'r') as f:
            cursor.execute(f.read(), multi=True)
        conn.commit()

#Funções para o CRUD em Condominio
def create_cond(cnpj, quant_torres, quant_andares, nome_condominio, tipo, data_entrada):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Condominio (cnpj, quant_torres, quant_andares, nome_condominio, tipo, data_entrada) VALUES (%s, %s, %s, %s, %s, %s)",
                       (cnpj, quant_torres, quant_andares, nome_condominio, tipo, data_entrada))
        conn.commit()

def get_conds():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Condominio")
        return cursor.fetchall()

def update_conds(condominio_id, cond_new_name):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Condominio SET nome_condominio = %s WHERE ID = %s", (cond_new_name, condominio_id))
        conn.commit()

def remove_cond(condominio_id):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Condominio WHERE ID = %s", (condominio_id,))
        conn.commit()

#Funções para o CRUD em Morador
def create_residents(nome_responsavel, cpf_responsavel, data_entrada):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Morador (nome_responsavel, cpf_responsavel, data_entrada) VALUES (%s, %s, %s)",
                       (nome_responsavel, cpf_responsavel, data_entrada))
        conn.commit()

def get_residents():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Morador")
        return cursor.fetchall()

def update_residents(novo_nome_responsavel, novo_cpf_responsavel, morador_id):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Morador
            SET nome_responsavel = %s, cpf_responsavel = %s
            WHERE ID = %s
        """, (novo_nome_responsavel, novo_cpf_responsavel, morador_id))
        conn.commit()

def remove_residents(morador_id):
   with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Morador WHERE ID = %s", (morador_id,))
        conn.commit()


#Funções para o CRUD em Localizacao
def create_location(condominio_id, uf, cidade, bairro, logradouro, numero):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Localizacao (condominio_id, uf, cidade, bairro, logradouro, numero)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (condominio_id, uf, cidade, bairro, logradouro, numero))
        conn.commit()

def get_locations():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Localizacao")
        return cursor.fetchall()

def update_location(localizacao_id, novo_uf, nova_cidade, novo_bairro, novo_logradouro, novo_numero):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Localizacao
            SET uf = %s, cidade = %s, bairro = %s, logradouro = %s, numero = %s
            WHERE ID = %s
        """, (novo_uf, nova_cidade, novo_bairro, novo_logradouro, novo_numero, localizacao_id))
        conn.commit()

def remove_location(localizacao_id):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Localizacao WHERE ID = %s", (localizacao_id,))
        conn.commit()

#Funções para o CRUD morador_condominio
def create_resident_cond(morador_id, condominio_id, apartamento, quant_moradores):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Morador_condominio (morador_id, condominio_id, apartamento, quant_moradores)
            VALUES (%s, %s, %s, %s)
        """, (morador_id, condominio_id, apartamento, quant_moradores))
        conn.commit()

def get_residents_cond():
   with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Morador_condominio")
        return cursor.fetchall()
   
def update_residents_cond(id, novo_apartamento, nova_quant_moradores):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Morador_condominio
            SET apartamento = %s, quant_moradores = %s
            WHERE ID = %s
        """, (novo_apartamento, nova_quant_moradores, id))
        conn.commit()

def remove_residents_cond():
     with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Morador_condominio")
        conn.commit()