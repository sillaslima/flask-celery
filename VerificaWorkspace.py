#-*- coding: utf-8 -*-
import os

#os.mkdir('tmp2')

def verifica_ws():

	print (os.getcwd())

	if os.path.exists('Audio'):
		print('existe a pasta Audio')
	else:
		print('não existe a pasta Audio')
		print('Criando a pasta Audio')
		os.makedirs('Audio')

	if os.path.exists('Slow'):
		print('existe a pasta Slow')
	else:
		print('não existe a pasta Slow')
		print('Criando a pasta Slow')
		os.makedirs('Slow')

	if os.path.exists('Reproduzir'):
		print('existe a pasta Reproduzir')
	else:
		print('não existe a pasta Reproduzir')
		print('Criando a pasta Reproduzir')
		os.makedirs('Reproduzir')
