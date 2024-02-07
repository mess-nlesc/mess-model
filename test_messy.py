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

    # # submit a new job
    # messy.submit_job()

    # # download files from the server
    # messy.get_files(
    #     remote_folder="/home/xenon/filesystem-test-fixture",
    #     local_folder="./copy_test"
    # )

    # copy files to the server
    messy.put_files(
        remote_folder="/home/xenon/",
        local_folder="./test_folder"
    )
