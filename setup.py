import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iterable-api", # Replace with your own username
    version="0.0.1",
    author="Alex Kahn",
    author_email="alex.kahn@outlook.com",
    description="Iterable API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexkahn/iterable-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)