# SourceXtractor

SourceXtractor is a Python package that allows you to extract the URLs of javascript files from a website and find their sourcemaps. It then parses the sourcemaps and recreates the original contents of the javascript files in an output directory. 

## Installation

To install `sourcextractor`, you can use pip:

```bash
pip install sourcextractor
```


## Usage

Quickstart:

```bash
sourcextractor url output_dir [-d]
```

This will extract javascript files and sourcemaps from the website URL, parse them and recreate the original contents in the output directory. 

To find all available options

```bash
sourcextractor -h
```

## Features

- Extracts the URLs of javascript files from a website.
- Finds the sourcemaps of the javascript files.
- Parses the sourcemaps and recreates the original contents of the javascript files in the output directory.
- Optionally, you can enable debug logging by passing the -d flag.

## Dependencies

This package requires `beautifulsoup4` and `requests`. These will be installed automatically when you install `sourcextractor` using pip.

## How to Contribute

We welcome contributions from the community! If you want to contribute, please follow our [contribution guidelines](https://github.com/rmonvfer/sourcextractor/blob/master/CONTRIBUTING.md).

## License

SourceXtractor is released under the GPLv3 license. See [LICENSE](https://github.com/rmonvfer/sourcextractor/blob/master/LICENSE) for more information.

## Credits

SourceXtractor was created by [rmonvfer](https://github.com/rmonvfer) and is maintained by the open-source community.

