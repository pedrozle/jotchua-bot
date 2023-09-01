import json
import sys
sys.path.insert(1, '/path/to/application/app/folder')
import db.mongo as mongo


class User():
    def __init__(self, dict):

        """ Instancia um novo objeto User com os seguintes atributos:

        self.id
        self.name
        {
            self.apelido
            self.balance
            self.bank
            self.lvl
            self.xp
        }
        """

        for key in dict:
            setattr(self, key, dict[key])

    def work(self, colecao, value):
        self.balance += value
        mongo.atualizar_um_na_colecao(nome_colecao=colecao, usuario={"id": self.id}, novos_dados={"$set": {"balance": self.balance}})

    def saldo(self):
        string_formatada = (
            f':dollar: : {self.balance}\n'
            f':bank: : {self.bank}'
        )
        return string_formatada

    def add_xp(self, colecao, value):
        neces = (5 * (self.lvl * self.lvl) + (50 * self.lvl) + 100 - self.xp) + self.xp
        if self.lvl == 0:
            neces = 100
        
        self.xp += value
        if self.xp >= neces:
            self.lvl +=1
        mongo.atualizar_um_na_colecao(nome_colecao=colecao, usuario={"id": self.id}, novos_dados={"$set": {"xp": self.xp, "lvl": self.lvl}})




        mongo.atualizar_um_na_colecao(colecao, usuario={"id": self.id}, novos_dados={"$set": {"xp": self.xp}})

    def deposito(self, colecao, value):
        self.balance -= value
        self.bank += value
        mongo.atualizar_um_na_colecao(nome_colecao=colecao, usuario={"id": self.id}, novos_dados={"$set": {"balance": self.balance, "bank": self.bank}})

    def saque(self, colecao, value):
        self.balance += value
        self.bank -= value
        mongo.atualizar_um_na_colecao(nome_colecao=colecao, usuario={"id": self.id}, novos_dados={"$set": {"balance": self.balance, "bank": self.bank}})

    def getsaldo(self):
        return self.balance

    def getpoup(self):
        return self.bank

    def getId(self):
        return self.id

    def get_xp(self):
        return self.xp

    def get_lvl(self):
        return self.lvl