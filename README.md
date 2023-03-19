# DS_Sink_or_Float
Proyecto para desarrollar el clásico juego "Hundir la flota" como parte del curso en Data Science en TheBridge School.

### Resumen
Cada jugador tiene un tablero compuesto por una matriz 10x10 colocará sus barcos. El objetivo es disparar adivinando la posición de los barcos del enemigo para "hundirlos" todos. 

Cada posición ocupada por un barco es una vida (20 vidas en total por jugador). Una vez uno de los dos llega a 0 vidas, se acaba el juego.

### Desarrollo
Los tableros se generan a partir de una matriz 10x10. Hay tres tableros: uno para cada jugador y otro tablero "visor" para que nosotros registremos nuestro historial de disparos.

Las posiciones del jugador se introducen barco a barco de forma manual indicando orientación según puntos cardinales y coordenadas desde 0 a 9. El programa identifica automáticamente el tamaño del barco (primero 4 barcos de tamaño 1, luego 3 de tamaño 2, 2 de tamaño 3 y para terminar 1 de tamaño 4). Los barcos no pueden salir de la matriz ni superponerse unos con otros. Las posiciones de la máquina se deciden aleatoriamente con unos parámetros dados.

Una vez posicionados los barcos comienzan los turnos de disparos mientras los jugadores tengan más de 0 vidas. Los disparos del jugador se introducen mediante coordenadas en los ejes X e Y. En caso de indicar una coordenada no válida el juego devuelve un error y nos pide otra válida. Las coordenadas de disparo del enemigo son elegidas aleatoriamente. Si un disparo acierta, el mismo jugador vuelve a disparar. Una vez falla el disparo, cambia el turno al otro jugador. Nuestros disparos acertados y fallidos son registrados en nuestro visor para llevar la cuenta de dónde hemos disparado. La máquina está configurada para no disparar donde ya lo ha hecho antes.

Los turnos de disparos transcurren sucesivamente empezando por el jugador. Una vez uno de los dos jugadores pierde todas sus vidas, se acaba el juego.

El programa está desarrollado íntegramente en Python con programación funcional. Las librerías utilizadas son Numpy, Random, Time, Sys y Os. Si bien se podría jugar en la terminal, lo ideal es hacerlo en un IDE ya que el programa contiene ciertas configuraciones como iconos o sonidos que la terminal estándar no soporta.

## Autores
Ismael Merino Limón
Mattheus Zottis
José Manuel Prado Appeceix