from logic import * 
from gui import * 
from Jugador import Jugador

jugadores = [Jugador(str(input("Ingrese el nombre del jugador {}: \n".format(i)))) for i in range(1, 3)]
N = int(input("Ingrese el numero de filas, columnas y tableros: \n"))
otra_partida = True
empieza = 0

while(otra_partida):
	
	tablero = [[[0 for k in range(N)] for j in range(N)] for i in range(N)]
	turno = empieza
	empieza = cambiar_jugador(empieza)
	fichas = N**3

	while(quedan_fichas(fichas)):
		
		dibujar_supertablero(tablero, N)

		while(True):
			
			tab, fila, col = obtener_jugada(jugadores[turno].nombre)
			
			if(es_valida(tablero, N, tab, fila, col)):
				break
			else:
				print("Jugada inválida")

		reflejar_jugada(tablero, tab, fila, col, turno)

		borrar()

		if(hay_linea(tablero, N, tab, fila, col)):
			sumar_lineas(tablero, N, tab, fila, col, turno, jugadores)

		imprimir_puntaje(jugadores)
		turno = cambiar_jugador(turno)

		fichas = fichas - 1

	borrar()
	imprimir_puntaje(jugadores)
	otra_partida = preguntar_seguir_jugando()