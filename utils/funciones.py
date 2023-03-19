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
      TABLERO, TABLERO1, VISOR, VIDAS_JUGADOR, VIDAS_MAQUINA, BOAT_1, BOAT_2, BOAT_3, BOAT_4


# FUNCIONES #

def colocar_barcos_jugador():
    '''
    Para colocar nuestros barcos en el tablero a través de tres inputs: 
    orientación, coordenada X y coordenada Y.
    '''
    from utils.config import CNT_BOAT


    while CNT_BOAT < 10: # Para establecer el límite de barcos a colocar.

        orient_valida = False # De esta manera nos aseguramos de que el input de orientación sea válido.
        while not orient_valida:
            orient = input("Dame la orientacion del barco (N, S, E o W): ")
            if orient not in ["N", "S", "E", "W"]:
                print("Orientación no válida, tiene que ser N, S, E o W")
            else:
                orient_valida = True
        
        while True: # Comprobación de la validez de las coordenadas X e Y
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

        if CNT_BOAT <= 3:
            VAR_INTERM = BOAT_1
        elif CNT_BOAT <=6 :
            VAR_INTERM = BOAT_2
        elif CNT_BOAT <= 8:
            VAR_INTERM = BOAT_3
        else:
            VAR_INTERM = BOAT_4

        
        if orient == "N":

            
            if ((colocar_x-VAR_INTERM+1) >= 0)&\
                (TABLERO[(colocar_x-VAR_INTERM+1):(colocar_x+1), colocar_y] != BARCO).all(): #Requisito para colocar un barco.

                TABLERO[(colocar_x-VAR_INTERM+1):(colocar_x+1), colocar_y] = BARCO
                print(f"Barco número {CNT_BOAT+1} colocado:")
                CNT_BOAT += 1 # En caso True aumentamos el contador de barcos para cambiar el tamaño de los barcos.
                
            elif ((colocar_x-VAR_INTERM+1) < 0): # Advertencia
                print("Te estás saliendo por arriba")
                
            else: # Advertencia
                print("¡Estás pisando otro barco!")

            time.sleep(1)
            print(TABLERO)

                            
            
        
        if orient == "S":

            if ((colocar_x+VAR_INTERM) <= BOARD_SIZE)&\
                (TABLERO[colocar_x:(colocar_x+VAR_INTERM), colocar_y] != BARCO).all():

                TABLERO[colocar_x:(colocar_x+VAR_INTERM), colocar_y] = BARCO
                print(f"Barco número {CNT_BOAT+1} colocado:")
                CNT_BOAT += 1 

            elif ((colocar_x+VAR_INTERM) > BOARD_SIZE):
                print("Te estás saliendo por abajo")
                
            else:
                print("¡Estás pisando otro barco!")
                
            time.sleep(1)
            print(TABLERO)   

        
                
        
        if orient == "E":
            
            if ((colocar_y+VAR_INTERM) <= BOARD_SIZE)&\
                (TABLERO[colocar_x, colocar_y:(colocar_y+VAR_INTERM)] != BARCO).all():

                TABLERO[colocar_x, colocar_y:(colocar_y+VAR_INTERM)] = BARCO
                print(f"Barco número {CNT_BOAT+1} colocado:")
                CNT_BOAT += 1

            elif ((colocar_y+VAR_INTERM) > BOARD_SIZE):
                print("Te estás saliendo por la derecha")
                
            else:
                print("¡Estás pisando otro barco!")
                
            time.sleep(1)
            print(TABLERO)
            

        
        if orient == "W":

            if ((colocar_y-VAR_INTERM+1) >= 0)&\
                (TABLERO[colocar_x, (colocar_y-VAR_INTERM+1):(colocar_y+1)] != BARCO).all():

                TABLERO[colocar_x, (colocar_y-VAR_INTERM+1):(colocar_y+1)] = BARCO
                print(f"Barco número {CNT_BOAT+1} colocado:")
                CNT_BOAT += 1

            elif ((colocar_y-VAR_INTERM+1) < 0):
                print("Te estás saliendo por la izquierda")
                
            else:
                print("¡Estás pisando otro barco!")
                
            time.sleep(1)
            print(TABLERO)     
    
            
        if CNT_BOAT == 10: # Cuando llegamos a 10 se acaba el bucle se termina esta función.
            print("\n Perfecto, ya has colocado todos tus barcos:")
            time.sleep(1)
            print(TABLERO)
            break
                 



