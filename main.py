import numpy as pd
import pandas as pd
import random
import sys
import os

sys.path.append(os.getcwd())

import pygame
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("sonidocanon.wav")
soundwater = pygame.mixer.Sound("sonidoagua.wav")
soundwin = pygame.mixer.Sound("sonidowin.wav")
soundlost = pygame.mixer.Sound("sonidolost.mp3")

# IMPORTACIÓN DE VARIABLES CONFIG #

from utils.config import BOARD_SIZE, MAR, BARCO, DISPARO_AGUA, DISPARO_BARCO,\
      TABLERO, TABLERO1, VISOR, VIDAS_JUGADOR, VIDAS_MAQUINA


# IMPORTACIÓN DE FUNCIONES #

from utils.funciones import colocar_barcos_jugador, colocar_barcos_maquina, disparo_jugador, disparo_maquina
      


# DESARROLLO DEL JUEGO #

print("""\n\n¡Bienvenido al juego Hundir la Flota! El objetivo es hundir
los barcos de tu oponente antes de que él hunda los tuyos. Coloca tus
barcos estratégicamente y elige con cuidado dónde disparar. \n\n¡Que gane el mejor capitán! \n\n\n""")

colocar_barcos_jugador()

colocar_barcos_maquina()

while VIDAS_MAQUINA > 0 and VIDAS_JUGADOR > 0:

    while VIDAS_MAQUINA > 0:

        disparo_jugador_x, disparo_jugador_y = disparo_jugador()

        if disparo_jugador_x < 0 or disparo_jugador_x >= BOARD_SIZE or \
           disparo_jugador_y < 0 or disparo_jugador_y >= BOARD_SIZE:
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
            VIDAS_MAQUINA -= 1
            print("¡Le has dado!")
            sound.play()
            print(f"Has disparado en las siguientes posiciones\n{VISOR}") # Para ver en qué posiciones hemos disparado ya.
            #print(tablero1)

        
        
        if TABLERO1[disparo_jugador_x, disparo_jugador_y] == MAR:
            TABLERO1[disparo_jugador_x, disparo_jugador_y] = DISPARO_AGUA
            VISOR[disparo_jugador_x, disparo_jugador_y] = DISPARO_AGUA # Para modificar nuestro mapa del enemigo con agua.
            print("Disparo fallido. Cambio de turno")
            soundwater.play()
            #print(tablero1)
            print(f"Has disparado en las siguientes posiciones\n{VISOR}") # Para ver en qué posiciones hemos disparado ya.
            break
        if VIDAS_MAQUINA == 0:
            print("¡Felicidades, has ganado!")
            soundwin.play()
            break

    while VIDAS_JUGADOR > 0:

        disparo_maquina_x, disparo_maquina_y = disparo_maquina()

        if disparo_maquina_x < 0 or disparo_maquina_x >= BOARD_SIZE or \
           disparo_maquina_y < 0 or disparo_maquina_y >= BOARD_SIZE:
            print("Coordenadas inválidas. Vuelve a intentarlo.")
            continue

        if TABLERO[disparo_maquina_x, disparo_maquina_y] == DISPARO_BARCO or \
           TABLERO[disparo_maquina_x, disparo_maquina_y] == DISPARO_AGUA:
            print("La máquina ya ha disparado en esa casilla. Vuelve a intentarlo.")
            continue

        if TABLERO[disparo_maquina_x, disparo_maquina_y] == BARCO:
            TABLERO[disparo_maquina_x, disparo_maquina_y] = DISPARO_BARCO
            VIDAS_JUGADOR -= 1
            print("¡Le has dado!")
            sound.play()
            print(TABLERO)
        
        
        if TABLERO[disparo_maquina_x, disparo_maquina_y] == MAR:
            TABLERO[disparo_maquina_x, disparo_maquina_y] = DISPARO_AGUA
            print("Disparo fallido. Cambio de turno")
            soundwater()
            print(TABLERO)
            break

        if VIDAS_JUGADOR == 0:
            soundlost.play()
            print("¡Lo siento, ha ganado la maquina! Intentalo de nuevo")
            break
