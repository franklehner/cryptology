"""
setup.py
"""


from setuptools import setup, find_packages

setup(
    name="cryptology",
    version="0.0.1",
    author="Frank Lehner",
    author_email="frank.lehner@unity-mail.de",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "pdfminer",
        "sqlalchemy",
        "click",
        "pyPdf",
        "sqlalchemy",
        "psycopg2",
    ],
    test_requires=[
        "pytest",
    ]
)
