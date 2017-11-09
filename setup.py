from setuptools import setup
import re, os

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

readme = ''
with open('README.md') as f:
    readme = f.read()

setup(name='whapy',
      author='Efraim Rodrigues',
      url='https://github.com/efraimrodrigues/WhaPy',
      version=0.0.1,
      packages=['whapy'],
      license='MIT',
      description='A python API for whatsapp web',
      long_description=readme,
      include_package_data=True,
      install_requires=requirements,
      classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
      ]
)