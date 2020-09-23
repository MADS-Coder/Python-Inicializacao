#Desafio: Desenhando Planetas

#Crie uma função para desenhar um planeta chamado drawStar(). Passe dados para
#a função para que você possa especifar o tamanho e a cor do planeta que você
#quer desenhar

from turtle import *

def drawStar(starSize, starColour, starBgcolor):
    color(starColour)
    bgcolor(starBgcolor)
    pendown()
    begin_fill()
    for side in range(360):
        left(1)
        forward(starSize)
    end_fill()
    penup()


tamanho = int(input("Digite o tamanho do planeta ente [1 a 5]: "))
cor = str(input("Digite uma cor em inglês: "))
fundo = str(input("Digite uma cor de fundo em inglês: "))
drawStar(tamanho, cor, fundo)

hideturtle()
done()
