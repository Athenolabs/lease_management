from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='lease_management',
    version=version,
    description='Lease Management Details',
    author='Indictrans',
    author_email='saurabh.p@indictranstech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
