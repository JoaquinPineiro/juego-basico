import random
from clases.enemigo import Enemigo
from clases.jugador import Jugador


def main():
    nombre_jugador = input("Bien a la aventura en el espacio. Ingrese nombre: ")
    jugador = Jugador(nombre_jugador)

    enemigos = [
        Enemigo("Alien", 30, 5),
        Enemigo("Robot", 50, 10)
    ]

    enemigos_derrotados = []

    print("Comienza el juego")

    while enemigos:
        enemigo_actual = random.choice(enemigos)
        if enemigo_actual in enemigos_derrotados:
            continue
        print(f"Te encuentras con un {enemigo_actual.nombre} en tu camino")

        while enemigo_actual.salud > 0:
            accion = input("Que desea hacer? (atacar/huir): ").lower()

            if accion == "atacar":
                dan_jugador = jugador.atacar()
                print(f"Has atacado al {enemigo_actual.nombre} y has hecho {dan_jugador} daño")
                enemigo_actual.recibir_dan(dan_jugador)

                if enemigo_actual.salud > 0:
                    dan_enemigo = enemigo_actual.atacar()
                    print(f"{enemigo_actual.nombre} ha atacado y le ha hecho {dan_enemigo} daño")
                    jugador.recibir_dan(dan_enemigo)

            elif accion == "huir":
                print("Has decidido huir del combate")
                break

        if jugador.salud <= 0:
            print("Has perdido la partida")
            break

        if enemigo_actual.salud <= 0:
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)

        jugador.ganar_exp(25)

        continuar = input("Quiere seguir explorando? (s/n): ").lower()

        if continuar != "s":
            print("Gracias por jugar")
            break
    
    if not enemigos:
        print("Felicidades has derrotado a todos los enemigos")

if __name__ == "__main__":
    main()