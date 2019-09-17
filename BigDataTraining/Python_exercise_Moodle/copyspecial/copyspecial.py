"""Code to copy special files in another directory and zip them."""

#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(directory):
    """Finds the special paths."""
    paths = list()

    for file_name in os.listdir(directory):
        name = re.search(r'__\w+__', file_name)

        if name:
            paths.append(os.path.abspath(file_name))

    return paths

def copy_to(paths, directory):
    """Copies files in a given directory."""
    if not os.path.exists(directory):
        os.mkdir(directory)

    dir_path = os.path.abspath(directory)

    for path in paths:
        shutil.copy(path, dir_path)

def zip_to(paths, zippath):
    """Creates zip file containing the files in the given directories."""
    concat_paths = ''
    for path in paths:
        concat_paths += path + ' '
    subprocess.call('zip -j ' + zippath + ' ' + concat_paths)

def main():
    """Main function."""
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if args is None:
        print("error: must specify one or more dirs")
        sys.exit(1)

  # +++your code here+++
  # Call your functions

    paths = list()

    for arg in args:
        paths += get_special_paths(arg)

    if todir:
        copy_to(paths, todir)
    if tozip:
        zip_to(paths, tozip)

if __name__ == "__main__":
    main()
