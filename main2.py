import sys, pygame, pygame.freetype
from Tablero import Tablero
from logic import *
from Jugador import Jugador

pygame.init()
pygame.font.init()

jugadores = [Jugador("Alejandro"), Jugador("Cristian")]

tamaño = ancho, alto = 600, 600
negro = 0, 0, 0
blanco = 255, 255, 255
azul = 0, 102, 255
rojo = 255, 0, 0
N = 3
font = pygame.freetype.SysFont('Arial', 24)

pantalla = pygame.display.set_mode(tamaño)

tablero_display = Tablero(100, 100, 400, 400, N)

tablero = [[[0 for k in range(N)] for j in range(N)] for i in range(N)]

tab = 0

turno = 0

while True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			sys.exit()

		elif event.type == pygame.MOUSEBUTTONDOWN:

			pos = pygame.mouse.get_pos()

			if pygame.mouse.get_pressed()[0]:

				if tablero_display.esta_adentro(pos):
					fila, columna = tablero_display.ultima_casilla
					print(fila, columna)

					try:
						assert es_valida(tablero, N, tab, fila, columna)

						reflejar_jugada(tablero, tab, fila, columna, turno)

						if hay_linea(tablero, N, tab, fila, columna):
							sumar_lineas(tablero, N, tab, fila, columna, turno, jugadores)

						turno = cambiar_jugador(turno)

						print(tablero)

					except:
						print("Jugada inválida")


				elif 274 <= pos[0] <= 326:
					if 49 <= pos[1] <= 88:
						tab -= 1 if tab > 0 else 0
					elif 512 <= pos[1] <= 551:
						tab += 1 if tab < N else 0


	pantalla.fill(blanco)
	pygame.draw.polygon(pantalla, azul, [(300, 49), (274, 88), (326, 88)])
	pygame.draw.polygon(pantalla, azul, [(300, 551), (274, 512), (326, 512)])
	tablero_display.dibujar(pantalla, negro)
	tablero_display.dibujar_fichas(pantalla, tablero[tab], [azul, rojo])
	font.render_to(pantalla, (255, 10), "Tablero {}".format(tab), negro)
	pygame.display.flip()