from setuptools import setup, find_packages

import os
try:
    SLASHML_DIR = os.environ['SLASHML_DIR']
except:
    print('using the current directory as root for build')
    SLASHML_DIR = f'{os.getcwd()}/'

def read_req_file(req_type):
    with open(f"{SLASHML_DIR}requires-{req_type}.txt") as fp:  # pylint: disable=W1514
        requires = (line.strip() for line in fp)
        return [req for req in requires if req and not req.startswith("#")]

# Read the contents of the README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="slashml",
    version="0.1.5",
    url="https://slashml.com/",
    author="eff-kay",
    author_email="faiizan14@gmail.com",
    description=(
        "A Python client for interacting with SlashML services" "Developed by SlashML."
    ),
    long_description=long_description,  # Use the contents of the README file
    long_description_content_type="text/markdown",  # Set the type of the README file
    packages=find_packages("."),
    package_dir={"": "."},
    install_requires=read_req_file("install"),
    license="MIT",
    python_requires=">=3.6",
)
