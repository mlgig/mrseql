# #!/usr/bin/env python3 -u
# # coding: utf-8

# __author__ = "Thach Le Nguyen"

# from setuptools import setup, Extension, find_packages
# from Cython.Build import cythonize

# ext = Extension('mrseql.mrseql',
#                    language='c++',
#                    sources=["src/mrseql/mrseql.pyx", "src/mrseql/seql_learn.cpp", "src/mrseql/SNode.cpp"],
#                    extra_compile_args=["-std=c++11"],                   
#                    include_dirs=['src/mrseql'])

# setup(
#     name='mrseql',
#     version="0.0.2",
#     author='Thach Le Nguyen',
#     author_email='thalng@protonmail.com',
#     setup_requires=[
#         'setuptools',  
#         'cython',
#         'sktime',
#     ],
#     packages=find_packages(where='src'),
#     package_dir={
#         '': 'src'
#     },
#     #description='Example python module with cython.',
#     #long_description=open('README.md').read(),
#     ext_modules=cythonize([ext]),
# )

__author__ = "Thach Le Nguyen"

from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize
import os 

def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()

def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            # __version__ = "0.9"
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")

cstuff = Extension('mrseql.mrseql',
                   language='c++',
                   sources=["src/mrseql/mrseql.pyx","src/mrseql/seql_learn.cpp", "src/mrseql/SNode.cpp","src/mrseql/sfa/MFT.cpp","src/mrseql/sfa/DFT.cpp","src/mrseql/sfa/SFA.cpp","src/mrseql/sfa/TimeSeries.cpp"],
                   extra_compile_args=["-Wall", "-Ofast", "-g", "-std=c++11", "-ffast-math"],
                   extra_link_args=["-lfftw3", "-lm", "-L/opt/local/lib"],           
                   include_dirs=['src/mrseql'])

setup(
    name='mrseql',
    version=get_version("src/mrseql/__init__.py"),
    author='Thach Le Nguyen',
    author_email='thalng@protonmail.com',
    python_requires='>=3.7',
    install_requires=[
        "numpy>=1.18",
        "pandas>=1.0.3",
        "scikit-learn >= 0.22",        
    ],
    packages=find_packages(where='src'),
    package_dir={
        '': 'src'
    },
    description='MrSEQL',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    ext_modules=cythonize([cstuff]),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)