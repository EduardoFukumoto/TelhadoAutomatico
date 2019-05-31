#TESTE SENSOR DE LUZ

import Adafruit_BBIO.ADC as ADC #Acionando biblioteca para fazer leitura de tensao
import time

sensor_pin = 'P9_40'

ADC.setup()

print('Reading\t\tVolts')

while True:
    reading = ADC.read(sensor_pin)
    volts = reading * 1.800
    print('%f\t%f' % (reading, volts))
    time.sleep(1)