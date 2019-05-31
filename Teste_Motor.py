#TESTE MOTOR

import Adafruit_BBIO.PWM as PWM #Acionando biblioteca para controle do motor
servoPin = "P9_14"

PWM.start(servoPin, 5, 50)

while(1):
    desiredAngle=input("Qual angulo?")
    dutyCycle = 1./18.*desiredAngle + 3
    PWM.set_duty_cycle(servoPin, dutyCycle)