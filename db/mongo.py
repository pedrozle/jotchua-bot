import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

connection_str = os.getenv('DATABASE_CONNECTION')
try:
    client = MongoClient(connection_str)
except Exception:
    print("Erro " + Exception)
else:
    print("Conectado ao Mongo")

discord_db = client.discord_db


# ----------------------- Funções para CRUD -----------------------

# ---------------------- Funções para Create ----------------------
def inserir_varios_na_colecao(nome_colecao: str, objs: list):
    colecao = discord_db.get_collection(nome_colecao)
    colecao.insert_many(objs)


def inserir_na_colecao(nome_colecao: str, obj: dict):
    colecao = discord_db.get_collection(nome_colecao)
    colecao.insert_one(obj)


# ---------------------- Funções para Read ------------------------
def buscar_varios_na_colecao(nome_colecao: str):
    colecao = discord_db.get_collection(nome_colecao)
    dados = colecao.find()

    resultado = []

    for dado in dados:
        resultado.append(dado)

    return resultado


def buscar_um_na_colecao(nome_colecao: str, usuario: dict):
    colecao = discord_db.get_collection(nome_colecao)
    usuario = colecao.find_one(usuario)
    return usuario


# ---------------------- Funções para Update ----------------------
def atualizar_um_na_colecao(nome_colecao: str, usuario: dict, novos_dados: dict):
    """Atualiza os dados do objeto de acordo com os novos dados

    usuario = {
        "id": id
    }

    novos_dados = {
        "$set": {"Nome_Campo": "Novo_Valor},
    }

    """
    colecao = discord_db.get_collection(nome_colecao)
    colecao.update_one(usuario, novos_dados)


# ---------------------- Funções para Delete ----------------------
def apagar_um_na_colecao(nome_colecao: str, usuario: dict):
    colecao = discord_db.get_collection(nome_colecao)
    colecao.delete_one(usuario)