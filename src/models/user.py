from src.db.database import insert_one, find_one, update_one, delete_one

class User:
    def __init__(self, user: str, guild: str, level: int, xp: int, money: int):
        self.user = user
        self.guild = guild
        self.level = level
        self.xp = xp
        self.money = money

    def save_to_db(self, db_name:str, collection_name: str, data: dict):
        insert_one(db_name, collection_name, data)
        return
    
    def get_from_db(self, db_name:str, collection_name: str, filter: dict):
        find = find_one(db_name, collection_name, filter)
        return find
    
    def update_db(self, db_name:str, collection_name: str, filter: dict, data: dict):
        update = update_one(db_name, collection_name, filter, data)
        return update