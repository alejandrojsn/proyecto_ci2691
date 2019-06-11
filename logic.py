from Jugador import Jugador

def quedan_fichas(fichas:int) -> bool:

	"""
	Parámetros:
	fichas (int): el número de fichas que quedan por jugar

	Retorna:
	(bool) Verdadero si fichas es mayor que 0, Falso en caso contrario
	"""

	return True if fichas > 0 else False

def es_valida(T:[[[int]]], N:int, tab:int, fila:int, col:int) -> bool:

	"""
	Parámetros:
	T ([[[int]]]): lista de lista de lista de enteros, representando los tableros
	N (int): el número de tableros,filas y columnas
	tab (int): el tablero de la celda jugada
	fila (int): la fila de la celda jugada
	col (int): la columna de la celda jugada

	Retorna:
	(bool) Verdadero si la jugada es válida, Falso en caso contrario

	Comportamiento:
	Checa que tanto el tablero como la fila y la columna sean mayores o iguales que 0 y menores que N,
	y que la celda jugada no haya sido jugada aún (T[tab][fila][col] == 0)
	"""

	return 0 <= tab < N and 0 <= fila < N and 0 <= col < N and T[tab][fila][col] == 0

def hay_linea_horizontal(T:[[[int]]], N:int, tab:int, fila:int) -> bool:

	"""
	Parámetros:
	T ([[[int]]]): lista de lista de lista de enteros, representando los tableros
	N (int): el número de tableros,filas y columnas
	tab (int): el tablero de la celda jugada
	fila (int): la fila de la celda jugada

	Retorna:
	(bool) Verdadero si todas las celdas de la fila tienen el mismo valor Falso en caso contrario
	"""

	return all(T[tab][fila][i] != 0 and T[tab][fila][i] == T[tab][fila][i+1] for i in range(N-1))

def hay_linea_vertical(T:[[[int]]], N:int, tab:int, col:int) -> bool:

	"""
	Parámetros:
	T ([[[int]]]): lista de lista de lista de enteros, representando los tableros
	N (int): el número de tableros,filas y columnas
	tab (int): el tablero de la celda jugada
	col (int): la fila de la celda jugada

	Retorna:
	(bool) Verdadero si todas las celdas de la columna tienn el mismo valor, Falso en caso contrario
	"""

	return all(T[tab][i][col] != 0 and T[tab][i][col] == T[tab][i+1][col] for i in range(N-1))

def hay_linea_diagonal(T:[[[int]]], N:int, tab:int, fila:int, col:int) -> int:

	"""
	Parámetros:
	T ([[[int]]]): lista de lista de lista de enteros, representando los tableros
	N (int): el número de tableros,filas y columnas
	tab (int): el tablero de la celda jugada
	fila (int): la fila de la celda jugada
	col (int): la fila de la celda jugada

	Retorna:
	(int) El número de lineas diagonales que hay 

	Comportamiento:
	Checha si la fila y la columna son iguales, en dado caso, la celda forma parte de la diagonal
	principal, por lo que checa que todas las celdas cuyas filas y columnas son iguales tengan el mismo valor. 

	Si suecede, suma 1 a result

	Checa que la suma de la fila con la columna sea igual a N-1, en dado caso, la celda forma parte de la
	diagonal secundaria, por lo que checha que todas las celdas cuyas filas y columnas suman N-1 tengan el mismo valor.

	Si sucede, suma 1 a result

	Retorna result
	"""
	result = 0;
	if(fila==col):
		result += 1 if all(T[tab][i][i] != 0 and T[tab][i][i] == T[tab][i+1][i+1] for i in range(N-1)) else 0
	if(fila+col == N-1):
		result += 1 if all( T[tab][i][N-1-i] != 0 and T[tab][i][N-1-i] == T[tab][i+1][N-2-i]  for i in range(N-1)) else 0
	
	return result

def hay_linea_tableros(T:[[[int]]], N:int, fila:int, col:int) -> bool:

	"""
	Parámetros:
	T ([[[int]]]): lista de lista de lista de enteros, representando los tableros
	N (int): el número de tableros,filas y columnas
	fila (int): la fila de la celda jugada
	col (int): la fila de la celda jugada
	
	Retorna:
	(bool) Verdadero si todas las celdas [fila][col] de los diferentes tableros tienen el mismo valor,
	Falso en caso contrario
	"""

	return all(T[i][fila][col] != 0 and T[i][fila][col] == T[i+1][fila][col] for i in range(N-1))

def hay_linea(T:[[[int]]], N:int, tab:int, fila:int, col:int) -> bool:

	"""
	Parámetros:
	T ([[[int]]]): lista de lista de lista de enteros, representando los tableros
	N (int): el número de tableros,filas y columnas
	tab (int): el tablero de la celda jugada
	fila (int): la fila de la celda jugada
	col (int): la fila de la celda jugada

	Retorna:
	(bool) Verdadero si se formó una línea en la fila, columna, diagonal o columna tridimensional de la celda
	jugada, Falso en caso contrario
	"""

	return any([hay_linea_horizontal(T, N, tab, fila), hay_linea_vertical(T, N, tab, col),\
		hay_linea_diagonal(T, N, tab, fila, col), hay_linea_tableros(T, N, fila, col)])

def sumar_lineas(T:[[[int]]], N:int, tab:int, fila:int, col:int, turno:int, jugadores:[Jugador]) -> None:

	"""
	Parámetros:
	T ([[[int]]]): lista de lista de lista de enteros, representando los tableros
	N (int): el número de tableros,filas y columnas
	tab (int): el tablero de la celda jugada
	fila (int): la fila de la celda jugada
	col (int): la fila de la celda jugada

	Retorna:
	result (int): el número de líneas formadas al jugar la celda
	
	Comportamiento:
	Inicializa result en 0, suma 1 por cada línea formada
	"""

	result = 0
	result += 1 if hay_linea_horizontal(T, N, tab, fila) else 0
	result += 1 if hay_linea_vertical(T, N, tab, col) else 0
	result += hay_linea_diagonal(T, N, tab, fila, col)
	result += 1 if hay_linea_tableros(T, N, fila, col) else 0
	
	jugadores[turno].puntaje += result

def reflejar_jugada(T:[[[int]]], tab:int, fila:int, col:int, turno:int) -> None:

	"""
	Parámetros:
	T ([[[int]]]): lista de lista de lista de enteros, representando los tableros
	N (int): el número de tableros,filas y columnas
	tab (int): el tablero de la celda jugada
	fila (int): la fila de la celda jugada
	col (int): la fila de la celda jugada
	turno (int): 0 si es el turno del jugador 1, 1 si es el turno del jugador 2

	Comportamiento:
	Cambia la celda T[tab][fila][col] a 1 si es el turno del jugador 1, 2 si es el turno del jugador 2
	"""

	T[tab][fila][col] = turno+1

def cambiar_jugador(turno:int) -> int:

	"""
	Parámetros:
	turno (int): 0 si es el turno del jugador 1, 1 si es el turno del jugador 2

	Retorna:
	(int) 0 si es el turno del jugador 2, 1 si es el turno del jugador 1
	"""

	return 0 if turno else 1
