import json
import os
import subprocess
import random
import time
import datetime
import pdb
from flask import Flask, request,make_response, jsonify
#from flask_sqlalchemy import SQLAlchemy
#from numpy.core.records import record

from cronometro import comecar, consultaCronometro, finaliza_cronometro
from cronometro import gravar, para_gravacao


from datetime import timedelta

app = Flask(__name__)
content_type_json = {'Content-Type': 'text/css; charset=utf-8'}

from celery import Celery

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
app.config['CELERY_TIMEZONE'] = 'UTC'

from celery.schedules import crontab
app.config['CELERYBEAT_SCHEDULE'] = {
    'play-every-morning': {
        'task': 'tasks.play_task',
        'schedule': crontab(hour=9, minute=10)
    },
    'pause-later': {
        'task': 'tasks.pause_task',
        'schedule': crontab(hour=9, minute=10)
    }
}

# Initialize Celery

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

####
#Escrita de arquivo
####
@celery.task
def start():
    print('iniciando o jogo')
    return comecar()

@celery.task
def consultar():
    print('consultando o tempo do jogo')
    #tempo = consultaCronometro()

    return 'tempo'

@celery.task
def finalizar():
    print('finalizando o jogo')
    return para_gravacao()

@celery.task
def vai_record():
    print('gravando o jogo')
    return gravar()

@app.route('/')
def index():
    msg = 'Opções: <a href="/start">Start</a> or <a href="/consultar">consultar</a>.' \
          'or <a href="/finalizar">finalizar</a> or <a href="/record">record</a>'
    return msg

@app.route('/start', methods=['GET','POST'])
def startCrono():
    start.delay()
    html = '<a href="/">voltar</a>'
    return html
        #, Response(jsonify({'status':'Em Andamento'}))


@app.route('/consultar', methods=['GET','POST'])
def consultarCrono():
    task = consultar.delay()
    #pdb.set_trace()
    print(task.id)
    print(task.backend)
    print(dir(task))

    #task = consultar.AsyncResult(task_id)
    tempo = consultaCronometro()

    response = {
            'estadoAtual': task.state,
            'id': str(task.id),
            'successful': str(task.backend),
            'status': str(task.status),
            'tempoAtual' : tempo,
            'resultado' : str(task.result)

        }
    return jsonify(response)

@app.route('/finalizar', methods=['GET','POST'])
def fimCrono():
    finalizar.delay()
    return jsonify({'status':'Fim Jogo'}), 200

@app.route('/record', methods=['GET','POST'])
def start_record():
    vai_record.delay()
    #a = gravar.out
    #print(a)
    tempo = consultaCronometro()
    return jsonify({'gravando':tempo}), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
