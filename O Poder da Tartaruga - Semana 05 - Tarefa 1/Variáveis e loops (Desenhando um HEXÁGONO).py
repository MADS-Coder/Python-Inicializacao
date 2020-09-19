#Variáveis e loops
#Desenhando um HEXÁGONO

from turtle import *
speed(2)
shape("turtle")

lados = 6
angulo = 360 / lados

for count in range(lados):
    forward(108)
    left(angulo)


done()
