from setuptools import setup, find_packages

setup(
    name='slashml',
    version='1.0',
    author='faizank',
    author_email='faiizan14@gmail.com',
    description='python client for slashml',
    packages=find_packages(),
    install_requires=['requests'],
)