import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'malleefowl',
    'nose',
    ]

classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        ]

setup(name='emu',
      version='0.1.2',
      description='WPS processes for testing and demo',
      long_description=README + '\n\n' + CHANGES,
      classifiers=classifiers,
      author='Birdhouse',
      url='https://github.com/bird-house/emu',
      license = "Apache License v2.0",
      keywords='wps PyWPS Python Malleefowl',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      install_requires=requires,
      entry_points = {
          'console_scripts': [
              ]}     
      ,
      )
