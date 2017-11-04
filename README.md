# flask-celery
chamada assincrona flask

1. sudo ./run-redis.sh
2. celery worker -A app.celery --loglevel=info
3. python3 app.y
4. http://localhost:5000/


############Comando FFMPEG##############
ffmpeg -loop 1 -i futshow_branco_1920_1080.png -c:v libx264 -t 3 -pix_fmt yuv420p futshow_branco_1920_1080.avi

ffmpeg -i Intro_FutPlay.avi -i 45941.avi -i fechamento.avi  -filter_complex '[0:v] [1:v] [2:v] concat=n=3:v=1 [v]' -map '[v]' 506521.avi

ffmpeg -loop 1 -i futshow_branco_1920_1080.png -c:v libx264 -t 3 -pix_fmt yuv420p -vf scale=1920x1080,setdar=16:9,setsar=1:1 futshow_branco_1920_1080.avi

#Gerar video de teste
ffmpeg -f lavfi -i smptebars=duration=10:size=640x360:rate=30 teste.mp4

############Comando FFMPEG##############


ps -ef | grep cronometro

 https://gist.github.com/mowings/6960b8058daf44be1b4e

 https://v4-alpha.getbootstrap.com/components/forms/


