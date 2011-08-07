#!/gcca/bin/python

import sys

import redneuronal
import imgpng

if __name__ == '__main__':
	rn = redneuronal.RedNeuronal()

	rn.cargar('redneuronal')

  try:
  	print nombrePNG, '->',	rn.patron(imgpng.ImgPNG(sys.argv[1]).decodificar())

	except:
		for i in xrange(10):
			nombrePNG = str(i) + '.png'
			print nombrePNG, '->',	rn.patron(imgpng.ImgPNG(nombrePNG).decodificar())
