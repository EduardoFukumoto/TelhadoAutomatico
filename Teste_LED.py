#TESTE LED

import Adafruit_BBIO.GPIO as GPIO #Acionando biblioteca para controle do LED e botões

pin_light1 = 'P9_12'
pin_light2 = 'P9_15'

GPIO.setup(pin_light1, GPIO.OUT)
GPIO.setup(pin_light2, GPIO.OUT)

from time import sleep

for i in range(0, 5):
    GPIO.output(pin_light1, GPIO.HIGH)
    sleep(1)
    GPIO.output(pin_light1, GPIO.LOW)
    sleep(1)

GPIO.cleanup()
