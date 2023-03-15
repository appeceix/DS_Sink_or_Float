BOARD_SIZE = 10


import numpy as np
import pandas as pd
import random

tablero = np.full(fill_value="-", shape=(BOARD_SIZE, BOARD_SIZE))
print(tablero)
tablero1 = np.full(fill_value="-", shape=(BOARD_SIZE, BOARD_SIZE))

boat_size = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
boat_size1 = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
cnt_boat = 0
cnt_boat1 = 0

# while cnt_boat < 10:

#     for i in boat_size: 
#         orient = input("Dame la orientacion del barco:  N, S, E o W: ")
#         colocar_x = int(input("Dame la coordenada X: "))
#         colocar_y = int(input("Dame la coordenada Y: "))

#         if orient == "N":
#             if ((colocar_x-i+1) >= 0)&\
#                 (tablero[(colocar_x-i+1):(colocar_x+1), colocar_y] != "O").all():
#                 tablero[(colocar_x-i+1):(colocar_x+1), colocar_y] = "O"
#                 cnt_boat += 1
#                 print(cnt_boat)
#             elif ((colocar_x-i+1) < 0):
#                 print("Te estás saliendo por arriba")
#             else:
#                 print("Ya hay un barco ahí")
#             print(tablero)            
            
        
#         if orient == "S":
#             if ((colocar_x+i) <= BOARD_SIZE)&\
#                 (tablero[colocar_x:(colocar_x+i), colocar_y] != "O").all():
#                 tablero[colocar_x:(colocar_x+i), colocar_y] = "O"
#                 cnt_boat += 1
#                 print(cnt_boat)
#             elif ((colocar_x+i) > BOARD_SIZE):
#                 print("Te estás saliendo por abajo")
#             else:
#                 print("Ya hay un barco ahí")
#             print(tablero)            
                   
        
#         if orient == "E":
#             if ((colocar_y+i) <= BOARD_SIZE)&\
#                 (tablero[colocar_x, colocar_y:(colocar_y+i)] != "O").all():
#                 tablero[colocar_x, colocar_y:(colocar_y+i)] = "O"
#                 cnt_boat += 1
#                 print(cnt_boat)
#             elif ((colocar_y+i) > BOARD_SIZE):
#                 print("Te estás saliendo por la derecha")
#             else:
#                 print("Ya hay un barco ahí")
#             print(tablero)            
            
        
#         if orient == "W":
#             if ((colocar_y-i+1) >= 0)&\
#                 (tablero[colocar_x, (colocar_y-i+1):(colocar_y+1)] != "O").all():
#                 tablero[colocar_x, (colocar_y-i+1):(colocar_y+1)] = "O"
#                 cnt_boat += 1
#                 print(cnt_boat)
#             elif ((colocar_y-i+1) < 0):
#                 print("Te estás saliendo por la izquierda")
#             else:
#                 print("Ya hay un barco ahí")
#             print(tablero)            
            
#         if cnt_boat == 10:
#             print("\nTablero 1 con barcos colocados:")
#             print(tablero)
#             break
        
    
    
        
print(tablero1)        
     

