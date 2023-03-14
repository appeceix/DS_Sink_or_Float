class Jugador:
    vidas = 20
    def __init__(self, tipo_jugador):
        self.tipo = tipo_jugador

jose = Jugador("jugador")
maquina = Jugador("máquina")

if jose.tipo == "jugador":
    print("Jose es un jugador")