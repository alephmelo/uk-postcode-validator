from distutils.core import setup

setup(
    name='uk-postcode-validator',
    version='0.1.0',
    author='Aleph Melo',
    author_email='alephmelo@icloud.com',
    packages=['postcode_val'],
    url='https://github.com/alephmelo/uk-postcode-validator',
    license='LICENSE',
    description='Library to validate uk postcodes.',
    long_description=open('README.md').read(),
)