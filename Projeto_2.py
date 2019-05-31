# PROJETO FINAL

import Adafruit_BBIO.ADC as ADC #Acionando biblioteca para fazer leitura de tensao
import Adafruit_BBIO.GPIO as GPIO #Acionando biblioteca para controle do LED e botões
import Adafruit_BBIO.PWM as PWM #Acionando biblioteca para controle do motor
import time
from time import sleep

a = 0
b = 0
loop = 1

sensor_pin = "P9_40"  # sensor
servoPin = "P9_14"  # Motor
automaticoButton = "P9_11"  # botao automatico
Button1 = "P9_13"  # botao manual
Button2 = "P9_24"
pin_light1 = "P9_12"

PWM.start(servoPin, 5, 50)  # Inicia o motor
ADC.setup()  # Inicia sensor de luz
GPIO.setup(automaticoButton, GPIO.IN)  # inicia botao automatico
GPIO.setup(Button1, GPIO.IN)  # inicia botao manual 1
GPIO.setup(Button2, GPIO.IN)  # inicia o botao manual 2
GPIO.setup(pin_light1, GPIO.OUT)  # inicia o LED

print('sensor\tvolts\tangulo\tCiclo')
while loop == 1:

    # RECEBER VALORES DOS BOTOES

    sleep(0.1)

    if GPIO.input(automaticoButton):
        print
        "automatico button pushed"
        a = 1
        b = 0
        sleep(1)

    if GPIO.input(Button1):
        print
        "Button 1 pushed"
        a = 0
        b = 1
        sleep(1)

    if GPIO.input(Button2):
        print
        "Button 2 pushed"
        a = 0
        b = 0
        sleep(1)

    if GPIO.input(Button1) and GPIO.input(Button2):
        break

    reading = ADC.read(sensor_pin)  # Leitura sensor
    volts = reading * 1.800  # volts sensor

    # controle de luz

    if volts >= 0.3:
        GPIO.output(pin_light1, GPIO.LOW)
    if volts < 0.18:
        GPIO.output(pin_light1, GPIO.HIGH)

    # BLOCO 1 MOTOR AUTOMATICO

    if a == 1:

        if volts >= 0.8 and volts <= 1.8:  # Muuuita LUZ
            desiredAngle = 15

        if volts >= 0.3 and volts < 0.7:  # Luz OK
            desiredAngle = 40

        if volts >= 0.01 and volts < 0.25:  # Sem Luz - Noite
            desiredAngle = 0

        dutyCycle = 1. / 18. * desiredAngle + 3  # Transformar angulo em ciclo, nosso servo atua entre 3 a 13
        PWM.set_duty_cycle(servoPin, dutyCycle)

        # BLOCO 2 PROGRAMA MANUAL (REGULAR COM BOTAO)

    if a == 0:

        if b == 0:
            desiredAngle = 0
        if b == 1:
            desiredAngle = desiredAngle + 10
            b = 2
            if desiredAngle > 40:
                desiredAngle = 0

        dutyCycle = 1. / 18. * desiredAngle + 3  # Transformar angulo em ciclo, nosso servo atua entre 3 a 13
        PWM.set_duty_cycle(servoPin, dutyCycle)

    print('%f\t%f\t%f\t%f' % (reading, volts, desiredAngle, dutyCycle))
