import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Refactoring",
    version="0.0.1",
    author="Marianalb",
    author_email="mariana_bento97@hotmail.com",
    description="A simple library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Marianalb/Refactoring.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)