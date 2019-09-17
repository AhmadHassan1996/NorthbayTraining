"""Creates an egg file for pymysql module."""

import os
import shutil
from setuptools import setup

if __name__ == "__main__":
    setup(
        name="pymysql",
        packages=['pymysql', 'pymysql.constants'],
        version="0.9.3",
        script_args=['--quiet', 'bdist_egg']
    )

    EGG_NAME = os.listdir('dist')[0]

    os.rename(
        os.path.join('dist', EGG_NAME),
        EGG_NAME
    )

    shutil.rmtree('build')
    shutil.rmtree('dist')
    shutil.rmtree('pymysql.egg-info')
