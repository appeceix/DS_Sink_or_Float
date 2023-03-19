import numpy as np
import random


BOARD_SIZE = 10
'''
Dimensiones del tablero.
'''
MAR = "\u3030"

BARCO ="\u26F5"

DISPARO_AGUA = "\U0001F4A6"

DISPARO_BARCO = "\U0001F4A5"

TABLERO = np.full(fill_value=MAR, shape=(BOARD_SIZE, BOARD_SIZE))
'''
Tablero del jugador.
'''

TABLERO1 = np.full(fill_value=MAR, shape=(BOARD_SIZE, BOARD_SIZE))
'''
Tablero del enemigo.
'''

VISOR = np.full(fill_value=MAR, shape=(BOARD_SIZE, BOARD_SIZE))
'''
Herramienta para que nosotros llevemos registro de
nuestros disparos.
'''

# Variables que nos ayudarán en la colocación de nuestros barcos.
BOAT_1 = 1
BOAT_2 = 2
BOAT_3 = 3
BOAT_4 = 4
VAR_INTERM = 0


BOAT_SIZE1 = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
'''
Herramienta para colocar los barcos del enemigo del tamaño adecuado.
'''

CNT_BOAT= 0

CNT_BOAT1 = 1

VIDAS_JUGADOR = 20

VIDAS_MAQUINA = 20
