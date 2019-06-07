#  Telhado Automatico feito em BeagleBone Black (Python)
**Integrantes do grupo:\\**
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
**ssh root@192.168.7.2**\
Outra maneira é baixar o Putty, podendo realizar o acesso com o sistema operacional windows.\
[Como fazer ssh pelo Putty](https://www.secnet.com.br/blog/ssh-com-putty/)\
Outra maneira ainda, é acessar a IDE cloud9 que já vem na placa, somente digitando em um navegador o seguinte link:\
**192.168.7.2:3000**
![alt text](https://raw.githubusercontent.com/username/projectname/branch/path/to/img.png)
## 2- Componentes utilizados no Projeto

### 2.1- Servomotor
#### 2.1.1 - Parte elétrica (explicar as portas e o funcionamento de cada coisa)
#### 2.1.2 - Parte mecanica (data sheet)
#### 2.1.3 - Programa teste (Explicar como o programa teste funciona)
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
