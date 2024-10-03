import random


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salud = 100
        self.nivel = 1
        self.experiencia = 0

    def atacar(self):
        return random.randint(10, 20) * self.nivel
    
    def recibir_dan(self, dan):
        self.salud -= dan
        if (self.salud) <= 0:
            print(f"{self.nombre} ha muerto")

    def ganar_exp(self, exp):
        self.experiencia += exp
        if self.experiencia >= 100:
            self.nivel += 1
            self.experiencia = 0
            print(f"{self.nombre} ha subido de nivel ahora es nivel {self.nivel}")