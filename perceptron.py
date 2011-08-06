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

    pass

	def entrenar(self, conjuntoEntrenamiento):
		'''
		Entrenamiento de la neurona

		:Parametros:
			conjuntoEntrenamiento: vector
				Tuplas de entradas para el entrenamiento
				
		'''
		
    pass
