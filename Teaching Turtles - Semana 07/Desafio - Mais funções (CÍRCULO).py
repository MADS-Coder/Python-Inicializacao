#Desafio: Mais funções (CÍRCULO)

#Defina e use uma função para desenhar outra forma, como um quadrado
#ou um triângulo, ou qualquer outra coisa que você queira desenhar!

from turtle import *
speed(100)
def drawStar():
    pendown()
    begin_fill()
    for side in range(360):
        left(1)
        forward(1)
    end_fill()
    penup()

color("Red")
bgcolor("Black")

drawStar()
forward(250)
drawStar()
left(120)
forward(150)
drawStar()


hideturtle()
done()
