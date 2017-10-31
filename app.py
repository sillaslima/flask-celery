import json
import os
import subprocess
import random
import time
import datetime
import pdb
from flask import Flask,render_template, request,make_response, jsonify
#from flask_sqlalchemy import SQLAlchemy
#from numpy.core.records import record

#from cronometro import comecar, consultaCronometro, finaliza_cronometro
from cronometro import gravar, para_gravacao, gera_momento


from datetime import timedelta

app = Flask(__name__)
content_type_json = {'Content-Type': 'text/css; charset=utf-8'}

from celery import Celery

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
app.config['CELERY_TIMEZONE'] = 'UTC'

###------------###
#Agendar tarefas/tasks com o celery

# from celery.schedules import crontab
# app.config['CELERYBEAT_SCHEDULE'] = {
#     'play-every-morning': {
#         'task': 'tasks.play_task',
#         'schedule': crontab(hour=9, minute=10)
#     },
#     'pause-later': {
#         'task': 'tasks.pause_task',
#         'schedule': crontab(hour=9, minute=10)
#     }
# }

###------------###
# Initialize Celery

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

####
#Escrita de arquivo
####


@celery.task
def vai_record():
    print('gravando o jogo')
    return gravar()

@celery.task
def finalizar():
    print('finalizando o jogo')
    return para_gravacao()


@celery.task
def captura_momento():
    print('capturando melhor momento')
    return gera_momento()
@app.route('/')
def index():
    #msg = 'Opções: <a href="/record">Inciar Gravação</a> or <a href="/finalizar">Finalizar Gravação</a> or <a href="/capturar">Gera Momento Gravação</a>'
    #return msg
    return render_template('index.html')


@app.route('/finalizar', methods=['GET','POST'])
def fimCrono():
    finalizar.delay()
    html = '<a href="/">voltar</a>'
    return html
    #return jsonify({'status':'Fim Jogo'}), 200

@app.route('/record', methods=['GET','POST'])
def start_record():
    vai_record.delay()
    #a = gravar.out
    #print(a)

    html = '<a href="/">voltar</a>'
    return html

@app.route('/capturar', methods=['GET','POST'])
def captura():
    captura_momento.delay()
    #a = gravar.out
    #print(a)

    html = '<a href="/">voltar</a>'
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
