class UserModel:

    def __init__(self, username: str, id: str, level: int = 0, xp: int = 0, money: int = 0):
        self.username = username
        self.id = id
        self.level = level
        self.xp = xp
        self.money = money
        self.xp_limit = 100
        
    def add_xp(self, points):
        self.xp += points
        if self.xp >= self.xp_limit:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp_limit =  int(self.xp_limit * 2.5)