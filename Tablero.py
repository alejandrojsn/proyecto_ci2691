import pygame
import pygame.gfxdraw
import math

class Tablero:

	def __init__(self, x:int, y:int, ancho:int, alto:int, n:int):
		self.x = x
		self.endx = x + ancho
		self.y = y
		self.endy = y + alto
		self.ancho = ancho
		self.alto = alto
		self.n = n
		self.ancho_celda = ancho // n
		self.alto_celda = alto // n

	def dibujar(self, superficie, color, borde = 2):

		for i in range(1, self.n):

			x = self.x + self.ancho_celda*i
			y = self.y + self.alto_celda*i

			pygame.draw.aaline(superficie, color, (self.x, y), (self.endx, y), borde)
			pygame.draw.aaline(superficie, color, (x, self.y), (x, self.endy), borde)

	def esta_adentro(self, punto):
		if self.x <= punto[0] <= self.endx and self.y <= punto[1] <= self.endy:
			self.ultima_casilla = ((punto[1] - self.y) // self.alto_celda, (punto[0] - self.x) // self.ancho_celda)
			return True

		return False

	def dibujar_fichas(self, superficie, tablero, colores):
		for i in range(0, self.n):
			for j in range(0, self.n):
				y = self.y + self.alto_celda // 2 + self.alto_celda * i
				x = self.x + self.ancho_celda // 2 + self.ancho_celda * j
				r = min(self.ancho_celda, self.alto_celda) // 4
				if tablero[i][j] != 0:

					pygame.gfxdraw.filled_circle(superficie, x, y, r, colores[tablero[i][j]-1])
					pygame.gfxdraw.aacircle(superficie, x, y, r, colores[tablero[i][j]-1])