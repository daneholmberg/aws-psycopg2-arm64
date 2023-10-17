import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("version.txt", "r") as fv:
    version = fv.read().strip()

setuptools.setup(
    name="aws-psycopg2-arm64",
    version=version,
    author="Dane H",
    description="A aws psycopg2 package from psycopg2 compatible with arm64 (graviton).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AbhimanyuHK/aws-psycopg2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
