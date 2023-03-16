import numpy as np
import pandas as pd
import random

######CONFIGS#####

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


##############################################1#################################
def colocar_barcos_jugador():
    from utils.config import CNT_BOAT, BOAT_SIZE

    CNT_BOAT
    while CNT_BOAT < 10:

        for i in BOAT_SIZE: 

            orient_valida = False
            while not orient_valida:
                orient = input("Dame la orientacion del barco:  N, S, E o W: ")
                if orient not in ["N", "S", "E", "W"]:
                    print("Orientación no válida, tiene que ser N, S, E o W")
                else:
                    orient_valida = True
            
            while True:
                try:
                    colocar_x = int(input("Dame la coordenada X: "))
                    if colocar_x < 0 or colocar_x >9:
                        print("Coordenada X no válida. Recuerda que debe ser entre 0 y 9. Inténtalo de nuevo:")
                        continue
                    break
                except ValueError:
                    print("Coordenada X no válida. Recuerda que debe ser entre 0 y 9. Inténtalo de nuevo:")

            while True:
                try:
                    colocar_y = int(input("Dame la coordenada Y: "))
                    if colocar_y <0 or colocar_y > 9:
                        print("Coordenada Y no válida. Recuerda que debe ser entre 0 y 9. Inténtalo de nuevo:")
                        continue
                    break
                except ValueError:
                    print("Coordenada Y no válida. Recuerda que debe ser entre 0 y 9. Inténtalo de nuevo:")

            if orient == "N":
                if ((colocar_x-i+1) >= 0)&\
                    (TABLERO[(colocar_x-i+1):(colocar_x+1), colocar_y] != BARCO).all():
                    TABLERO[(colocar_x-i+1):(colocar_x+1), colocar_y] = BARCO
                    CNT_BOAT += 1
                    print(CNT_BOAT)
                elif ((colocar_x-i+1) < 0):
                    print("Te estás saliendo por arriba")
                else:
                    print("Ya hay un barco ahí")
                print(TABLERO)            
                
            
            if orient == "S":
                if ((colocar_x+i) <= BOARD_SIZE)&\
                    (TABLERO[colocar_x:(colocar_x+i), colocar_y] != BARCO).all():
                    TABLERO[colocar_x:(colocar_x+i), colocar_y] = BARCO
                    CNT_BOAT += 1
                    print(CNT_BOAT)
                elif ((colocar_x+i) > BOARD_SIZE):
                    print("Te estás saliendo por abajo")
                else:
                    print("Ya hay un barco ahí")
                print(TABLERO)            
                    
            
            if orient == "E":
                if ((colocar_y+i) <= BOARD_SIZE)&\
                    (TABLERO[colocar_x, colocar_y:(colocar_y+i)] != BARCO).all():
                    TABLERO[colocar_x, colocar_y:(colocar_y+i)] = BARCO
                    CNT_BOAT += 1
                    print(CNT_BOAT)
                elif ((colocar_y+i) > BOARD_SIZE):
                    print("Te estás saliendo por la derecha")
                else:
                    print("Ya hay un barco ahí")
                print(TABLERO)            
                
            
            if orient == "W":
                if ((colocar_y-i+1) >= 0)&\
                    (TABLERO[colocar_x, (colocar_y-i+1):(colocar_y+1)] != BARCO).all():
                    TABLERO[colocar_x, (colocar_y-i+1):(colocar_y+1)] = BARCO
                    CNT_BOAT += 1
                    print(CNT_BOAT)
                elif ((colocar_y-i+1) < 0):
                    print("Te estás saliendo por la izquierda")
                else:
                    print("Ya hay un barco ahí")
                print(TABLERO)            
                
            if CNT_BOAT == 10:
                print("\nTablero 1 con barcos colocados:")
                print(TABLERO)
                break
            
 ##############################################2#################################       



