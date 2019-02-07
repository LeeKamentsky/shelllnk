from setuptools import setup

version = "1.0.0"

with open("./README.md") as fd:
    long_description = fd.read()

setup(
    name="shelllnk",
    version=version,
    description="Package for parsing Microsoft Shell Link (.lnk) files",
    long_description = long_description,
    author="Lee Kamentsky",
    packages=["shelllnk"],
    entry_points = dict(
        console_scripts=[
            "shelllnk-info=shelllnk.main:main"
        ]),
    url="https://github.com/leekamentsky/shelllnk",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3"
    ]
    )