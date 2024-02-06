import paramiko
import getpass
import time

class Messy:
    """This is a class to submit jobs to SLURM cluster
    """

    def __init__(self, username, hostname, port) -> None:
        self.username = username
        self.hostname = hostname
        self.port = port
        self.password = self.get_password()
        self.ssh_client = self.set_ssh_client()

    def get_password(self) -> str:
        """Sets user password"""
        password = getpass.getpass('Enter your password: ')
        return password

    def set_ssh_client(self) -> paramiko.SSHClient:
        """
        Creates an SSH client and connects to remote server
        """
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(
            self.hostname,
            port=self.port,
            username=self.username,
            password=self.password
        )
        return ssh_client

    def put_files(self) -> None:
        """
        Put files to the remote server
        """
        pass

    def get_files(self) -> None:
        """
        Get files from the remote server
        """
        pass

    def submit_job(self) -> None:
        """
        Submit job to SLURM cluster
        """
        stdin, stdout, stderr = self.ssh_client.exec_command('sbatch /home/xenon/test-slurm.job')
        job_id = int(stdout.read().decode().split()[-1])
        print(f'Submitted job with ID {job_id}')

    def monitor_jobs(self) -> None:
        """
        Check job status
        """
