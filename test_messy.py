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

    # submit a new job
    job_id, stdin, stdout, stderr = messy.submit_job(
        job_file="/home/xenon/test-slurm.job"
    )
    print(f'job_id: {job_id}')

    # copy files to the server
    messy.put_files(
        remote_folder="/home/xenon/",
        local_folder="./test_folder"
    )

    # download files from the server
    messy.get_files(
        remote_folder="/home/xenon/test_folder",
        local_folder="./copy_of_test_folder"
    )
