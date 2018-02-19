from setuptools import setup
import re, os

readme = ''
with open('README.rst') as f:
    readme = f.read()

setup(name='whapy',
      author='Efraim Rodrigues',
      author_email='efraimnaassom@gmail.com',
      url='https://github.com/efraimrodrigues/WhaPy',
      version= '0.2.0',
      packages=['whapy'],
      license='MIT',
      description='A python API for whatsapp web',
      long_description=readme,
      include_package_data=True,
      install_requires='selenium',
      classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
)