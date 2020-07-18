from setuptools import setup
import pathlib


LICENSE = 'Apache License 2.0'
HERE = pathlib.Path(__file__).parent

setup(name='okra_py',
    version='1.1',
    description='Python wrapper for Okra API',
    long_description = (HERE / "README.md").read_text(),
    long_description_content_type = "text/markdown",
    url='https://github.com/Uchencho/okra_py',
    author="Uchenna Alozie",
    author_email='alozieuche17@gmail.com',
    license=LICENSE,
    install_requires=['requests'],
    packages=['okra_py'],
    )