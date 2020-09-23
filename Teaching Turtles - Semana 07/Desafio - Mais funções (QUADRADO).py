#Desafio: Mais funções (QUADRADO)

#Defina e use uma função para desenhar outra forma, como um quadrado
#ou um triângulo, ou qualquer outra coisa que você queira desenhar!

from turtle import *

def drawStar():
    pendown()
    begin_fill()
    for side in range(4):
        left(90)
        forward(100)
    end_fill()
    penup()

color("Red")
bgcolor("Black")

drawStar()
left(90)
forward(100)


hideturtle()
done()
