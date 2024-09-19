

import random

elecciones = ["Piedra","Papel","Tijera"]

enemigo = random.choice(elecciones)

compare_enemigo = enemigo.lower()

jugador = input("Piedra, Papel o Tijera, ya: ")

compare_jugador = jugador.lower()

coindicion1 = compare_jugador == "piedra" and compare_enemigo == "tijera"
coindicion2 = compare_jugador == "papel" and compare_enemigo == "piedra"
coindicion3 = compare_jugador == "tijera" and compare_enemigo == "papel"

if compare_jugador == compare_enemigo:
    print("Ha sido un empate, la computadora eligo:", enemigo)
elif coindicion1 or coindicion2 or coindicion3:
    print("Ha ganado el humano, la computadora eligio:", enemigo)
else:
    print("Gano la computadora, la computadora eligio:", enemigo)
