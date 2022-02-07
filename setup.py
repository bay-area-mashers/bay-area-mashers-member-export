from setuptools import setup

setup(
    name='bay-area-mashers-member-export',
    version='1.0.0',
    packages=['bay_area_mashers_member_export'],
    url='https://github.com/bay-area-mashers/bay-area-mashers-member-export',
    license='GPL-3.0',
    author='Gene Wood',
    author_email='gene_wood@cementhorizon.com',
    description='Tool to query Bay Area Mashers member list and return all current members\' email addresses',
    entry_points={
        "console_scripts": [
            "bay-area-mashers-member-export = bay_area_mashers_member_export:main"
        ]
    },
    requires=['gspread']
)
