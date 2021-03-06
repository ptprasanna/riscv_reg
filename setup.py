# See LICENSE.incore.incore for details

"""The setup script."""

from setuptools import setup, find_packages
import os

# Base directory of package
here = os.path.abspath(os.path.dirname(__file__))


# def read(*parts):
#     with codecs.open(os.path.join(here, *parts), 'r') as fp:
#         return fp.read()
# def read_requires():
#     with open(os.path.join(here, "riscv_reg/requirements.txt"),"r") as reqfile:
#         return reqfile.read().splitlines()

# #Long Description
# with open("README.rst", "r") as fh:
#     readme = fh.read()

setup_requirements = [ ]

test_requirements = [ ]

setup(
    name='riscv_reg',
    version='0.0.1',
    description="RISC-V REG",
    # long_description=readme + '\n\n',
    classifiers=[
          "Programming Language :: Python :: 3.6",
          "License :: OSI Approved :: BSD License",
          "Development Status :: 1 - alpha"
    ],
    # url='https://github.com/ptprasanna/riscv_reg',
    # author="IITM",
    # author_email='riscvreg@gmail.com',
    # license="BSD-3-Clause",
    packages=find_packages(),
    package_dir={'riscv_reg': 'riscv_reg'},
    package_data={
        'riscv_reg': [
            'requirements.txt',
            'data/*',
            'env/*'
            ]
        },
    # install_requires=read_requires(),
    python_requires='>=3.6.0',
    entry_points={
        'console_scripts': [
            'riscv_reg=riscv_reg.main:cli',
        ],
    },
    include_package_data=True,
    keywords='riscv_reg',
    test_suite='tests',
    tests_require=test_requirements,
    zip_safe=False,
    install_requires=['pandas']
)
