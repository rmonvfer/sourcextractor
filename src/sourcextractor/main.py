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

import argparse
import os
import logging
import requests
import json
from bs4 import BeautifulSoup
import urllib.parse

def parse_args():
    parser = argparse.ArgumentParser(description='Extract javascript files and sourcemaps from a website and recreate original contents in the output directory.')
    parser.add_argument('url', type=str, help='The website URL')
    parser.add_argument('output_dir', type=str, help='The output directory')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug logging')
    return parser.parse_args()

def extract_javascript_files(url):
    # Make a GET request to the website
    response = requests.get(url)

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract URLs of javascript files
    javascript_file_urls = []
    for link in soup.find_all('script'):
        src = link.get('src')
        if src:
            # If the URL is relative, make it absolute
            if not urllib.parse.urlparse(src).netloc:
                src = urllib.parse.urljoin(url, src)
            javascript_file_urls.append(src)

    return javascript_file_urls

def extract_sourcemap(javascript_file_url):
    # Make a GET request to the javascript file
    response = requests.get(javascript_file_url)

    # Search for the sourceMappingURL in the file
    sourcemap_url = None
    for line in response.text.splitlines():
        if line.startswith('//# sourceMappingURL='):
            sourcemap_url = line.split('=')[1]
            break

    return sourcemap_url

def parse_sourcemap(sourcemap_url):
    # Make a GET request to the sourcemap
    response = requests.get(sourcemap_url)
    sourcemap = json.loads(response.text)
    return sourcemap

def recreate_original_contents(sourcemap, output_dir):
    for file in sourcemap['sources']:
        original_file_content = requests.get(file).text
        filename = os.path.join(output_dir, os.path.basename(file))
        with open(filename, 'w') as f:
            f.write(original_file_content)

def main():
    args = parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    javascript_file_urls = extract_javascript_files(args.url)
    logging.debug(f'Found javascript files: {javascript_file_urls}')

    for javascript_file_url in javascript_file_urls:
        sourcemap_url = extract_sourcemap(javascript_file_url)
        if sourcemap_url:
            logging.debug(f'Found sourcemap: {sourcemap_url}')
            sourcemap = parse_sourcemap(sourcemap_url)
            recreate_original_contents(sourcemap, args.output_dir)
        else:
            logging.debug(f'No sourcemap found for {javascript_file_url}')

if __name__ == '__main__':
    main()
