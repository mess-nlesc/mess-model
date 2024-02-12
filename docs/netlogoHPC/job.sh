#!/bin/bash
apptainer exec netlogo-headless.sif netlogo-headless.sh --model "/app/netlogo/models/IABM Textbook/chapter 4/Wolf Sheep Simple 5.nlogo" --experiment "Wolf Sheep Simple model analysis" --table wolf_sheep_output.csv
