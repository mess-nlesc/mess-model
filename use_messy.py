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
    # job_id, stdin, stdout, stderr = messy.submit_job(
    #     job_file="/home/xenon/test-slurm.job"
    # )
    # print(f'job_id: {job_id}')

    # # copy files to the server
    # messy.put_files(
    #     remote_folder="/home/xenon/",
    #     local_folder="./test_folder"
    # )

    # # download files from the server
    # messy.get_files(
    #     remote_folder="/home/xenon/test_folder",
    #     local_folder="./copy_of_test_folder"
    # )

    # # check if the required tools (commands) available on the host system
    # requirements_status = messy.check_required_tools(['docker', 'apptainer'])
    # print(f'Requirements status: {requirements_status}')

    # # build the apptainer image from the docker image
    # image_build_status = messy.build_apptainer_image(netlogo_version='6.3.0')
    # print(f'Image build status: {image_build_status}')

    # # generate a slurm job file
    # messy.generate_job_file(
    #     job_name='messy_experiment_job',
    #     job_time='0:30:00',
    #     model_path="/home/model/path",
    #     experiment_name="test_experiment",
    #     table_name="table_name"
    # )

    # # run a command on the remote system
    # messy.run_command_on_remote(command='ls -la', flush=True)
    # messy.run_command_on_remote(command='ls /')

    # # watch the slurm queue
    # messy.watch_slurm_queue()