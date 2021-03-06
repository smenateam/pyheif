# thirdparty
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyheif",
    version="0.5.1",
    packages=["pyheif"],
    install_requires=["cffi>=1.0.0", "six>=1.15.0"],
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["libheif/libheif_build.py:ffibuilder"],
    author="David Poirier",
    author_email="david-poirier-csn@users.noreply.github.com",
    description="Python 2.7+ interface to libheif library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">= 2.7",
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
    keywords="heif heic",
    url="https://github.com/smenateam/pyheif",
)
