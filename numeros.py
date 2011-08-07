#!/gcca/bin/python

import redneuronal
import imgpng

if __name__ == '__main__':
	rn = redneuronal.RedNeuronal()

	rn.cargar('redneuronal')

	for i in xrange(10):
		nombrePNG = str(i) + '.png'
		print nombrePNG, '->',	rn.patron(imgpng.ImgPNG(nombrePNG).decodificar())
