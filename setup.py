import sys

from setuptools import setup, find_packages


if "--with-xunit" in sys.argv:
    sys.argv.remove("--with-xunit")

packages = [
    "pytest-cov",
    "pytest",
    "pytest-timeout",
    "pandas==1.3.4",
]

setup(
    name="sample-data-science",
    version="1.0.0",
    author="DevSkiller",
    author_email="support@devskiller.com",
    packages=find_packages(),
    install_requires=packages,
    tests_require=packages,
    setup_requires=["pytest-runner==5.2"],
    extras_require={"dev": ["black"]},
)
