#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = [
    "requests",
    "validators"
]

setup(
    name="fisherman",
    version="1.0.1",
    author="Edward",
    author_email="14011954+0xedward@users.noreply.github.com",
    license="MIT",
    url="https://github.com/0xedward/fisherman",
    description="A tool for looking up an email address's reputation on EmailRep and Apility without API keys",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    download_url='https://github.com/0xedward/fisherman/archive/1.0.0.tar.gz',
    install_requires=requirements,
    classifiers=[
        "Topic :: Security",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    entry_points={"console_scripts": ["fisherman = fisherman.main:main"]},
    keywords=["security", "phishing"],
)