#!/bin/bash

python Camera_record_stop.py

pkill -f cronometro.sh

rm timeResult.txt nohup.out
