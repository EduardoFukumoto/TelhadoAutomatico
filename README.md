#  Telhado Automatico feito em BeagleBone Black (Python)
**Integrantes do grupo:**\
  Eduardo Akira Fukumoto\
  Carolina Bergamaschi\
  Caio de Oliveira Martins\
  Heloise Mantovani
  
## 1- Introdução
O projeto que será descrito nesse relatório consiste em um protótipo inicial de um sistema de automação residencial, mais especificamente controle de um telhado automático conforme leitura em sensor de luminosidade(LDR).\
Sistema de malha fechada processado pela Beaglebone Black, programado em Python com auxílio da biblioteca Adafruit.\
Primeiramente iremos mostrar como utilizar cada componente do projeto de forma separada. Depois disso, iremos juntar todos os componentes, mostrar as conexões feitas com a placa e o código.
### 1.1 - Bibliotecas usadas em Python
Foi utilizada a biblioteca Adafruit para utilizar as portas GPIO (para realizar o controle dos LEDs e receber inputs dos botões), PWM(realizar o controle do motor) e ADC(medir a tensão no sensor de luminosidade LDR).\
É necessário ter a biblioteca Adafruit para realizar o tutorial abaixo, ela já está presente no sistema operacional mais atualizado do Debian, que pode ser instalada na BeagleBone Black ou que já vem embutida nas placas mais novas. Caso não tenha essa biblioteca será necessário instalar ela.\
[Tutorial - Iniciar a usar a sua beaglebone](https://beagleboard.org/getting-started/)

### 1.2 - Acessando a placa
Existem várias maneiras de acessar a placa BeagleBone, realizando a conexão ssh. Caso você utilize o Linux, pode acessar a placa utilizando o terminal e utilizar o seguinte comando:\
**ssh root@192.168.7.2**

Outra maneira é baixar o Putty, podendo realizar o acesso com o sistema operacional windows:\
[Tutorial - Como fazer ssh pelo Putty](https://www.secnet.com.br/blog/ssh-com-putty/)

Outra maneira ainda, é acessar a IDE cloud9 que já vem na placa, somente digitando em um navegador o seguinte link:\
**192.168.7.2:3000**

### 1.3 - Datasheet placa

<img src = "http://www.toptechboy.com/wp-content/uploads/2015/06/beaglebone-black-pinout.jpg">
fonte: http://www.toptechboy.com/beaglevone-black-rev-c/beaglebone-black-lesson-1-understanding-beaglebone-black-pinout/attachment/beaglebone-black-pinout/

## 2- Componentes utilizados no Projeto

### 2.1- Servomotor
O modelo utilizado foi o servomotor MG995 como na imagem a seguir:\
![Imagem do motor]()

#### 2.1.1 - Parte elétrica
Fio amarelo do motor: Fio de controle;\
Fio vermelho do motor: Vcc/Tensão de alimentação;\
Fio preto/marrom do motor: GND/Ground/Terra.

Para mais dados sobre alimentação do motor consultar datasheet no próximo tópico. Mesmo que a placa tenha alimentação de 5V, que pode ser necessário para o motor, é aconselhável usar uma fonte externa.\
É aconselhável colocar um resistor em série entre a porta de controle da placa e o motor, no caso é usado de 10kohm.

O controle do movimento do motor é feito pela variação da tensão no pino de controle (amarelo) então para isso ser possível e no caso de uso da Beaglebone temos que fazer a conexão em algum pino de controle PWM (Pulse Width Modulation).

<img src = "https://cdn-learn.adafruit.com/assets/assets/000/010/760/original/beaglebone_fritzing_big_servo.png?1378201406" height = "300" width = "350">
fonte: https://learn.adafruit.com/
**OBS: Pode conectar o controle do motor na placa em GPIO também, mas para isso o código é alterado. Pode-se seguir a imagem, mas conectar o controle do motor em P9_14 - PWM**

#### 2.1.2 - Parte mecanica

| Descrição               | MG 995R TowerPro  |
|-------------------------|-------------------|
| Tensão de Alimentação   | 4,8 - 7,2V        |
| Corrente de Operação    | 500mA - 900mA     |
| Corrente Stall          | 2,5A              |
| Temperatura de Operação | 0 ~ 55ºC          |
| Comprimento do cabo     | 24,5cm            |
| Velocidade              | 0,16 seg/60º (6V) |
| Torque a 4.8V           | 9,4 kg-cm         |
| Torque a 6V             | 11 kg-cm          |
| Dimensões               | 40.7x19.7x42.9mm  |
| Peso                    | 55g               | 

#### 2.1.3 - Programa teste
```
import Adafruit_BBIO.PWM as PWM #Acionando biblioteca para controle do motor
servoPin = "P9_14"

PWM.start(servoPin, 5, 50)

while(1):
    desiredAngle=input("Qual angulo?")
    dutyCycle = 1./18.*desiredAngle + 3
    PWM.set_duty_cycle(servoPin, dutyCycle)
```
### 2.2- Sensor de luz LDR
Um resistor dependente de luz ou LDR (Light Dependent Resistor), é um componente eletrônico passivo do tipo resistor variável, mais especificamente, é um resistor cuja resistência varia conforme a intensidade da luz que incide sobre ele. Quanto mais luz menor a resistência do LDR, quando mais escuro maior é a resistência. 

O LDR deve ser conectado a uma entrada analógica para a Beaglebone seja capaz de receber os dados providos pelo sensor, mais detalhes a frente.

<img src = "https://cdn.awsli.com.br/600x700/468/468162/produto/19414320/sensor-fotoresistor-ldr-de-5mm-6344c5f4.jpg" height = "300" width = "350">

#### 2.2.1 - Parte elétrica
Resistor de 10Kohm para realizar uma divisão de tensão. Isso é necessário para que a queda de tensão do sensor de luz varie entre 0 e 1.8V, a faixa de valor que a porta da placa BeagleBoard consegue fazer a leitura.

<img src = "https://cdn-learn.adafruit.com/assets/assets/000/009/320/original/beaglebone_fritzing.png?1396887528" height = "300" width = "380">
Fonte: https://learn.adafruit.com/measuring-light-with-a-beaglebone-black/

#### 2.2.2 - Programa teste

```
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
```
### 2.3- Botão

<img src = "https://cdn.awsli.com.br/600x700/78/78150/produto/3890423/1f95cf6a89.jpg" height = "300" width = "350">

#### 2.3.1 - Parte elétrica

<img src = "http://www.toptechboy.com/wp-content/uploads/2015/06/button-beaglebone-black.jpg" height = "300" width = "350">
Fonte:http://www.toptechboy.com/beaglevone-black-rev-c/beaglebone-lesson-8-digital-input-from-gpio-pins-in-python/
**OBS: a imagem dos resistores está incorreta, é para usar resistores de 1kOhm**

#### 2.3.2 - Programa teste

```
import Adafruit_BBIO.GPIO as GPIO #Acionando biblioteca para controle do LED e botões
from time import sleep

topButton = "P9_24"
bottomButton = "P9_13"

GPIO.setup(topButton, GPIO.IN)
GPIO.setup(bottomButton, GPIO.IN)

while (1):
    if GPIO.input(topButton):
        print
        "Botao1 Pressionado"

    if GPIO.input(bottomButton):
        print
        "Botao2 pressionado"

    if GPIO.input(bottomButton) and GPIO.input(topButton):
        break

    sleep(.2)
    print("a/t", a, "b", b)
GPIO.cleanup()
```

### 2.4- LED
Importante relembrar que o LED possui um lado certo que cada fio deve ser conectado. Pode-se encontrar qual a maneira correta de fazer a ligação olhando dentro do LED (a marcação do retângulo interno) ou qual lado do seu cabo é mais curto e longo.
<img src = "https://hackster.imgix.net/uploads/attachments/446767/led_AOuhtzYEQe.png?auto=compress%2Cformat&w=600&h=450&fit=min" height = "300" width = "350">

#### 2.4.1 - Parte elétrica

<img src = "http://www.toptechboy.com/wp-content/uploads/2015/06/LED-Beaglebone-Circuit.jpg" height = "300" width = "350">
Fonte:http://www.toptechboy.com/beaglevone-black-rev-c/beaglebone-black-lesson-5-blinking-leds-from-gpio-pins/

#### 2.4.2 - Programa teste

```
import Adafruit_BBIO.GPIO as GPIO #Acionando biblioteca para controle do LED
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
```

## 3- O Projeto
O projeto pode ser visto em funcionamento através desse link:
[![Watch the video](https://img.youtube.com/vi/T-Yk8eOxkoNCM/maxresdefault.jpg)](https://youtu.be/T-Yk8eOxkoNCM)



### 3.1- Conexão dos componentes na placa


### 3.2- Código do projeto

```
# PROJETO FINAL

#Esses sao os codigos comentados de um programa que realiza o controle de um prototipo de um telhado residencial para controlar a luminosidade
#interna da casa, controlando a partir de um sensor de luminosidade a abertura de um teto, a partir de um servo motor e o acionamento de
#luz, representada no caso por LED.

#Junto com esse documento esta disponibilizado um documento WORD com alguns tutoriais na internet - esses tutoriais mostram o funcionamento
#de cada um dos componentes utilizados nesse projeto, porem de forma separada. Alem disso, no documento Word estara registrado como sao feitas
#as ligacoes na protoboard, com os respectivos resistores para proteçao da placa e divisao de tensao, e como realizar as ligacoes nos pinos da
#placa. 
#Um video tambem sera disponibilizado para mostrar o projeto final em funcionamento.

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
    ```
