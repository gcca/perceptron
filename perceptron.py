from numpy import *

class Perceptron:
	'''
	Neurona :Perceptron

	:Parametros:
		pesos: vector de decimal
				Pesos de la neurona
		umbral: decimal
				Umbral de activacion

	:Formato:
		Ejemplo 1: para 2 criterios de entradas
			>>> 
				...
				
	'''
	def __init__(self, NEntradas):
		self.pesos = array([.0]*NEntradas) 
		self.umbral = 0.5
		self.radioEntrenamiento = 0.1
	
	def suma(self, entradas):
		'''
		Suma de las entradas ponderadas por los pesos

		:Parametros:
			entradas: vector
				Vector de entradas

		:Retorna:
			salida: decimal
				Suma ponderada

		'''

		return sum(self.pesos * entradas)

	def calcular(self, entradas):
		'''
		Calculo de activacion de la neurona

		:Parametros:
			entradas: vector
				Vector de entradas

		:Retorna:
			salida: bool en {0, 1}
				0 si desactivado
				1 si activado
				
		'''

		return 1 if self.suma(entradas) > self.umbral else 0

	def entrenar(self, conjuntoEntrenamiento):
		'''
		Entrenamiento de la neurona

		:Parametros:
			conjuntoEntrenamiento: vector
				Tuplas de entradas para el entrenamiento
				
		'''
		
		while True:
			entrenado = True
			
			for par in conjuntoEntrenamiento.items():
				resultado = self.calcular(par[0])
				error = par[1] - resultado
				
				if error != 0:
					entrenado = False
					
					for i, v in enumerate(par[0]):
						if v == 1:
							self.pesos[i] += \
								error * self.radioEntrenamiento
			if entrenado:
				break
