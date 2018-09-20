from setuptools import setup, find_packages

import pypadding


setup(
    name             = 'PyPadding',
    version          = pypadding.__version__,
    description      = 'Padding package when using block cryptography',
    long_description = open('README.md').read(),
    author           = 'Min Choro',
    author_email     = 'blinglnav@gmail.com',
    url              = 'https://github.com/blinglnav/pypadding',
    install_requires = [],
    packages         = find_packages(exclude = ['tests*']),
    keywords         = ['Padding', 'Cryptography', 'Encrypt', 'Decrypt',
                        'PKCS', 'PKCS#5', 'PKCS#7', 'ANSI x923', 'ISO 10126',
                        'ISO/IEC 7816-4'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
