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
