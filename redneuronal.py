#!/gcca/bin/python

import pickle

import perceptron

class RedNeuronal:
	'''
	Red Neuronal :Perceptron

	:Parametros:
		NPatrones: Perceptron
				Umbral de activacion

	:Formato:
		Ejemplo 1: para 4 patrones
			>>> 
				...
				
	'''
	def __init__(self, NPatrones, NEntradas):
		self.patrones = [perceptron.Perceptron(NEntradas) for _ in xrange(NPatrones)]

	def entrenar(self, conjuntoEntrenamiento):
		'''
		Entrenamiento de la Red Neuronal

		:Parametros:
			conjuntoEntrenamiento: vector
				Tuplas de entradas para el entrenamiento
				Si es una lista o tupla no especifica salida
				Si es un diccionario espeficica salida
		
		'''
		
		if type(conjuntoEntrenamiento) is list or \
			 type(conjuntoEntrenamiento) is tuple:
			for i in xrange(len(conjuntoEntrenamiento)):
				resultado = [0] * len(conjuntoEntrenamiento)
				resultado[i] = 1

				self.patrones[i].entrenar(
					dict(zip(conjuntoEntrenamiento, resultado)))
		else:
			for i in xrange(len(conjuntoEntrenamiento)):
				resultado = [0] * len(conjuntoEntrenamiento)
				resultado[i] = conjuntoEntrenamiento.values()[i]
				
				self.patrones[i].entrenar(
					dict(zip(conjuntoEntrenamiento.keys(), resultado)))
			
	def calcular(self, entradas):
		'''
		Calculo de activacion de la Red Neuronal

		:Parametros:
			entradas: vector
				Vector de entradas

		:Retorna:
			salida: vector
				Vector con los patrones que se activan
				
		'''
		
		resultado = []

		for patron in self.patrones:
			resultado.append(patron.calcular(entradas))

		return resultado

	def patron(self, entradas):
		'''
		Numero de patron reconocido

		:Parametros:
			entradas: vector
				Vector de entradas

		:Retorna:
			salida: entero
				Numero que representa al primer patron reconocido
		
		'''
		
		return self.calcular(entradas).index(1)

	def valor(self, entradas):
		'''
		Activacion del patron

		:Parametros:
			entradas: vector
				Vector de entradas

		:Retorna:
			salida: bool {0, 1}
				0 si desactivado
				1 si activado
		
		'''

		return 1 if 1 in self.calcular(entradas) else 0

	def cargar(self, fichero):
		'''
		Carga la Red Neuronal desde un fichero

		:Parametros:
			fichero: cadena
				Nombre del fichero

		'''

		with open(fichero) as fichero:
			for p in self.patrones:
				p.pesos = pickle.load(fichero)

	def guardar(self, fichero):
		'''
		Guarda la Red Neuronal a un fichero

		:Parametros:
			fichero: cadena
				Nombre del fichero

		'''

		with open(fichero,'w') as fichero:
			for p in self.patrones:
				pickle.dump(p.pesos, fichero)