def colocar_barcos_maquina():
    '''
    Función que al llamarla colocará automáticamente los barcos\
    de la máquina en su tablero. En principio nosotros no podemos verlo salvo que\
    descomentemos el print oportuno.
    '''
    from utils.config import CNT_BOAT1, BOAT_SIZE1 

    while CNT_BOAT1 < 11:

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
                        time.sleep(1)
                        print(f"El enemigo ha colocado el barco número {CNT_BOAT1}.\n\n\n")
                        # print(TABLERO1) 

                    elif ((colocar_x-i+1) < 0): # Supuestos de colocación incorrecta por parte de la máquina.
                        # print("Te estás saliendo por arriba")
                        pass

                    else:
                        # print("Ya hay un barco ahí")
                        pass

                if orient == "S":

                    if ((colocar_x+i) <= BOARD_SIZE)&\
                        (TABLERO1[colocar_x:(colocar_x+i), colocar_y] != BARCO).all():
                        TABLERO1[colocar_x:(colocar_x+i), colocar_y] = BARCO
                        colocado = True
                        time.sleep(1)
                        print(f"El enemigo ha colocado el barco número {CNT_BOAT1}.\n\n\n")
                        # print(TABLERO1) 

                    elif ((colocar_x+i) > BOARD_SIZE):
                        # print("Te estás saliendo por abajo")
                        pass

                    else:
                        # print("Ya hay un barco ahí")
                        pass

                if orient == "E":

                    if ((colocar_y+i) <= BOARD_SIZE)&\
                        (TABLERO1[colocar_x, colocar_y:(colocar_y+i)] != BARCO).all():
                        TABLERO1[colocar_x, colocar_y:(colocar_y+i)] = BARCO
                        colocado = True
                        time.sleep(1)
                        print(f"El enemigo ha colocado el barco número {CNT_BOAT1}.\n\n\n")
                        # print(TABLERO1) 

                    elif ((colocar_y+i) > BOARD_SIZE):
                        # print("Te estás saliendo por la derecha")
                        pass

                    else:
                        # print("Ya hay un barco ahí")
                        pass


                if orient == "W":

                    if ((colocar_y-i+1) >= 0)&\
                        (TABLERO1[colocar_x, (colocar_y-i+1):(colocar_y+1)] != BARCO).all():
                        TABLERO1[colocar_x, (colocar_y-i+1):(colocar_y+1)] = BARCO
                        colocado = True
                        time.sleep(1)
                        print(f"El enemigo ha colocado el barco número {CNT_BOAT1}.\n\n\n")
                        # print(TABLERO1) 

                    elif ((colocar_y-i+1) < 0):
                        # print("Te estás saliendo por la izquierda")
                        pass

                    else:
                        # print("Ya hay un barco ahí")
                        pass
            CNT_BOAT1 += 1
            if CNT_BOAT1 == 11:
                time.sleep(1)
                print("\n\nEl enemigo ya ha colocado todos sus barcos\n\n")
                # print(TABLERO1)
                break         # Aquí termina la colocación de barcos de la máquina.




def disparo_jugador():
    '''
    Disparar en las coordenadas introducidas mediante input.
    '''
    while True:
        while True:
            try:
                disparo_jugador_x = int(input("Ingrese la coordenada X (0-9): "))
                if disparo_jugador_x < 0 or disparo_jugador_x > 9:
                    print("Coordenada X fuera de rango. Inténtalo de nuevo.")
                    continue
                break
            except ValueError:
                print("Coordenada X inválida. Inténtalo de nuevo.")

        while True:
            try:
                disparo_jugador_y = int(input("Ingrese la coordenada Y (0-9): "))
                if disparo_jugador_y < 0 or disparo_jugador_y > 9:
                    print("Coordenada Y fuera de rango. Inténtalo de nuevo.")
                    continue
                break
            except ValueError:
                print("Coordenada Y inválida. Inténtalo de nuevo.")
                
        return disparo_jugador_x, disparo_jugador_y



def disparo_maquina():
    '''
    Función que hará que la máquina dispare automáticamente dentro de unos parámetros dados.
    '''
    disparo_maquina_x = random.randint(0, 9)
    disparo_maquina_y = random.randint(0, 9)
    return (disparo_maquina_x, disparo_maquina_y)
    