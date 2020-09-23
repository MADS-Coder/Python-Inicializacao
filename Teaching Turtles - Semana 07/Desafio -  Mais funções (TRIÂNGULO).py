#Desafio: Mais funções (TRIÂNGULO)

#Defina e use uma função para desenhar outra forma, como um quadrado
#ou um triângulo, ou qualquer outra coisa que você queira desenhar!

from turtle import *

def drawStar():
    pendown()
    begin_fill()
    for side in range(3):
        left(120)
        forward(100)
    end_fill()
    penup()

color("Yellow")
bgcolor("Black")

drawStar()
forward(150)
drawStar()
left(120)
forward(250)
drawStar()


hideturtle()
done()
