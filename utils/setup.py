from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import sys

def _compile_alpha(file_name):
    print(file_name)
    setup(ext_modules = cythonize([file_name]), script_args=['build_ext'])