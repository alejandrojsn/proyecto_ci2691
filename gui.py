import os
from Jugador import Jugador

def dibujar_tablero(tab:[[int]], N:int) -> None:

	for i in range(N):
		line = ""
		for j in range(N):
			line += ' x ' if tab[i][j] == 1 else (' o ' if tab[i][j] == 2 else '   ')
			line += '|' if j < N-1 else ''

		print(line)
		if(i < N-1):
			print('-'*(4*N-1))

def dibujar_supertablero(supertab:[[[int]]], N:int) -> None:
	for index,tab in enumerate(supertab):
		print('\n Tablero {}:'.format(index))
		dibujar_tablero(tab, N)

def borrar():
	os.system('cls' if os.name=='nt' else 'clear')

def obtener_jugada(nombre:str) -> None:
	print("Juega {}".format(nombre))
	return int(input("Ingrese el número del tablero en el que desea jugar \n")), \
	int(input("Ingrese el número de la fila en la que desea jugar \n")), \
	int(input("Ingrese el número de la columna en la que desea jugar \n"))

def imprimir_puntaje(jugadores:[Jugador]) -> None:
	print("Puntaje:")
	for jugador in jugadores:
		print("{}: {}".format(jugador.nombre, jugador.puntaje))

def preguntar_seguir_jugando() -> bool:
	seguir = str(input("Desea seguir jugando? [y] \n"))
	return True if(seguir.lower() == "y") else False