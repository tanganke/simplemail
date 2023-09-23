from setuptools import setup, find_packages

setup(
    name="simplemail",
    version="0.1.0",
    description="A simple mail for sending mail",
    author="Anke Tang",
    packages=find_packages(),
    install_requires=["yagmail", "omegaconf"],
    entry_points={
        "console_scripts": [
            "simplemail=simplemail.cli:main",
        ]
    },
)
