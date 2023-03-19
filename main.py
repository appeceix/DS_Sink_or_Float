# IMPORTACIÓN DE LIBRERÍAS #

import numpy as np
import random
import time
import sys
import os
sys.path.append(os.getcwd())
import pygame
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("sonidocanon.wav")
sonidoagua = pygame.mixer.Sound("sonidoagua.wav")
soundwin = pygame.mixer.Sound("sonidowin.wav")
soundlost = pygame.mixer.Sound("sonidolost.mp3")

# IMPORTACIÓN DE VARIABLES CONFIG #

from utils.config import BOARD_SIZE, MAR, BARCO, DISPARO_AGUA, DISPARO_BARCO,\
      TABLERO, TABLERO1, VISOR, VIDAS_JUGADOR, VIDAS_MAQUINA


# IMPORTACIÓN DE FUNCIONES #

from utils.funciones import colocar_barcos_jugador, colocar_barcos_maquina, disparo_jugador, disparo_maquina
      

# DESARROLLO DEL JUEGO #
print(" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print(" ░░░░░░░░░░▄███████▄░░░░░░░░░░")
print(" ░░░░░░░░░▐██▀░░░▀██▌░░░░░░░░░")
print(" ░░░░░░░░░▐██░░░░░██▌░░░░░░░░░")
print(" ░░░░░░░░░▐██▄░░░▄██▌░░░░░░░░░")
print(" ░░░░░░░░░░▀███████▀░░░░░░░░░░")
print(" ░░░░░░░░░░░░▐█▄█▌░░░░░░░░░░░░")
print(" ░░░░░░░░░░▐███▄███▌░░░░░░░░░░")
print(" ░░░░░░░░░░░░▐█▄█▌░░░░░░░░░░░░")
print(" ░░░░░░░░░░░░▐█▄█▌░░░░░░░░░░░░")
print(" ░░░░░░░░░░░░▐█▄█▌░░░░░░░░░░░░")
print(" ░░░░░░░░░░░░▐█▄█▌░░░░░░░░░░░░")
print(" ░░░░░░░░░░░░▐█▄█▌░░░░░░░░░░░░")
print(" ░░░░░░░░░░░░▐█▄█▌░░░░░░░░░░░░")
print(" ░░▄█▄░░░░░░░▐█▄█▌░░░░░░░▄█▄░░")
print(" ▄█████▄░░░░░▐█▄█▌░░░░░▄█████▄")
print(" ░░███░░░░░░░▐█▄█▌░░░░░░░███░░")
print(" ░░███▄░░░░░▄██▄██▄░░░░░▄███░░")
print(" ░░▀████▄▄▄████▄████▄▄▄████▀░░")
print(" ░░░░▀█████████▄█████████▀░░░░")
print(" ░░░░░░▀███████▄███████▀░░░░░░")
print(" ░░░░░░░░░▀████▄████▀░░░░░░░░░")
print(" ░░░░░░░░░░░░▀█▄█▀░░░░░░░░░░░░")


print("╔══════════════════════════════╗")
print("║                              ║")
print("║    ¡Bienvenido a Hundir la   ║")
print("║           Flota!             ║")
print("║                              ║")
print("╚══════════════════════════════╝")


print("""\n\n¡Bienvenido al juego Hundir la Flota! El objetivo es hundir
los barcos de tu oponente antes de que él hunda los tuyos. Coloca tus
barcos estratégicamente y elige con cuidado dónde disparar.\n\n¡Que gane el mejor capitán!\n\n\n\
Empecemos colocando tus barcos.\n\n""")

time.sleep(2) # A lo largo del código hay varios time.sleep para que no sea todo tan instantáneo y mejore la experiencia.

colocar_barcos_jugador() # En este punto del juego el jugador coloca sus barcos.

time.sleep(3)

colocar_barcos_maquina() # Acto seguido la máquina coloca sus posiciones automáticamente

time.sleep(1)




print("\n\n\n¡Ambos tableros han sido colocados! ¡¡¡A los cañones!!!\n\n\n")

print("───────▓▓╬▓")
print("──────▓▓▓║▓▓")
print("─────▓▓▓▓╬▓▓▓▓")
print("░░▄░▓▓▓▓▓║▓▓▓▓▓░░░░░")
print("░▀████████████████▀░░\n\n\n")

while VIDAS_MAQUINA > 0 and VIDAS_JUGADOR > 0: # Este es el mecanismo que hace que avancen los turnos mientras a algún jugador le quede vidas.

    while VIDAS_MAQUINA > 0: # Esta es nuestra secuencia de disparo.

        disparo_jugador_x, disparo_jugador_y = disparo_jugador()

        if disparo_jugador_x < 0 or disparo_jugador_x >= BOARD_SIZE or \
           disparo_jugador_y < 0 or disparo_jugador_y >= BOARD_SIZE: # Para corroborar las coordenadas del disparo.
            print("Coordenadas inválidas. Vuelve a intentarlo.")
            continue

        if disparo_jugador_x not in range(10):
            print("Coordenadas inválidas. Vuelve a intentarlo.")
            continue
        if disparo_jugador_y not in range(10):
            print("Coordenadas inválidas. Vuelve a intentarlo.")
            continue

        if TABLERO1[disparo_jugador_x, disparo_jugador_y] == DISPARO_BARCO or \
           TABLERO1[disparo_jugador_x, disparo_jugador_y] == DISPARO_AGUA:
            print("Ya has disparado en esa casilla. Vuelve a intentarlo.")
            continue

        if TABLERO1[disparo_jugador_x, disparo_jugador_y] == BARCO:
            TABLERO1[disparo_jugador_x, disparo_jugador_y] = DISPARO_BARCO
            VISOR[disparo_jugador_x, disparo_jugador_y] = DISPARO_BARCO # Para modificar nuestro mapa del enemigo con acierto.
            VIDAS_MAQUINA -= 1 # Restamos una vida a la máquina, avanzando en nuestro objetivo.
            print("\n\n¡Proyectil lanzado! ¿Acertará..?")
            time.sleep(2)
            print("\n\n¡Le has dado!")
            sound.play()
            time.sleep(2)
            print(f"\n\nHas disparado en las siguientes posiciones\n{VISOR}") # Para ver en qué posiciones hemos disparado ya.
            time.sleep(2)
            #print(tablero1) # Si queremos comprobar el tablero del enemigo podemos hacer este print.

        if TABLERO1[disparo_jugador_x, disparo_jugador_y] == MAR:
            TABLERO1[disparo_jugador_x, disparo_jugador_y] = DISPARO_AGUA
            VISOR[disparo_jugador_x, disparo_jugador_y] = DISPARO_AGUA # Para modificar nuestro visor del mapa del enemigo con agua.
            print("\n\n¡Proyectil lanzado! ¿Acertará..?")
            time.sleep(2)
            print("\n\nDisparo fallido. Cambio de turno")
            sonidoagua.play()
            time.sleep(2)
            #print(tablero1)
            print(f"\n\nHas disparado en las siguientes posiciones\n{VISOR}")
            break

        if VIDAS_MAQUINA == 0: # El objetivo del juego es llegar hasta este punto.
            time.sleep(3)
            print("\n\n\n¡Felicidades, has ganado!")
            print("\n\n\nEsperamos que hayas disfrutado.\n\nIsmael Merino\nMatheus Zottis\n José Prado")
            soundwin.play()
            break


    while VIDAS_JUGADOR > 0 and VIDAS_MAQUINA>0: # Esta sería la secuencia de disparo de la máquina.

        disparo_maquina_x, disparo_maquina_y = disparo_maquina()

        if disparo_maquina_x < 0 or disparo_maquina_x >= BOARD_SIZE or \
           disparo_maquina_y < 0 or disparo_maquina_y >= BOARD_SIZE:
            print("Coordenadas inválidas. Vuelve a intentarlo.")
            continue

        if TABLERO[disparo_maquina_x, disparo_maquina_y] == DISPARO_BARCO or \
           TABLERO[disparo_maquina_x, disparo_maquina_y] == DISPARO_AGUA:
            print("El enemigo está considerando su disparo...")
            continue

        if TABLERO[disparo_maquina_x, disparo_maquina_y] == BARCO: # Caso de acierto por parte de la máquina.
            TABLERO[disparo_maquina_x, disparo_maquina_y] = DISPARO_BARCO
            VIDAS_JUGADOR -= 1 # Cuando la máquina nos da a nosotros se nos resta una vida.
            print("\n\n¡Ouch! ¡El enemigo te ha dado!")
            sound.play()
            print(TABLERO)
        
        
        if TABLERO[disparo_maquina_x, disparo_maquina_y] == MAR: # Caso de fallo por parte de la máquina.
            TABLERO[disparo_maquina_x, disparo_maquina_y] = DISPARO_AGUA
            print("\n\nEl enemigo ha fallado su disparo. Ahora es tu turno.")
            sonidoagua.play()
            print(TABLERO)
            break

        if VIDAS_JUGADOR == 0: # Condición para que la máquina gane.
            time.sleep(3)
            soundlost.play()
            print("\n\n\n¡Lo siento, ha ganado la maquina! Intentalo de nuevo")
            print("\n\n\nEsperamos que hayas disfrutado.\n\nIsmael Merino\nMatheus Zottis\nJosé Prado")
            break
