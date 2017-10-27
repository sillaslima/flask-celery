#!/bin/bash

#python Camera_record_start.py 

#stauts=$?

#if [ $status != 0 ]; then
#   echo "Erro ao startar a Camera, verifique e reinicie"
#   exit 3
#else

#   sh cronometro.sh &
   #Copiar fluxo de video da live para a pasta local
#   ffmpeg -i rtsp://192.168.42.1:554/live -crf 30 -preset ultrafast -r 30 -codec:v copy videoCamera.avi &
 
#fi


ffmpeg -f x11grab -s 1440x900 -r 60 -i :0.0 screencast-`date +%d-%m-%Y_%H:%M:%S`.mp4
