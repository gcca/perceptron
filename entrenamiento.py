#!/gcca/bin/python

import pickle

import redneuronal
import imgpng

if __name__ == '__main__':
	rn = redneuronal.RedNeuronal(10, 35)

	conjuntoEntrenamiento = \
		[imgpng.ImgPNG(str(i) + '.png').decodificar() for i in xrange(10)]

	rn.entrenar(conjuntoEntrenamiento)

	with open('pesos','wt') as fichero:
		for p in rn.patrones:
			pickle.dump(p.pesos, fichero)

	for i in xrange(10):
		nombrePNG = str(i) + '.png'
		print nombrePNG, '->',	rn.patron(imgpng.ImgPNG(nombrePNG).decodificar())
