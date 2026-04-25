import random

class Equipo:
    def __init__(self, nombre, partidosGanados = 0, partidosPerdidos = 0, setGanados = 0):

        self.nombre = nombre
        self.partidosGanados = partidosGanados
        self.partidosPerdidos = partidosPerdidos
        self.setGanados = setGanados
equipo1 = Equipo("Leones")
equipo2 = Equipo("Aguilas")



def RegistraSet(equipo_ganador):
    if equipo_ganador == 1:
        equipo1.setGanados += 1

        if equipo1.setGanados == 3:
            
            equipo1.partidosGanados += 1
            equipo2.partidosPerdidos += 1
            equipo1.setGanados = 0
            equipo2.setGanados = 0

    else:
        equipo2.setGanados += 1
        if equipo2.setGanados == 3:

            equipo2.partidosGanados += 1
            equipo1.partidosPerdidos += 1
            equipo1.setGanados = 0
            equipo2.setGanados = 0

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido():
    puntos1 = Puntos()
    puntos2 = Puntos()
    print(f"{equipo1.nombre}: {puntos1} pts")
    print(f"{equipo2.nombre}: {puntos2} pts")
    while not (puntos1 >= 25 or puntos2 >= 25):
        puntos1 += PuntosExtras()
        puntos2 += PuntosExtras()
        print(f"==> Puntos extras - {equipo1.nombre}: {puntos1} pts | {equipo2.nombre}: {puntos2} pts")
    if puntos1 > puntos2:
        RegistraSet(1)
        print(f"=> Gana el set: {equipo1.nombre}")
    else:
        RegistraSet(2)
        print(f"-> Gana el set: {equipo2.nombre}")

def ResultadoTorneo():
    print("=" * 30)
    print("RESULTADOS DEL TORNEO")
    print("=" * 30)
    print(f"{equipo1.nombre}:")
    print(f"- Partidos Ganados : {equipo1.partidosGanados}")
    print(f"- Partidos Perdidos: {equipo1.partidosPerdidos}")
    print(f"{equipo2.nombre}:")
    print(f"- Partidos Ganados : {equipo2.partidosGanados}")
    print(f"- Partidos Perdidos: {equipo2.partidosPerdidos}")
    print("=" * 30)

print("------JUEGO DE VOLEIBOL----------")
print("=" * 40)

while True:
    try:
        num_partidos = int(input("-> Cuantos partidos van a jugar: "))
        if num_partidos > 0:
            break
        else:
            print(" Ingrese un número mayor a cero")
    except ValueError:
        print(" Ingrese un número valido.")

print(f"Juego de {num_partidos} partidos: {equipo1.nombre} vs {equipo2.nombre}")

for i in range(1, num_partidos + 1):
    print(f"{'=' * 20} PARTIDO #{i} {'=' * 20}")
    JugarPartido()
ResultadoTorneo()