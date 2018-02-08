#!/usr/bin/env bash

imagem_abertura=$1
imagem_propaganda=$2
video_normal=$3
video_slow=$4
dir=`pwd`

ffmpeg -y \
 -loop 1 -t 3 \
 -i $1 \
 -loop 1 -t 3 \
 -i $2 \
 -i $3 -an \
 -i $4 -an \
-filter_complex \
"[3:v]setpts=1.7*PTS[v0]; \
 [0:v]scale=1440x900,setdar=8:5,setsar=1:1[v1]; \
 [1:v]scale=1440x900,setdar=8:5,setsar=1:1[v2];\
 [1:v]scale=1440x900,setdar=8:5,setsar=1:1[v3];\
 [v1][2:v][v2][v0][v3]concat=n=5:v=1,format=yuv420p[out]" -map "[out] -c copy" $dir/tmp/video_extraido/FutShow-`date +%d-%m-%Y_%H:%M:%S`.mp4



#ffmpeg -y \
# -loop 1 -t 3 \
# -i $1 \
# -loop 1 -t 3 \
# -i $2 \
# -i $3 -an \
# -i $4 -an \
#-filter_complex \
#"[3:v]setpts=1.7*PTS[v0]; \
# [0:v]scale=1920x1080,setdar=16:9,setsar=1:1[v1]; \
# [1:v]scale=1920x1080,setdar=16:9,setsar=1:1[v2];\
# [1:v]scale=1920x1080,setdar=16:9,setsar=1:1[v3];\
# [v1][2:v][v2][v0][v3]concat=n=5:v=1,format=yuv420p[out]" -map "[out] -c copy" $dir/tmp/video_extraido/FutShow-`date +%d-%m-%Y_%H:%M:%S`.mp4