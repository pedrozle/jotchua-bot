from pymongo import MongoClient
from config import get_settings
from pymongo import MongoClient
from pymongo.errors import AutoReconnect
from config import get_settings

DB_USER = get_settings().DB_USER
DB_PASS = get_settings().DB_PASS
DB_SERVER = get_settings().DB_SERVER

class DB:
    def __init__(self):
        self.client = self._connect()
        
    def _connect(self):
        print("conectando...")
        uri = f"mongodb+srv://{DB_USER}:{DB_PASS}@{DB_SERVER}"
        try:
            self.client = MongoClient(uri)
            print("Conexão estabelecida com sucesso!")
        except AutoReconnect as e:
            print(f"Erro ao conectar: {e}")
        return self.client
        
    def get_collection(self, collection_name: str):
        return self.client["jotchua_bot"][collection_name]

db_instance = DB()