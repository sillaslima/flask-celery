#!/bin/bash

#python Camera_record_stop.py

pkill -f cronometro.sh

pkill -f ffmpeg

rm timeResult1.txt nohup.out timeResult.txt