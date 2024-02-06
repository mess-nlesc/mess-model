# see: https://github.com/paramiko/paramiko/blob/main/demos

import paramiko
import getpass
import time


# get user credentials
password = getpass.getpass('Enter your password: ')

# connect using ssh
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('localhost', port=10022, username='xenon', password=password)

# submit a batch job
stdin, stdout, stderr = ssh.exec_command('sbatch /home/xenon/test-slurm.job')
job_id = int(stdout.read().decode().split()[-1])
print(f'Submitted job with ID {job_id}')

