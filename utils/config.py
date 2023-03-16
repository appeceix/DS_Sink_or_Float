import numpy as np
import pandas as pd
import random


BOARD_SIZE = 10
MAR = "\u3030"
BARCO ="\u26F5"
DISPARO_AGUA = "\U0001F4A6"
DISPARO_BARCO = "\U0001F4A5"
TABLERO = np.full(fill_value=MAR, shape=(BOARD_SIZE, BOARD_SIZE))
TABLERO1 = np.full(fill_value=MAR, shape=(BOARD_SIZE, BOARD_SIZE))
VISOR = np.full(fill_value=MAR, shape=(BOARD_SIZE, BOARD_SIZE))
BOAT_SIZE = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
BOAT_SIZE1 = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
CNT_BOAT= 0
CNT_BOAT1 = 0
VIDAS_JUGADOR = 20
VIDAS_MAQUINA = 20