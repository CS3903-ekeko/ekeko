import setuptools

with open("README.md", "r") as r:
    long_description = r.read()

setuptools.setup(
    name = "ekeko",
    version = "0.0.0",
    author = "Otreblan",
    description = "Ekeko",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CS3903-ekeko/ekeko",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
    ],
    install_requires=[
        "flask",
    ],
    entry_points={
        "console_scripts": [
            "ekeko = ekeko:main",
        ],
    },
)
