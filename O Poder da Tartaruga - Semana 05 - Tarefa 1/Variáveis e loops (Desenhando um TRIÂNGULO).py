#Variáveis e loops
#Desenhando um TRIÂNGULO

from turtle import *
speed(2)
shape("turtle")

lados = 3
angulo = 360 / lados

for count in range(lados):
    forward(108)
    left(angulo)


done()
