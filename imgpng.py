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
		
		pass
