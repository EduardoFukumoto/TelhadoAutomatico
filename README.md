#  Telhado Automatico feito em BeagleBone Black (Python)
**Integrantes do grupo:**\
  Eduardo Akira Fukumoto\
  Carolina Bergamaschi\
  Caio de Oliveira Martins\
  Heloise Mantovani
  
## 1- Introdução
O projeto que será descrito nesse relatório consiste em um protótipo inicial de um sistema de automação residencial, mais especificamente controle de um telhado automático conforme leitura em sensor de luminosidade(LDR).\
Sistema de malha fechada processado pela Beaglebone Black, programado em Python com auxílio da biblioteca Adafruit.
### 1.1 - Bibliotecas usadas em Python
Foi utilizada a biblioteca Adafruit para utilizar as portas GPIO (para realizar o controle dos LEDs e receber inputs dos botões), PWM(realizar o controle do motor) e ADC(medir a tensão no sensor de luminosidade LDR)\
É necessário ter a biblioteca Adafruit para realizar o tutorial abaixo, ela já está presente no sistema operacional mais atualizado do Debian, que pode ser instalada na BeagleBone Black ou que já vem embutida nas placas mais novas. Caso não tenha essa biblioteca será necessário instalar ela.\
[Tutorial para iniciar a usar a sua beaglebone](https://beagleboard.org/getting-started/)

### 1.2 - Acessando a placa
Existem várias maneiras de acessar a placa BeagleBone, realizando a conexão ssh. Caso você utilize o Linux, pode acessar a placa utilizando o terminal e utilizar o seguinte comando:\
**ssh root@192.168.7.2**

Outra maneira é baixar o Putty, podendo realizar o acesso com o sistema operacional windows.\
[Como fazer ssh pelo Putty](https://www.secnet.com.br/blog/ssh-com-putty/)

Outra maneira ainda, é acessar a IDE cloud9 que já vem na placa, somente digitando em um navegador o seguinte link:\
**192.168.7.2:3000**
## 2- Componentes utilizados no Projeto

### 2.1- Servomotor
O modelo utilizado foi o servomotor MG995 como na imagem a seguir:\
[Imagem do motor]()

#### 2.1.1 - Parte elétrica
Fio amarelo do motor: Fio de controle\
Fio vermelho do motor: Vcc/Tensão de alimentação\
Fio preto/marrom do motor: GND/Ground/Terra

Para mais dados sobre alimentação do motor consultar datasheet no próximo tópico. Mesmo que a placa tenha alimentação de 5V, que pode ser necessário para o motor, é aconselhável usar uma fonte externa.

O controle do movimento do motor é feito pela variação da tensão no pino de controle (amarelo) então para isso ser possível e no caso de uso da Beaglebone temos que fazer a conexão em algum pino de controle PWM (Pulse Width Modulation).

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
...
import Adafruit_BBIO.PWM as PWM #Acionando biblioteca para controle do motor
servoPin = "P9_14"

PWM.start(servoPin, 5, 50)

while(1):
    desiredAngle=input("Qual angulo?")
    dutyCycle = 1./18.*desiredAngle + 3
    PWM.set_duty_cycle(servoPin, dutyCycle)
...

### 2.2- Sensor de luz LDR
#### 2.2.1 - Parte elétrica
#### 2.2.2 - Programa teste
### 2.3- Botão
#### 2.3.1 - Parte elétrica
#### 2.3.2 - Programa teste
### 2.4- LED
#### 2.4.1 - Parte elétrica
#### 2.4.2 - Programa teste

## 3- O Projeto
### 3.1- Conexão dos componentes na placa
### 3.2- Código do projeto
