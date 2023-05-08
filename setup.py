from setuptools import setup, find_packages

import os
SLASHML_DIR = os.environ['SLASHML_DIR']

def read_req_file(req_type):
    with open(f"{SLASHML_DIR}requires-{req_type}.txt") as fp:  # pylint: disable=W1514
        requires = (line.strip() for line in fp)
        return [req for req in requires if req and not req.startswith("#")]


setup(
    name="slashml",
    version="0.1.1",
    url="https://slashml.com/",
    author="eff-kay",
    author_email="faiizan14@gmail.com",
    description=(
        "A Python client for interacting with SlashML services" "Developed by SlashML."
    ),
    packages=find_packages("slashml"),
    install_requires=read_req_file("install"),
    license="MIT",
    python_requires=">=3.6",
)
