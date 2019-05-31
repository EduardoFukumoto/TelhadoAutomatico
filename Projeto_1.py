#  TESTE COM O SENSOR DE LUZ + MOTOR

import Adafruit_BBIO.ADC as ADC #Acionando biblioteca para fazer leitura de tensao
import Adafruit_BBIO.PWM as PWM #Acionando biblioteca para controle do motor
import time

sensor_pin = P9_40  # sensor
servoPin = P9_14  # Motor
a = 0

PWM.start(servoPin, 5, 50)  # Inicia o motor
ADC.setup()  # Inicia sensor de luz

print('sensortvoltstangulotCiclo')

while a != 1

    reading = ADC.read(sensor_pin)  # Leitura sensor
    volts = reading
    1.800  # volts sensor

    if volts = 1.5 and volts = 1.8  # Muuuita LUZ
    desiredAngle = 2

if volts = 0.7 and volts  1.5  # Luz OK
desiredAngle = 40

if volts = 0 and volts  0.7  # Sem Luz - Noite
desiredAngle = 85

dutyCycle = 1.18.desiredAngle + 3  # Transformar angulo em ciclo, nosso servo atua entre 3 a 13
PWM.set_duty_cycle(servoPin, dutyCycle)  # Coloca a posição do motor

print('%ft%ft%ft%f' % (reading, volts, desiredAngle, dutyCycle))
time.sleep(1)

