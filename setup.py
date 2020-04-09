from distutils.core import setup, Extension
from Cython.Distutils import build_ext
import numpy

libdr = ['/usr/local/lib', '/usr/lib/']
incdr = [numpy.get_include(), '/usr/local/include/', '/usr/include/opencv4/', '/usr/local/include/opencv4/']

ext = [
	Extension('cvt', ['python/cvt.pyx'],
		language = 'c++',
		extra_compile_args = ['-std=c++11'],
		include_dirs = incdr,
		library_dirs = libdr,
		libraries = ['opencv_core']),
	Extension('KCF', ['python/KCF.pyx', 'src/kcftracker.cpp', 'src/fhog.cpp'],
		language = 'c++',
		extra_compile_args = ['-std=c++11'],
		include_dirs = incdr,
		library_dirs = libdr,
		libraries = ['opencv_core', 'opencv_imgproc'])
]

setup(
	name = 'app',
	cmdclass = {'build_ext':build_ext},
	ext_modules = ext
)

#python setup.py build_ext --inplace
