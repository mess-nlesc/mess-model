## Requirements
- Apptainer (https://apptainer.org/)

## Purpose
This document describes how to run a single Netlogo model on HPC using Apptainer container. We use the [Netlogo installation file](https://ccl.northwestern.edu/netlogo/6.3.0/NetLogo-6.3.0-64.tgz) as a base for our Apptainer container. The Apptainer container is then used to run the model in headless mode on HPC. The output is saved in a csv file.

## Build a container
Build a singularity container from the singularity definition file. A Linux system with sudo rights is needed.

```shell
sudo apptainer build netlogo-headless.sif netlogo-headless.def
```

This will create an image `netlogo-headless.sif` from the corresponding definition file in the current directory. This image can be used to run the model in headless mode on HPC.

## Prepare `job.sh` file

This line of code will execute a `netlogo-headless.sh` command within a singularity container. `--model` is an argument that specifies the NetLogo model to be run. The `--experiment` argument is optional and can be used to specify the name of the experiment. The `--table` argument is optional and can be used to specify the name of the output file.

```shell
apptainer exec netlogo-headless.sif netlogo-headless.sh --model "PATH TO MODEL IN YOUR HOME DIR" --experiment "EXPERIMENT NAME" --table OUTPUT.CSV
```

For example to run a model `Wolf Sheep Simple 5.nlogo` with an experiment `Wolf Sheep Simple model analysis` and save the output in `wolf_sheep_output.csv`, use the following command.

```shell
apptainer exec netlogo-headless.sif netlogo-headless.sh --model "/app/netlogo/models/IABM Textbook/chapter 4/Wolf Sheep Simple 5.nlogo" --experiment "Wolf Sheep Simple model analysis" --table wolf_sheep_output.csv
```

Alternatively, you can run your own model  `main.nlogo` with an experiment `experiment` and save the output in `output.csv`, use the following command.

```shell
#!/bin/bash  
apptainer exec NetlogoContainer/netlogo.sif netlogo-headless.sh --model "model/main.nlogo" --experiment "RD40to200_GC30_CSPHY3__50years" --table output.csv
```    

Place the code in the file `job.sh`, then change permissions to make it executable with

```shell
chmod +x job.sh
```

## Create archive to be copied to HPC 

Copy `model`, `container.sif`, and `job.sh` in the directory, say `jobHPC`.
Where `model` is a given model, `container.sif` is a container and `job.sh` is a shell script that contains command to be run.

Create a gzip tarball of a directory.

```shell
tar -czvf jobHPC.tar.gz jobHPC
```

## Copy to HPC

To copy a file from your local machine to HPC cluster, you can use the `scp` command.

```shell
scp jobHPC.tar.gz username@hpc:/path/to/your/directory
```
Replace `username@remote` with your username and the address of the HPC cluster. Replace `/path/to/remote/directory` with the path to the directory on the HPC cluster where you want to copy the file. This command will prompt you for your password on the HPC cluster before copying the file.

## Unpack the archive on HPC

```shell
tar -xzvf jobHPC.tar.gz
```

## Run model on HPC

```shell
sbatch --time=0-02:00:00 job.sh
```
