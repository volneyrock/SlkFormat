# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name ='SlkFormat',
    version='0.5',
    description='Formatador de dispositivos',
    author='volney',
    author_email='volneyrock@gmail.com',
    url='https://github.com/volneyrock/SlkFormat',
    packages=(['bin', 'bin.modules']),
    long_description="GUI para o formatador mkfs do linux",
    classifiers=[
        "Programming Language :: Python :: 2.7",
    ],
    keywords='formatador gráfico, linux formater, pendrive linux formater',
    license='GPL',
    scripts=['slk-format'],
 )

##python setup.py register
##python setup.py sdist upload  