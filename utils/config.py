def MENSAJE_BIENVENIDA():
    import time
    mensaje_inicio = "CARGANDO EL JUEGO..."
    
    for letra in mensaje_inicio:
        time.sleep(0.05)

        print(f"{letra}", end=" ")
    
MENSAJE_BIENVENIDA()
