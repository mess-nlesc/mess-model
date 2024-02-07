import os
import time
import getpass
import paramiko
from stat import S_ISDIR, S_ISREG

# setup logging
paramiko.util.log_to_file("Messy.log")

class Messy:
    """This is a class to submit jobs to SLURM cluster
    """
    def __init__(self, username, hostname, port) -> None:
        self.username = username
        self.hostname = hostname
        self.port = port
        self.password = self.get_password()
        self.transport = self.set_transport()
        self.ssh_client = self.set_ssh_client()
        self.sftp_client = self.set_sftp_client()

    def get_password(self) -> str:
        """Sets user password"""
        password = getpass.getpass('Enter your password: ')
        return password

    def set_transport(self) -> paramiko.Transport:
        """
        Creates an paramiko transport
        """
        transport = paramiko.Transport((self.hostname, self.port))
        return transport

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

    def set_sftp_client(self) -> paramiko.SFTPClient:
        """
        Creates a SFTP client
        """
        self.transport.connect(
            username=self.username,
            password=self.password
        )
        sftp_client = paramiko.SFTPClient.from_transport(self.transport)
        return sftp_client

    def put_files(self, remote_folder: str) -> None:
        """
        Put files to the remote server
        """
        pass

    def create_remote_folder(self, remote_folder: str) -> None:
        """
        Create a folder in the remote server
        """
        try:
            self.sftp_client.mkdir(remote_folder)
        except IOError:
            print(f"(assuming {remote_folder}/ already exists)")

    def get_files(self, remote_folder: str, local_folder: str = "./") -> None:
        """
        Get files from the remote server
        """
        if not os.path.exists(local_folder):
            os.mkdir(local_folder)

        for entry in self.sftp_client.listdir_attr(remote_folder):
            remotepath = remote_folder + "/" + entry.filename
            localpath = os.path.join(local_folder, entry.filename)
            mode = entry.st_mode
            if S_ISDIR(mode):
                try:
                    os.mkdir(localpath)
                except OSError:
                    pass
                self.get_files(remotepath, localpath)
            elif S_ISREG(mode):
                self.sftp_client.get(remotepath, localpath)


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
