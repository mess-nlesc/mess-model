#!/usr/bin/env python
"""A script to test Messy class
"""

from Messy import Messy

if __name__ == "__main__":

    messy = Messy(
        username='xenon',
        hostname='localhost',
        port=10022
    )

    messy.submit_job()
    messy.get_files(
        remote_folder="/home/xenon/",
        local_folder="./"
    )
