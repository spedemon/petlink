
# petlink - Decode and encode PETlink streams. 
# Stefano Pedemonte
# Aalto University, School of Science, Helsinki
# Oct 2013, Helsinki 
# Jan 2015, Helsinki


# Use old Python build system, otherwise the extension libraries cannot be found. FIXME 
import sys
for arg in sys.argv: 
    if arg=="install":
        sys.argv.append('--old-and-unmanageable') 

from setuptools import setup, Extension
from glob import glob 

petlink32_c_module = Extension('petlink.petlink32_c', ['petlink/petlink32_c.c']) 

setup(
    name='petlink',
    version='0.3.4',
    author='Stefano Pedemonte',
    author_email='stefano.pedemonte@gmail.com',
    packages=['petlink', 'petlink.examples', 'petlink.tests'], 
    ext_modules=[petlink32_c_module, ],
    test_suite = "petlink.tests", 
    url='http://occiput.scienceontheweb.net/',
    license='LICENSE.txt',
    description='Decode and encode PETlink streams.',
    long_description=open('README.rst').read(),
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    install_requires=[
        "numpy >= 1.6.0", 
        "simplewrap >= 0.3.0", 
    ], 
)

