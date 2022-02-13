# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bay-area-mashers-member-export',
    version='1.0.0',
    packages=['bay_area_mashers_member_export'],
    url='https://github.com/bay-area-mashers/bay-area-mashers-member-export',
    license='GPL-3.0',
    author='Gene Wood',
    author_email='gene_wood@cementhorizon.com',
    description='Tool to query Bay Area Mashers member list and return all current members\' email addresses',
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        "console_scripts": [
            "bay-area-mashers-member-export = bay_area_mashers_member_export:main"
        ]
    },
    install_requires=['gspread']
)
