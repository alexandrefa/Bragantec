import mraa	# Controles de I/O
import time	# Funcoes de  tempo

led = mraa.Gpio(23)	# Declarando a variavel 'led' como um pino da placa
led.dir(mraa.DIR_OUT)	# Declarando que o 'led' sera uma saida

while True:	# Executa indefinidamente o codigo

	led.write(1)	# Liga o led
	time.sleep(0.2)	# Aguarda 200ms 
	led.write(0)	# Desliga o led
	time.sleep(0.2)	# Aguarda 200ms
