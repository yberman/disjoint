import setuptools

with open("README.md") as rm:
    long_description = rm.read()

setuptools.setup(
    name='disjoint',
    version='0.1.1',
    packages=setuptools.find_packages(),
    description='disjoint set data structure',
    url='https://github.com/yberman/disjoint',
    long_description=long_description,
    long_description_content_type='text/markdown',
    maintainer="yberman",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
