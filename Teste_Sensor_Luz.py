#TESTE SENSOR DE LUZ E ACIONAMENTO DE LED

import Adafruit_BBIO.ADC as ADC #Acionando biblioteca para fazer leitura de tensao
import time
import Adafruit_BBIO.GPIO as GPIO #Acionando biblioteca para controle do LED e botões

sensor_pin = 'P9_40'
pin_light1 = 'P9_12'

GPIO.setup(pin_light1, GPIO.OUT)

ADC.setup()

print('Reading\t\tVolts')

while True:
    reading = ADC.read(sensor_pin)
    volts = reading * 1.800
    print('%f\t%f' % (reading, volts))
    time.sleep(1)

    if volts >= 1.0:
        GPIO.output(pin_light1, GPIO.LOW)
    if volts < 1.0:
        GPIO.output(pin_light1, GPIO.HIGH)
