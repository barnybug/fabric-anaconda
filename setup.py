from setuptools import setup, find_packages

setup(
    name="fabric-anaconda",
    version="0.0.4",
    author='Barnaby Gray',
    author_email='barnaby@pickle.me.uk',
    url='http://pypi.python.org/pypi/fabric-anaconda/',
    description=(
        "Some additional functions for working with anaconda environments "
        "in Fabric."
    ),
    long_description=open('README.rst').read(),
    packages=find_packages(),
    install_requires=[
        'Fabric'
    ]
)