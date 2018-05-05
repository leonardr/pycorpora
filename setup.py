from __future__ import print_function
try:
    from setuptools import setup
    from setuptools.command.install import install
except ImportError:
    from distutils.core import setup
    from distutils.command.install import install
import glob
import io
import zipfile


setup(
    name="pycorpora",
    version="0.1.2",
    packages=['pycorpora'],
    package_data={'pycorpora': ['data/*/*.json', 'data/*/*/*.json']},
    author="Allison Parrish",
    author_email="allison@decontextualize.com",
    description="A Python wrapper for Darius Kazemi's Corpora Project",
    url="https://github.com/aparrish/pycorpora",
    license="LICENSE.txt",
    long_description=open("README.rst").read(),
    keywords="nlp corpus text language",
    entry_points = {
        'console_scripts': [
            "pycorpora-download = pycorpora.downloader:main"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Artistic Software",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"],
)
