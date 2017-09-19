#Declaracao das bibliotecas

import os	# Funcoes de sistema
import mraa	# Controles de I/O
import time	# Funcoes de  tempo


sensor = mraa.Gpio(27)	# Declarando a variavel 'sensor' como um pino da placa
sensor.dir(mraa.DIR_IN)	# Declarando que o 'sensor' sera um entrada


while True:	# Executa os codigos abaixo indefinidamente

	porta_status = sensor.read()	# Le o status do 'sensor' e guarda em outra variavel 'porta status' 
	
	if porta_status == 0:	# Vefifica se a porta esta aberta ou fechada e emite mensagem correspondente
		print ("A porta esta fechada / Sensor = ") + str(porta_status)
	else:
		print ("A porta esta aberta / Sensor = ") + str(porta_status)


	caminho = 'sudo ThingSpeakC/./ThingSpeakC GGL8TAYS0PQISG3Y ' + str(porta_status)	# Caminho para enviar os dados
	os.system(caminho) # Envia os dados via sistema
	time.sleep(20)	# Aguarda 20 segundos
	
