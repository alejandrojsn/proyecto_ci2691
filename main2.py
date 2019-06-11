import sys, pygame, pygame.freetype
from Tablero import Tablero
from logic import *
from Jugador import Jugador

# Configuración de Pygame
pygame.init()
tamaño = ancho, alto = 800, 600
pantalla = pygame.display.set_mode(tamaño)

font = pygame.freetype.SysFont('Arial', 24)

# Colores
negro = 0, 0, 0
blanco = 255, 255, 255
azul = 0, 102, 255
rojo = 255, 0, 0

# Configuración pantalla introductoria
intro = True
jugadores = [Jugador(""), Jugador("")]
turno = 0
N = ""
n_error = False

# Pantalla introductoria
while intro:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			sys.exit()

		#elif event.type == pygame.MOUSEBUTTONDOWN:
			#intro = False

		elif event.type == pygame.KEYDOWN:

			if event.key == pygame.K_RETURN:

				if turno < 2:

					turno += 1 

				else:
					try:

						assert int(N) > 0
						intro = False

					except:
						n_error = True


			elif turno < 2:

				if event.key == pygame.K_BACKSPACE:

					jugadores[turno].nombre = jugadores[turno].nombre[:-1]

				else:

					jugadores[turno].nombre += event.unicode

			else:

				if event.key == pygame.K_BACKSPACE:

					N = N[:-1]

				else:
					valid_keys = "0123456789"#["0". "1", "2", "3", "4", "5", "6", "7", "8", "9"]

					if event.unicode in valid_keys:
						N += event.unicode

	pantalla.fill(negro)

	font.render_to(pantalla, (50, 50), "Ingrese el nombre del jugador 1:", blanco)
	font.render_to(pantalla, (50, 80), jugadores[0].nombre, blanco)

	if turno > 0:
		font.render_to(pantalla, (50, 110), "Ingrese el nombre del jugador 2:", blanco)
		font.render_to(pantalla, (50, 140), jugadores[1].nombre, blanco)

	if turno > 1:
		font.render_to(pantalla, (50, 170), "Ingrese el número de tableros,", blanco)
		font.render_to(pantalla, (50, 200), "filas y columnas:", blanco)
		font.render_to(pantalla, (50, 230), N, blanco)

	if n_error:
		font.render_to(pantalla, (50, 500), "N debe ser mayor que 0", rojo)

	pygame.display.flip()

# Configuración inicial del juego

N = int(N)
tablero_display = Tablero(100, 100, 400, 400, N)
primer_jugador = 0
otra_partida = True

while otra_partida:

	# Configuración inicial de la partida
	turno = primer_jugador
	primer_jugador = cambiar_jugador(primer_jugador)
	tab = 0
	tablero = [[[0 for k in range(N)] for j in range(N)] for i in range(N)]
	fichas = N**3


	# Pantalla Principal del Juego
	while quedan_fichas(fichas):

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				sys.exit()

			elif event.type == pygame.MOUSEBUTTONDOWN:

				pos = pygame.mouse.get_pos()

				if pygame.mouse.get_pressed()[0]:

					if tablero_display.esta_adentro(pos):
						fila, columna = tablero_display.ultima_casilla

						try:
							assert es_valida(tablero, N, tab, fila, columna)

							reflejar_jugada(tablero, tab, fila, columna, turno)

							if hay_linea(tablero, N, tab, fila, columna):
								sumar_lineas(tablero, N, tab, fila, columna, turno, jugadores)

							#print("Puntaje: \n {jugador1}: {puntaje1} \n {jugador2}: {puntaje2}".format(jugador1 = jugadores[0].nombre, jugador2 = jugadores[1].nombre, puntaje1 = jugadores[0].puntaje, puntaje2 = jugadores[1].puntaje))
							
							fichas -= 1
							turno = cambiar_jugador(turno)

						except:
							pass
							#print("Jugada inválida")


					elif 274 <= pos[0] <= 326:
						if 49 <= pos[1] <= 88:
							tab -= 1 if tab > 0 else 0
						elif 512 <= pos[1] <= 551:
							tab += 1 if tab < N-1 else 0

		pantalla.fill(blanco)
		pygame.draw.rect(pantalla, (236, 240, 241), (580, 0, 800, 600))
		pygame.draw.polygon(pantalla, azul, [(300, 49), (274, 88), (326, 88)])
		pygame.draw.polygon(pantalla, azul, [(300, 551), (274, 512), (326, 512)])
		tablero_display.dibujar(pantalla, negro)
		tablero_display.dibujar_fichas(pantalla, tablero[tab], [azul, rojo])
		font.render_to(pantalla, (255, 10), "Tablero {}".format(tab), negro)
		font.render_to(pantalla, (600, 10), "Puntaje:", negro)
		font.render_to(pantalla, (600, 40), jugadores[0].nombre, negro)
		font.render_to(pantalla, (600, 70), str(jugadores[0].puntaje), negro)
		font.render_to(pantalla, (600, 100), jugadores[1].nombre, negro)
		font.render_to(pantalla, (600, 130), str(jugadores[1].puntaje), negro)
		font.render_to(pantalla, (600, 160), "Turno: {}".format(jugadores[turno].nombre), negro)
		pygame.display.flip()

	outro = True
	# Pantalla Final
	while outro:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				print(pos)

				if pygame.mouse.get_pressed()[0]:
					if 230 <= pos[1] <= 260:
						if 50 <= pos[0] <= 80:
							outro = False
						elif 100 <= pos[0] <= 130:
							otra_partida = False
							outro = False

		pantalla.fill(negro)
		font.render_to(pantalla, (50, 50), "Puntaje:", blanco)
		font.render_to(pantalla, (50, 80), jugadores[0].nombre, blanco)
		font.render_to(pantalla, (50, 110), str(jugadores[0].puntaje), blanco)
		font.render_to(pantalla, (50, 140), jugadores[1].nombre, blanco)
		font.render_to(pantalla, (50, 170), str(jugadores[1].puntaje), blanco)
		font.render_to(pantalla, (50, 200), "¿Desea seguir jugando?", blanco)
		font.render_to(pantalla, (50, 230), "Si", blanco)
		font.render_to(pantalla, (100, 230), "No", blanco)
		pygame.display.flip()
