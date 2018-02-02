from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
 
setup(
  name = 'qatest',
  ext_modules=cythonize([
    Extension("qatest", ["qatest.pyx"]),
    ]),
)
 