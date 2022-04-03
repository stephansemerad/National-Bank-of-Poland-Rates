from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION             = '0.0.9'
DESCRIPTION         = 'Get rates from the Polish National Bank (Narodowy Bank Polski)'
LONG_DESCRIPTION    = 'A package that allows you to retrieve the mid rate used for Accounting from the API directly of the Polish National Bank'

setup(
    name="pln_fx",
    version=VERSION,
    author="Stephan Semerad",
    author_email="<stephan.semerad@gmail.com>",
    url = "https://github.com/stephansemerad/National-Bank-of-Poland-Rates",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'poland', 'fx', 'exchange rates', 'exchange', 'pln', 'plnfx', 'zloty'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
