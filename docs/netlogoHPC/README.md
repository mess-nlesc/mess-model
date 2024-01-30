## Purpose
In this document we describe how to run a single Netlogo model on HPC using Apptainer container. We use the [Netlogo docker image](https://hub.docker.com/r/comses/netlogo) as a base for our Apptainer container. The Apptainer container is then used to run the model in headless mode on HPC. The output is saved in a csv file.

## Build
Build needs a Linux system with sudo rights.
```
./build.sh
```

`build.sh` will create an image `netlogo-headless.sif` from the corresponding definition file in the current directory. This image can be used to run the model in headless mode on HPC.

## Test
Run one of the examples provided by netlogo as a test.
```
./run.sh
```
## Run your own model in headless mode
```
apptainer exec netlogo-headless.sif netlogo-headless.sh --model "PATH TO MODEL IN YOUR HOME DIR" --experiment "EXPERIMENT NAME" --table OUTPUT.CSV
```
Or use the container executable directly to run the model. N.B. you need to escape the quotes in this example.
```
./netlogo-headless.sif --model \'/app/netlogo/models/IABM Textbook/chapter 4/Wolf Sheep Simple 5.nlogo\' --experiment \'Wolf Sheep Simple model analysis\' --table wolf_sheep_output.csv
```