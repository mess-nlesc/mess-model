## Requirements

- Apptainer 1.2.5 or newer (https://apptainer.org/)
- Python 3.11.X or newer

## 1. Prepare and run Apptainer Image

1. Convert [`comses/netlogo`](https://github.com/comses/docker-netlogo/blob/main/Dockerfile) Docker image to an apptainer image

    ```shell
    apptainer pull docker://comses/netlogo:6.3.0
    ```

    This will generate an apptainer container file called `netlogo_6.3.0.sif`.

1. Running the model using the apptainer image

    To run an example NetLogo model run:

    ```shell
    apptainer exec netlogo_6.3.0.sif /opt/netlogo/netlogo-headless.sh --model "/opt/netlogo/models/IABM Textbook/chapter 4/Wolf Sheep Simple 5.nlogo" --experiment "Wolf Sheep Simple model analysis" --table wolf_sheep_output.csv
    ```

    If you need to change environment variables, for example to increase amount memory to be used by NetLogo, you can add `--env` flag to the command above. Below is an example allocating 8G of memory by adding `JAVA_TOOL_OPTIONS=-Xmx8G` environment variable.

    ```shell
    apptainer exec --env "JAVA_TOOL_OPTIONS=-Xmx8G" netlogo_6.3.0.sif /opt/netlogo/netlogo-headless.sh --model "/opt/netlogo/models/IABM Textbook/chapter 4/Wolf Sheep Simple 5.nlogo" --experiment "Wolf Sheep Simple model analysis" --table wolf_sheep_output.csv
    ```

    ### Other useful commands

    If you want to start a shell inside a container run:

    ```shell
    apptainer shell netlogo_6.3.0.sif
    ```

    If you want to start NetLogo GUI run:

    ```shell
    apptainer exec netlogo_6.3.0.sif /opt/netlogo/bin/NetLogo
    ```

## 2. Set up a local SLURM cluster

To emulate an HPC system we will run [SLURM](Workload Manager) workload manager in a Docker container. The Docker image we will use canbe found at [`xenon-docker-images`](https://github.com/xenon-middleware/xenon-docker-images.git) repository.

First, pull the latest docker image:

```shell
docker pull xenonmiddleware/slurm:latest
```

To start SLURM run:

```shell
docker run --detach --publish 10022:22 xenonmiddleware/slurm:latest
```

This will start the service in the background and you will be able to connect to it via ssh.

To connect run:

```shell
ssh -p 10022 xenon@localhost -t /bin/bash
```

The password for xenon user is `javagat`.


**Note: It may take a few minutes for SLURM service to start. Please be patient ;)**

You can now submit a test jobs:

```shell
sbatch /home/xenon/test-slurm.job
```

You can check the status of the job with

```shell
squeue
sacct
```

## 3. Use pyxenon to submit jobs

Create a new Python virtual environment

```shell
python3 -m venv venv
```

Activate the virtual environment

```shell
. ./venv/bin/activate
```

Upgrade pip

```shell
pip install --upgrade pip wheel
```

Install requirements

```shell
pip install -r requirements.txt
```

Run the test script which copies files to a remote server (HPC running SLURM) and submits a job.

```shell
python3 test_messy.py
```
