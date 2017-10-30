import os
import subprocess
import datetime
import time
import signal
import pdb
# def comecar():
#     with open('pidfile.txt', 'w') as f:
#         print(os.getpid(), file=f)
#         # print(str(tempo_atual), file=f, end='\n')
#     i = 0
#     while True:
#         time.sleep(1)
#         i += 1
#         tempo_atual = datetime.timedelta(seconds=i)
#         print('0' + str(tempo_atual), end='\n')
#
#         with open('cronometro.txt', 'w') as crono:
#             print('0' + str(tempo_atual), file=crono, end='\n')
#     return 'foi'


# def consultaCronometro():
#     with open('cronometro.txt','rt') as f:
#         linhas = f.readlines()
#         #print(linhas)
#         f.close()
#         ultimo_tempo = linhas[len(linhas) -1]
#         print(ultimo_tempo)
#     return ultimo_tempo
# #consultaCronometro()


# # def finaliza_cronometro():
# #
# #     if os.path.exists('pidfile.txt'):
# #         print(type(os.path.exists('pidfile.txt')))
# #         print(os.getpid())
# #         with open('pidfile.txt','rt') as f:
# #             x = f.read()
# #             print(x)
# #             print(type(x))
# #             os.kill(int(x),signal.SIGTERM)
#
#
#     else:
#         print('Cronometro Não Iniciado')
#         raise SystemExit(1)


def gravar():
    #pdb.set_trace()
    cmd = ["./start.sh"]
    print(os.getpid())
    #cmd = ["touch test1.txt"]
    p = subprocess.Popen(cmd)
    #print(p.communicate()[0])
    return 'gravando'


def gera_momento():
    cmd = ["./hourconverter.sh", "captura"]
    p = subprocess.Popen(cmd)

    return "gera video melhor momento"


def para_gravacao():
    cmd = ["./stop.sh"]
    #print(os.getpid())
    #cmd = ["ls", "-l" "&"]
    p = subprocess.Popen(cmd)

    return "Parou a gravação"
#gravar()

