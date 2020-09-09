#Variáveis e loops
#Desenhando um QUADRADO

from turtle import *
speed(2)
shape("turtle")

lados = 4
angulo = 360 / lados

for count in range(lados):
    forward(108)
    right(angulo)


done()
