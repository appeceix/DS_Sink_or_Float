
BOARD_SIZE = 10



import numpy as np
import pandas as pd

tablero = np.full(fill_value="-", shape=(BOARD_SIZE, BOARD_SIZE))
print(tablero)

boat_size = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

cnt_boat = 0

while cnt_boat < 11:

    for i in boat_size: 
        orient = input("Dame la orientacion del barco:  N, S, E o W: ")
        colocar_x = int(input("Dame la coordenada X: "))
        colocar_y = int(input("Dame la coordenada Y: "))

        if orient == "N":
            if ((colocar_x-i+1) >= 0)&\
                (tablero[(colocar_x-i+1):(colocar_x+1), colocar_y] != "O").all():
                tablero[(colocar_x-i+1):(colocar_x+1), colocar_y] = "O"
                cnt_boat += 1
                print(cnt_boat)
            elif ((colocar_x-i+1) < 0):
                print("Te estás saliendo por arriba")
            else:
                print("Ya hay un barco ahí")
            print(tablero)            
            
        
        if orient == "S":
            if ((colocar_x+i) <= BOARD_SIZE)&\
                (tablero[colocar_x:(colocar_x+i), colocar_y] != "O").all():
                tablero[colocar_x:(colocar_x+i), colocar_y] = "O"
                cnt_boat += 1
                print(cnt_boat)
            elif ((colocar_x+i) > BOARD_SIZE):
                print("Te estás saliendo por abajo")
            else:
                print("Ya hay un barco ahí")
            print(tablero)            
                   
        
        if orient == "E":
            if ((colocar_y+i) <= BOARD_SIZE)&\
                (tablero[colocar_x, colocar_y:(colocar_y+i)] != "O").all():
                tablero[colocar_x, colocar_y:(colocar_y+i)] = "O"
                cnt_boat += 1
                print(cnt_boat)
            elif ((colocar_y+i) > BOARD_SIZE):
                print("Te estás saliendo por la derecha")
            else:
                print("Ya hay un barco ahí")
            print(tablero)            
            
        
        if orient == "W":
            if ((colocar_y-i+1) >= 0)&\
                (tablero[colocar_x, (colocar_y-i+1):(colocar_y+1)] != "O").all():
                tablero[colocar_x, (colocar_y-i+1):(colocar_y+1)] = "O"
                cnt_boat += 1
                print(cnt_boat)
            elif ((colocar_y-i+1) < 0):
                print("Te estás saliendo por la izquierda")
            else:
                print("Ya hay un barco ahí")
            print(tablero)            
            
    if cnt_boat == 10:
        break
