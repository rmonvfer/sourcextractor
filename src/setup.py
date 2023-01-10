# Copyright (C) 2023 Ramón Vila.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(
    name='sourcextractor',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/rmonvfer/sourcextractor',
    license='MIT',
    author='Ramón Vila Ferreres',
    author_email='ramonvilafer@proton.me',
    description='A package to extract javascript files and sourcemaps from a website and recreate original contents in the output directory',
    install_requires=['beautifulsoup4','requests'],
    entry_points={
        'console_scripts': [
            'sourcextractor = sourcextractor.main:main',
        ],
    }
)
