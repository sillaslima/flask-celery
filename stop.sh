#!/bin/bash

#python Camera_record_stop.py

pkill -f cronometro.sh

pkill -f ffmpeg

python3.6 teste.py

rm timeResult1.txt nohup.out timeResult.txt