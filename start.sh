#!/bin/bash

#python Camera_record_start.py 

#stauts=$?

#if [ $status != 0 ]; then
#   echo "Erro ao startar a Camera, verifique e reinicie"
#   exit 3
#else
 
   sh cronometro.sh &
   #ffmpeg -f x11grab -s 1440x900 -r 60 -i :0.0 screencast-`date +%d-%m-%Y_%H:%M:%S`.mp4
   #Copiar fluxo de video da live para a pasta local
   
   #ffmpeg -filters
   #ffmpeg -i rtsp://192.168.15.64:554/ -crf 30 -preset ultrafast -r 30 -codec:v copy videoCamera.avi &
   ffmpeg -loglevel debug -rtsp_transport tcp -i rtsp://192.168.15.64:554 -c copy -map 0 videoCamera.avi &
 	
#fi


#ffmpeg -f x11grab -s 1440x900 -r 60 -i :0.0 screencast-`date +%d-%m-%Y_%H:%M:%S`.mp4
#ffmpeg -filters
#ffmpeg -filters | less |
#ffmpeg -y -i rtsp://192.168.15.64:554 -r 30 -codec:v copy videoCamera.avi
#ffmpeg -y -i rtsp://192.168.15.64:554 -r 30 default -c:v libx264 videoCamera.avi
#ffmpeg -rtsp_transport tcp -i rtsp://192.168.15.64:554 -c copy -map 0 videoCamera.avi
