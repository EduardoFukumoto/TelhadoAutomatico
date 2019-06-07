# PROJETO FINAL
import Adafruit_BBIO.ADC as ADC #Acionando biblioteca para fazer leitura de tensao
import Adafruit_BBIO.GPIO as GPIO #Acionando biblioteca para controle do LED e botoes
import Adafruit_BBIO.PWM as PWM #Acionando biblioteca para controle do motor
import time #biblioteca para realizar sleep (diminuir a velocidade com que o loop roda)
from time import sleep

a = 0 #Variavel a e b sao para diferenciar os modos em que o programa esta funcionando - Automatico ou manual
b = 0
loop = 1 #Definir loop

sensor_pin = "P9_40"  # sensor
servoPin = "P9_14"  # Motor
automaticoButton = "P9_11"  # botao automatico
Button1 = "P9_13"  # botao manual
Button2 = "P9_24" # botao para fechar
pin_light1 = "P9_12" # pino para acender luzes

PWM.start(servoPin, 5, 50)  # Inicia o motor
ADC.setup()  # Inicia sensor de luz
GPIO.setup(automaticoButton, GPIO.IN)  # inicia botao automatico - GPIO recebe tensao do botao
GPIO.setup(Button1, GPIO.IN)  # inicia botao manual 1  - GPIO recebe tensao do botao
GPIO.setup(Button2, GPIO.IN)  # inicia o botao manual 2 - GPIO recebe tensao do botao
GPIO.setup(pin_light1, GPIO.OUT)  # inicia o LED - GPIO envia tensão ao LED

print('sensor\tvolts\tangulo\tCiclo') #inicio do print, para verificar movimentacao do motor e leitura do sensor de luz
while loop == 1:

    # RECEBER VALORES DOS BOTOES

    sleep(0.1)

    if GPIO.input(automaticoButton): #caso o botao seja pressionado, dois valores sao atribuidos a variaveis
        print
        "automatico button pushed"
        a = 1 # a=1 significa que o motor esta se movendo de acordo com a leitura do sensor de luz
        b = 0 # b=0 nao tem funcao quando a=1
        sleep(1) #impede que sejam feitas varias leituras apertando o botao somente uma vez

    if GPIO.input(Button1): #transforma o sistema em sistema manual
        print
        "Button 1 pushed"
        a = 0 # a=0 significa que o sistema esta manual
        b = 1 # b=1 significa que o motor ira rotacionar um pouco, cada vez que ele for pressionado
        sleep(1)#impede que sejam feitas varias leituras apertando o botao somente uma vez

    if GPIO.input(Button2):
        print
        "Button 2 pushed"
        a = 0 # a=0 significa que o sistema esta manual
        b = 0 # b=1 significa que o motor ira rotacionar um pouco, cada vez que ele for pressionado
        sleep(1)#impede que sejam feitas varias leituras apertando o botao somente uma vez

    reading = ADC.read(sensor_pin)  # comando para realizar leitura no sensor
    volts = reading * 1.800  # volts sensor - essa conversao pode facilitar o trabalho, mas nao eh obrigatoria
    # a tensao do sensor varia de 0V, sendo 0V pouquíssima luz a 1.8V (maximo da porta ADC), sendo 1.8V quando o sensor recebe muita luz
    
    # controle de luz
    if volts >= 0.3: #Quando temos muita luz, o LED conectado desliga
        GPIO.output(pin_light1, GPIO.LOW) #esse comando desativa o LED, faz com que a porta gere baixa tensao
    if volts < 0.18: #Quando temos pouca luz, o LED conectado liga
        GPIO.output(pin_light1, GPIO.HIGH) #esse comando ativa o LED, faz com que a porta gere alta tensao

    # BLOCO 1 MOTOR AUTOMATICO

    if a == 1: #Quando o botao automatico eh pressionado, o programa realiza essa parte

        if volts >= 0.8 and volts <= 1.8:  # Muuuita LUZ
            desiredAngle = 15 #Com uma quantidade de luz alta, o teto se abre pela metade, diminuindo a entrada de luz que pode ser incomoda.

        if volts >= 0.3 and volts < 0.7:  # Luz OK
            desiredAngle = 40 #Com uma quantidade de luz media, o teto se abre por completo.

        if volts >= 0.01 and volts < 0.25:  # Sem Luz - Noite
            desiredAngle = 0

        dutyCycle = 1. / 18. * desiredAngle + 3  # Transformar angulo em ciclo. Eh colocado um . para que os numeros sejam lidos como float.
        #o valor 1. foi encontrado da seguinte maneira: para dutyCycle0 = 3, nosso motor fica em 0graus e para dutyCycle180 = 13 ele atinge 180graus
        #Entao temos que dutyCycle = (dutyCycle180 - dutyCycle0)/180 * angulo + dutyCycle0 
        #Esses valores sao diferentes para cada motor
        
        PWM.set_duty_cycle(servoPin, dutyCycle) # Coloca o motor na posicao desejada

   # BLOCO 2 PROGRAMA MANUAL (REGULAR COM BOTAO)

    if a == 0:

        if b == 0: #Botao2 sendo pressionado
            desiredAngle = 0
        if b == 1: #Botao1 sendo pressionado
            desiredAngle = desiredAngle + 10 #Aumento gradativo do angulo
            if desiredAngle > 40: #Se o angulo atingir 40graus, que eh o limite no nosso projeto, o teto se fecha e retorna a posicao inicial
                desiredAngle = 0

        dutyCycle = 1. / 18. * desiredAngle + 3  # Transformar angulo em ciclo, nosso servo atua entre dutyCycle = 3 a dutyCycle = 13
        PWM.set_duty_cycle(servoPin, dutyCycle) # Coloca o motor na posicao desejada

    print('%f\t%f\t%f\t%f' % (reading, volts, desiredAngle, dutyCycle)) #print para verificar o que esta acontecendo com os valores no programa
    #Eh muito interessante colocar isso para analisar o que ocorre dentro do programa.
