#-*- coding: utf-8 -*-
import os,shutil,time
import glob
import subprocess
from random import randint
import threading
import pdb


def geraNome():
    a = randint(0,90000)
    ext ='.avi'
    nome_arquivo = str(a)+ext
    return nome_arquivo
def retira_audio(video):
    print(video)
    sem_audio = video
    nome_audio=geraNome()
    retira_audio = ['ffmpeg', '-i',sem_audio,'-y','-an', nome_audio]
    print('----------------APLICANDO EFEITO PARA RETIRAR O AUDIO------------------')
    an = subprocess.Popen(retira_audio,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
    saida_audio=an.wait()
    if saida_audio == 0:
        print ('AUDIO RETIRADO COM SUCESSO',nome_audio)
        #rm = os.unlink(sem_audio)
        #rm = os.unlink(video_slow)
        mv = shutil.move(sem_audio, './Audio')
        print('move com sucesso')

    else:
        print ('PROBLEMAS AO RETIRAR O AUDIO')
    return nome_audio
def gerar_slow(video_gerar_slow):
    print('----PARAMETRO RECEBIDO',video_gerar_slow)
    slow=video_gerar_slow
    nome_slow=geraNome()
    aplica_slow = [
        'ffmpeg',
        '-i',
        slow,
        '-y',
        '-filter:v',
        'setpts=1.7*PTS',
        nome_slow
    ]
    print('----------------APLICANDO EFEITO PARA GERAR O SLOW MOTION------------------')
    slow_motion = subprocess.Popen(aplica_slow,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
    saida_slow = slow_motion.wait()
    if saida_slow == 0:
        print('SLOW MOTION GERADO COM SUCESSO',nome_slow)
    #mv = shutil.move(nome_slow, './Slow')
    #rm = os.unlink(slow)
    #print('move SLOW com sucesso')
    #print('remove SLOW com sucesso')


    else:
        print('PROBLEMAS COM SLOW MOTION')
    return nome_slow

def concatena_slow (video_audio, video_slow):
    print("--------VAMOS CONCATENAR O VIDEO SEM AUDIO COM SLOW MOTION--------")
    print("--------VIDEO SEM AUDIO RECEBIDO",video_audio)
    print("--------VIDEO ORIGINAL RECEBIDO",video_slow)
    video_intro="/home/pi/app/flask-celery/static/videos/fechamento.avi"
    nome_concatena=geraNome()
    print(video_intro)
    concatenar = [

        "ffmpeg",
        "-i",
        video_audio,
        "-i",
        video_slow,
        "-i",
        video_intro,
        "-filter_complex",
        "[0:v] [1:v] [2:v] concat=n=3:v=1 [v]",
        "-map","[v]",
        nome_concatena
    ]
    print(concatenar)
    print('----------------APLICANDO PARA CONCATENAR VIDEO SEM AUDO COM SLOW MOTION------------------')
    concat_video = subprocess.Popen(concatenar,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
    saida_concat = concat_video.wait()
    if saida_concat == 0:
        print('VIDEOS CONCATENADO COM SUCESSO',nome_concatena)
        rm = os.unlink(video_audio)
        rm = os.unlink(video_slow)

        mv = shutil.move(nome_concatena, './Reproduzir')
        print('move com sucesso')
    else:
        print('PROBLEMAS AO CONCATENAR VIDEOS')
    return nome_concatena

def time_line_finaliza_video(verifica_video):
    print ('---------INICIANDO A VERIFICAÇÃO E EDIÇÃO DE VIDEOS---------')
    #pdb.set_trace()
    verifica_video = verifica_video

    if verifica_video == 1:
        nome_concatena=geraNome()
        print ('----------------Verificando se existem VIDEOS na pasta-----------------')
        lista_videos = glob.glob('./tmp/video_extraido/*.avi')
        lista_imagens = glob.glob('./static/images/*.png')
        if len(lista_imagens) > 0:
            imagem_abertura = lista_imagens[0]
            imagem_propaganda = lista_imagens[1]
        else:
            print('Não existe imagem para concatenar no video')

        print(lista_videos)
        if len(lista_videos) > 0:
            print('Lista de videos na pasta',lista_videos)



            for i in range(len(lista_videos)):
                print('Lista de videos',lista_videos[i])
                video_normal=lista_videos[i]
                video_slow=lista_videos[i]
                cmd=["./FinalizaVideo.sh",imagem_abertura,imagem_propaganda,video_normal,video_slow]
                #p = subprocess.Popen(cmd)
                print(cmd)
                a = subprocess.Popen(cmd,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
                print(a.stdout)
                a.wait()


            print('----------------APLICANDO PARA CONCATENAR VIDEO SEM AUDO COM SLOW MOTION------------------')

        else:
            print('não existe arquivo .avi na pasta')
    else:
        if verifica_video == 2:
            roda = False
            print('saindo')
            #break
            exit(1)
    return 'time line de video gerada'