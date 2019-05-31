#TESTE BOTAO

import Adafruit_BBIO.GPIO as GPIO #Acionando biblioteca para controle do LED e botões
from time import sleep

topButton = "P9_24"
bottomButton = "P9_13"
a = 0
b = 0

GPIO.setup(topButton, GPIO.IN)
GPIO.setup(bottomButton, GPIO.IN)

while (1):
    if GPIO.input(topButton):
        print
        "Botao1 Pressionado"
        a = 1
        b = 0

    if GPIO.input(bottomButton):
        print
        "Botao2 pressionado"
        b = 1
        a = 0

    if GPIO.input(bottomButton) and GPIO.input(topButton):
        break

    sleep(.2)

    print("a/t", a, "b", b)

GPIO.cleanup()