while cnt_boat1 < 10:

    letras_orient = ["N", "S", "E", "W"] # Lista para seleccionar orientación válida
    
    for i in boat_size1:
        
        colocado = False
        
        while not colocado:
            
            orient = random.choice(letras_orient) # Elige una orientación aleatoria
            colocar_x = random.randint(0, 9)  # Da coordenada aleatoria
            colocar_y = random.randint(0, 9)

            if orient == "N":

                if ((colocar_x-i+1) >= 0)&\
                    (tablero1[(colocar_x-i+1):(colocar_x+1), colocar_y] != "O").all():
                    tablero1[(colocar_x-i+1):(colocar_x+1), colocar_y] = "O"
                    colocado = True
                    print(cnt_boat1)
                    print(tablero1) 

                elif ((colocar_x-i+1) < 0):
                    print("Te estás saliendo por arriba")


                else:
                    print("Ya hay un barco ahí")


            if orient == "S":

                if ((colocar_x+i) <= BOARD_SIZE)&\
                    (tablero1[colocar_x:(colocar_x+i), colocar_y] != "O").all():
                    tablero1[colocar_x:(colocar_x+i), colocar_y] = "O"
                    colocado = True
                    print(cnt_boat1)
                    print(tablero1) 

                elif ((colocar_x+i) > BOARD_SIZE):
                    print("Te estás saliendo por abajo")


                else:
                    print("Ya hay un barco ahí")


            if orient == "E":

                if ((colocar_y+i) <= BOARD_SIZE)&\
                    (tablero1[colocar_x, colocar_y:(colocar_y+i)] != "O").all():
                    tablero1[colocar_x, colocar_y:(colocar_y+i)] = "O"
                    colocado = True
                    print(cnt_boat1)
                    print(tablero1) 

                elif ((colocar_y+i) > BOARD_SIZE):
                    print("Te estás saliendo por la derecha")


                else:
                    print("Ya hay un barco ahí")



            if orient == "W":

                if ((colocar_y-i+1) >= 0)&\
                    (tablero1[colocar_x, (colocar_y-i+1):(colocar_y+1)] != "O").all():
                    tablero1[colocar_x, (colocar_y-i+1):(colocar_y+1)] = "O"
                    colocado = True
                    print(cnt_boat1)
                    print(tablero1) 

                elif ((colocar_y-i+1) < 0):
                    print("Te estás saliendo por la izquierda")


                else:
                    print("Ya hay un barco ahí")

        cnt_boat1 += 1
        if cnt_boat1 == 10:
            print("\nTablero 2 con barcos colocados:")
            print(tablero1)
            break

def disparo_jugador():
    disparo_jugador_x = int(input("Dime coordanada X: "))
    disparo_jugador_y = int(input("Dime coordanada Y: "))
    return (disparo_jugador_x, disparo_jugador_y)
    

def disparo_maquina():
    disparo_maquina_x = int(input("Dime coordanada X: "))
    disparo_maquina_y = int(input("Dime coordanada Y: "))
    return (disparo_maquina_x, disparo_maquina_y)

vidas_jugador = 20
vidas_maquina = 20

while vidas_maquina > 0 and vidas_jugador > 0:

    while vidas_maquina > 0:

        disparo_jugador_x, disparo_jugador_y = disparo_jugador()

        if disparo_jugador_x < 0 or disparo_jugador_x >= BOARD_SIZE or \
           disparo_jugador_y < 0 or disparo_jugador_y >= BOARD_SIZE:
            print("Coordenadas inválidas. Vuelve a intentarlo.")
            continue

        if tablero1[disparo_jugador_x, disparo_jugador_y] == "X" or \
           tablero1[disparo_jugador_x, disparo_jugador_y] == "T":
            print("Ya has disparado en esa casilla. Vuelve a intentarlo.")
            continue

        if tablero1[disparo_jugador_x, disparo_jugador_y] == "O":
            tablero1[disparo_jugador_x, disparo_jugador_y] = "X"
            vidas_maquina -= 1
            print("¡Le has dado!")
            print(tablero1)

        
        
        if tablero1[disparo_jugador_x, disparo_jugador_y] == "-":
            tablero1[disparo_jugador_x, disparo_jugador_y] = "T"
            print("Disparo fallido. Cambio de turno")
            print(tablero1)
            break
        if vidas_maquina == 0:
            print("¡Felicidades, has ganado!")
            break

    while vidas_jugador > 0:

        disparo_maquina_x, disparo_maquina_y = disparo_maquina()

        if disparo_maquina_x < 0 or disparo_maquina_x >= BOARD_SIZE or \
           disparo_maquina_y < 0 or disparo_maquina_y >= BOARD_SIZE:
            print("Coordenadas inválidas. Vuelve a intentarlo.")
            continue

        if tablero[disparo_maquina_x, disparo_maquina_y] == "X" or \
           tablero[disparo_maquina_x, disparo_maquina_y] == "T":
            print("La máquina ya ha disparado en esa casilla. Vuelve a intentarlo.")
            continue

        if tablero[disparo_maquina_x, disparo_maquina_y] == "O":
            tablero[disparo_maquina_x, disparo_maquina_y] = "X"
            vidas_jugador -= 1
            print("¡Le has dado!")
            print(tablero)
        
        
        if tablero[disparo_maquina_x, disparo_maquina_y] == "-":
            tablero[disparo_maquina_x, disparo_maquina_y] = "T"
            print("Disparo fallido. Cambio de turno")
            print(tablero)
            break

        if vidas_jugador == 0:
            print("¡Lo siento, ha ganado la maquina! Intentalo de nuevo")
            break

