## Technical plan

### Model submission

1. Convert Netlogo docker image[1] into a singularity[2] image
1. Use Slurm Docker images[3] to imitate the SURF HPC cluster
1. Use pyxenon[4]
    - to copy the singularity image and the model files
    - submit the simulations
1. Run tests on HPC cluster

### New model generation

1. Convert current model into a jinja template[5]
1. Develop a Python CLI which
    - generates new models (see **Model submission**) based on a< user provided arguments
    - submits the new models to the HPC cluster
    - retrives the output files from the HPC cluster

## Links:

1. https://hub.docker.com/r/comses/netlogo
1. https://github.com/singularityhub/docker2singularity
1. https://github.com/xenon-middleware/xenon-docker-images/blob/master/slurm-20/README.md
1. https://github.com/xenon-middleware/pyxenon
1. https://palletsprojects.com/p/jinja/
