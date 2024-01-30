## Requirements

- Apptainer (https://apptainer.org/)

## Instructions

1. Convert [`comses/netlogo`](https://github.com/comses/docker-netlogo/blob/main/Dockerfile) Docker image to an apptainer image

    ```shell
    apptainer pull docker://comses/netlogo:6.3.0
    ```

    This will generate an apptainer container file called `netlogo_6.3.0.sif`.

1. Running the model using the apptainer image

    To start a shell run:

    ```shell
    apptainer shell netlogo_6.3.0.sif
    ```

    To start NetLogo run:

    ```shell
    apptainer exec netlogo_6.3.0.sif /opt/netlogo/bin/NetLogo
    ```

    To run an example NetLogo model run:

    ```shell
    apptainer exec netlogo_6.3.0.sif /opt/netlogo/netlogo-headless.sh --model "/opt/netlogo/models/IABM Textbook/chapter 4/Wolf Sheep Simple 5.nlogo" --experiment "Wolf Sheep Simple model analysis" --table wolf_sheep_output.csv
    ```

    If you need to change environment variables, for example to increase amount memory to be used by NetLogo, you can add `--env` flag to the command above. Below is an example allocating 8G of memory.

    ```shell
    apptainer exec --env "JAVA_TOOL_OPTIONS=-Xmx8G" netlogo_6.3.0.sif /opt/netlogo/netlogo-headless.sh --model "/opt/netlogo/models/IABM Textbook/chapter 4/Wolf Sheep Simple 5.nlogo" --experiment "Wolf Sheep Simple model analysis" --table wolf_sheep_output.csv
    ```