from setuptools import setup

setup(name='numeric_methods_dths', 
      version='0.1', 
      url='https://github.com/dthseemsbttr/Numeric-Methods-Dths', 
      license='MIT', 
      author='Vera Korotkova',
      author_email='verakorotkova10@mail.ru', 
      description='Numeric methods library',  
      long_description=open('README.md').read(),
      setup_requires=['sympy>=1.6.2', 'mpmath>=1.1.0', 'scipy>=1.5.2',
                      'numpy>=1.19.2,<1.21', 'matplotlib>=3.5.0',
                      'PyWavelets>=1.1.1', 'numba>=0.51.2',
                      'networkx>=2.5'],
      zip_safe=False)