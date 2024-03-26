## Motivation
Imagine you have a Netlogo model that you want to run on a High-Performance Computing (HPC) system. You have access to the HPC system via SSH, but you do not have the necessary permissions to install Netlogo on the system or you do not know how. Also you want to run the model without Graphical User Interface (GUI) because it avoids overhead and makes your model run faster.

## Purpose
The purpose of this document is to demostrate how to run a single Netlogo model on HPC using [Apptainer](https://apptainer.org/) container. We use the [Netlogo](https://ccl.northwestern.edu/netlogo/6.3.0/NetLogo-6.3.0-64.tgz) installation file as a base for the container. Apptainer container allows to package model and dependencies (i.e. Netlogo) in a single image that can be run uniformly across different systems with different environments. Apptainer is particularly suitable for HPC, as it integrates with common job schedulers and does not require root access to run. The container is then used to run the Netlogo model in headless mode. The headless mode is a mode in which the model is run without the graphical user interface and he output is saved in a csv file.

## Requirements
- Apptainer 
- a Linux system with sudo rights
- BASH shell
- access to a HPC system via SSH

## Build a container
Build an apptainer container on a local machine from a definition file. A Linux system with sudo rights is needed. 

```shell
sudo apptainer build netlogo-headless.sif netlogo-headless.def
```

This will create an apptainer image `netlogo-headless.sif` from the corresponding definition file in the current directory. This image can be used to run the model in headless mode on HPC.

## Prepare `job.sh` file

We need to create a shell script that contains the command to run the model in headless mode. First we look at how to run the model in headless mode without a container.

```shell
./netlogo-headless.sh --model "PATH_TO_MODEL" --experiment "EXPERIMENT_NAME" --table OUTPUT.CSV
```
The line of code above will execute a `netlogo-headless.sh` command, where 
- `--model` is an argument that specifies the NetLogo model to be run;
- `--experiment` argument is optional and can be used to specify the name of the experiment;
- `--table` argument is optional and can be used to specify the name of the output file.

If we want to execute the same command using apptainer we need to modify the above command as following:

```shell
apptainer exec netlogo-headless.sif netlogo-headless.sh --model "PATH_TO_MODEL" --experiment "EXPERIMENT_NAME" --table OUTPUT.CSV
```

For example to run a model `Wolf Sheep Simple 5.nlogo` with an experiment `Wolf Sheep Simple model analysis` and save the output in `wolf_sheep_output.csv`, use the following command.

```shell
apptainer exec netlogo-headless.sif netlogo-headless.sh --model "/app/netlogo/models/IABM Textbook/chapter 4/Wolf Sheep Simple 5.nlogo" --experiment "Wolf Sheep Simple model analysis" --table wolf_sheep_output.csv
```

Alternatively, you can run your own model  `main.nlogo` with an experiment `experiment` and save the output in `output.csv`, use the following command.

```shell
#!/bin/bash  
apptainer exec netlogo-headless.sif netlogo-headless.sh --model "model/main.nlogo" --experiment "RD40to200_GC30_CSPHY3__50years" --table output.csv
```    
Where `model/main.nlogo` is the path to your model and `RD40to200_GC30_CSPHY3__50years` is the name of the experiment. 

We save the code above as `job.sh` and change permissions to make it executable with

```shell
chmod +x job.sh
```

## Create an archive to be copied to HPC

To run our model on HPC, we need to copy all files to the remote machine. First, we create an archive on a local machine that contains the model, the container, and the shell script. For this, we create a directory and copy `model`, `netlogo-headless.sif`, and `job.sh` into it and call this directory `jobHPC`. Then we create a gzip tarball of a directory.

```shell
tar -czvf jobHPC.tar.gz jobHPC
```

## Copy to HPC

To copy `jobHPC.tar.gz` file from your local machine to HPC cluster, we can use the `scp` command. This command will copy `jobHPC.tar.gz` file to the remote machine using SSH (Secure Shell) protocol for data transfer.

```shell
scp jobHPC.tar.gz username@remote:/path/to/your/directory
```
Replace `username@remote` with your username and the address of the HPC cluster. Replace `/path/to/remote/directory` with the path to the directory on the HPC cluster where you want to copy the file. This command will prompt you for your password on the HPC cluster before copying the file.

## Unpack the archive on HPC

Once file is copied to the HPC cluster, login to the remote machine and unpack the archive using the following command:

```shell
tar -xzvf jobHPC.tar.gz
```

## Run model on HPC

Submit job to a (SLURM) scheduler on HPC using the following command:

```shell
sbatch --time=0-02:00:00 job.sh
```
Here, we set a limit of 2 hours for the job to run. You can change the time limit as per your requirement.
