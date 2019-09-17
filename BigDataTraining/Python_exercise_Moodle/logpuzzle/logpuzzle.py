"""Solves a puzzle using code."""

#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
from urllib.request import urlretrieve

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
    with open(filename) as fhand:
        urls = list()
        for line in fhand:
            words = line.split()
            server = filename.split('_')

            if 'puzzle' in words[6]:
                url = 'http://' + server[1] + words[6]

                if url not in urls:
                    urls.append(url)
        fhand.close()

    return urls

def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    dir_path = os.path.abspath(dest_dir)
    count = 0
    print('Retrieving...')

    for img in img_urls:
        file_path = dir_path + '\\img' + str(count) + '.jpg'
        count += 1
        urlretrieve(img, file_path)


    with open('./images/index.html', 'w+') as fhand:
        fhand.write('<verbatim>\n')
        fhand.write('<html>\n')
        fhand.write('<body>\n')

        img_num = 0
        while img_num < count:
            fhand.write('<img src="' + dir_path + '\\img' + str(img_num) + '.jpg">')
            img_num += 1
        fhand.write('\n')
        fhand.write('</body>\n')
        fhand.write('</html>')

        fhand.close()

def second_word_sort(url):
    """Helper function for sorting."""
    data = re.search(r'-\w+-(\w+).jpg', url)
    return data.group(1)

def main():
    """Main function."""
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        if args[0] == 'animal_code.google.com':
            download_images(sorted(img_urls), todir)
        else:
            download_images(sorted(img_urls, key=second_word_sort), todir)
    else:
        print('\n'.join(img_urls))

if __name__ == '__main__':
    main()
