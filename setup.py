from setuptools import find_packages, setup


setup(
    name='MFRC522',
    version='0.1.0',
    description='A small class to interface with the NFC reader Module MFRC522',
    py_modules=['mfrc522'],
    install_requires=[
        'SPI-Py==1.0'
    ]
)
