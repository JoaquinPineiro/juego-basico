import random


class Enemigo:
    def __init__(self, nombre, salud, ataque):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque

    def atacar(self):
        return random.randint(5, 15)
    
    def recibir_dan(self, dan):
        self.salud -= dan
        if self.salud <= 0:
            print(f"Has derrotado a {self.nombre}")
            return True
        return False
