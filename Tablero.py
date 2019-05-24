import pygame

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

	def dibujar(self, superficie, color, borde = 4):

		for i in range(1, self.n):

			x = self.x + self.ancho_celda*i
			y = self.y + self.alto_celda*i

			pygame.draw.line(superficie, color, (self.x, y), (self.endx, y), borde)
			pygame.draw.line(superficie, color, (x, self.y), (x, self.endy), borde)

	def esta_adentro(self, punto):
		if self.x <= punto[0] <= self.endx and self.y <= punto[1] <= self.endy:
			self.ultima_casilla = ((punto[1] - self.y) // self.alto_celda, (punto[0] - self.x) // self.ancho_celda)
			return True

		return False