def colocar_barcos_maquina():
    from utils.config import CNT_BOAT1, BOAT_SIZE1

    while CNT_BOAT1 < 10:

        letras_orient = ["N", "S", "E", "W"] # Lista para seleccionar orientación válida
        
        for i in BOAT_SIZE1:
            
            colocado = False
            
            while not colocado:
                
                orient = random.choice(letras_orient) # Elige una orientación aleatoria
                colocar_x = random.randint(0, 9)  # Da coordenada aleatoria
                colocar_y = random.randint(0, 9)

                if orient == "N":

                    if ((colocar_x-i+1) >= 0)&\
                        (TABLERO1[(colocar_x-i+1):(colocar_x+1), colocar_y] != BARCO).all():
                        TABLERO1[(colocar_x-i+1):(colocar_x+1), colocar_y] = BARCO
                        colocado = True
                        print(CNT_BOAT1)
                        print(TABLERO1) 

                    elif ((colocar_x-i+1) < 0):
                        print("Te estás saliendo por arriba")


                    else:
                        print("Ya hay un barco ahí")


                if orient == "S":

                    if ((colocar_x+i) <= BOARD_SIZE)&\
                        (TABLERO1[colocar_x:(colocar_x+i), colocar_y] != BARCO).all():
                        TABLERO1[colocar_x:(colocar_x+i), colocar_y] = BARCO
                        colocado = True
                        print(CNT_BOAT1)
                        print(TABLERO1) 

                    elif ((colocar_x+i) > BOARD_SIZE):
                        print("Te estás saliendo por abajo")


                    else:
                        print("Ya hay un barco ahí")


                if orient == "E":

                    if ((colocar_y+i) <= BOARD_SIZE)&\
                        (TABLERO1[colocar_x, colocar_y:(colocar_y+i)] != BARCO).all():
                        TABLERO1[colocar_x, colocar_y:(colocar_y+i)] = BARCO
                        colocado = True
                        print(CNT_BOAT1)
                        print(TABLERO1) 

                    elif ((colocar_y+i) > BOARD_SIZE):
                        print("Te estás saliendo por la derecha")


                    else:
                        print("Ya hay un barco ahí")



                if orient == "W":

                    if ((colocar_y-i+1) >= 0)&\
                        (TABLERO1[colocar_x, (colocar_y-i+1):(colocar_y+1)] != BARCO).all():
                        TABLERO1[colocar_x, (colocar_y-i+1):(colocar_y+1)] = BARCO
                        colocado = True
                        print(CNT_BOAT1)
                        print(TABLERO1) 

                    elif ((colocar_y-i+1) < 0):
                        print("Te estás saliendo por la izquierda")


                    else:
                        print("Ya hay un barco ahí")

            CNT_BOAT1 += 1
            if CNT_BOAT1 == 10:
                print("\nTablero de la máquina con barcos colocados:")
                print(TABLERO1)
                break        

############################################3##############################

def disparo_jugador():
    while True:
        while True:
            try:
                disparo_jugador_x = int(input("Ingrese la coordenada x (0-9): "))
                if disparo_jugador_x < 0 or disparo_jugador_x > 9:
                    print("Coordenada x fuera de rango. Intente de nuevo.")
                    continue
                break
            except ValueError:
                print("Coordenada x inválida. Intente de nuevo.")

        while True:
            try:
                disparo_jugador_y = int(input("Ingrese la coordenada y (0-9): "))
                if disparo_jugador_y < 0 or disparo_jugador_y > 9:
                    print("Coordenada y fuera de rango. Intente de nuevo.")
                    continue
                break
            except ValueError:
                print("Coordenada y inválida. Intente de nuevo.")
                
        return disparo_jugador_x, disparo_jugador_y

############################################4##############################

def disparo_maquina():
        disparo_maquina_x = random.randint(0, 9)
        disparo_maquina_y = random.randint(0, 9)
        return (disparo_maquina_x, disparo_maquina_y)
    