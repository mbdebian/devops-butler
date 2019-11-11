# 
# Project   : devops-butler
# Timestamp : 11-11-2019 23:08
# Author    : Manuel Bernal Llinares <mbdebian@gmail.com>
# ---
# 

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='devopsbutler',
    version='0.1.0',
    description='DevOps Management Helper',
    long_description=readme,
    author='Manuel Bernal Llinares',
    author_email='mbdebian@gmail.com',
    url='https://github.com/mbdebian/devops-butler',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
