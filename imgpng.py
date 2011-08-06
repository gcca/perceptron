import png

class ImgPNG:
	'''
	Imagen PNG

	:Parametros:
		fichero: cadena
			Nombre del fichero de imagen PNG
	
	'''
	def __init__(self, fichero = None):
		self.fichero = open(fichero)
		self.png = png.Reader(file = self.fichero)
		self.vector = []

	def decodificar(self):
		'''
		Decodificar la imagen PNG a vector binario
		
		'''
		
		if not self.vector:
			self.img = self.png.read()
			self.imgBin = list(self.img[2])

			for i in xrange(len(self.imgBin)/20):
				for j in xrange(len(self.imgBin[0])/(20*4)):
					self.vector.append(0 if self.imgBin[10+20*i][40+4*20*j] else 1)
			self.fichero.close()
			
		return self.vector
