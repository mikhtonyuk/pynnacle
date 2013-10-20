from setuptools import setup, find_packages

KEYWORDS = 'networking codec connection pooling service futures finagle'.split(' ')
SUMMARY = 'Finagle-inspired networking abstraction library for Python'
DESCRIPTION = '''Finagle-inspired networking abstraction library for Python'''

setup(name='pynnacle',
      version='0.0.1',
      url='https://github.com/mikhtonyuk/pynnacle',
      author='Sergii Mikhtoniuk',
      author_email='mikhtonyuk@gmail.com',
      license='MIT',
      description=SUMMARY,
      long_description=DESCRIPTION,
      keywords=KEYWORDS,
      packages=find_packages(exclude=['*_test']),
      zip_safe=False,
      test_suite='pynnacle_test')