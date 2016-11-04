from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name="fabric-anaconda",
    version="0.0.2",
    author='Barnaby Gray',
    author_email='barnaby@pickle.me.uk',
    url='http://pypi.python.org/pypi/fabric-anaconda/',
    description=(
        "Some additional functions for working with anaconda environments "
        "in Fabric."
    ),
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'Fabric'
    ]
)