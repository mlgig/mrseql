#!/usr/bin/env python3 -u
# coding: utf-8

__author__ = "Thach Le Nguyen"

from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize

ext = Extension('mrseql.mrseql',
                   language='c++',
                   sources=["src/mrseql/mrseql.pyx", "src/mrseql/seql_learn.cpp", "src/mrseql/SNode.cpp"],
                   extra_compile_args=["-std=c++11"],                   
                   include_dirs=['src/mrseql'])

setup(
    name='mrseql',
    version="0.0.1",
    author='Thach Le Nguyen',
    author_email='thalng@protonmail.com',
    setup_requires=[
        'setuptools',  
        'cython',
        'sktime',
    ],
    packages=find_packages(where='src'),
    package_dir={
        '': 'src'
    },
    #description='Example python module with cython.',
    #long_description=open('README.md').read(),
    ext_modules=cythonize([ext]),
)