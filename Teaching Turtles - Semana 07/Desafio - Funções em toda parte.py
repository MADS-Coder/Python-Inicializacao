#Desafio: Funções em toda parte!

from turtle import *
from random import *


def moveToRandomLocation():
    penup()
    setpos(randint(-400,400), randint(-400,400))
    pendown()

def drawStar(starSize, starColour):
    color(starColour)
    pendown()
    begin_fill()
    for side in range(8):
        forward(starSize)
        right(108)
    end_fill()
    penup()

def drawGalaxia(numero):
    starColours = ["#00CED1","#8B0000","#FFFF00"]
    moveToRandomLocation()
    for star in range(numero):
        drawStar(6, choice(starColours))
        pendown()
        forward(108)
        right(109)
    drawStar(6, choice(starColours))

def drawConstelacao(numero):
    moveToRandomLocation()
    for star in range(numero):
        drawStar(109, "White")
        pendown()
        forward(108)
        right(109)
    drowStar(109, "White")

speed(20)
bgcolor("PowderBlue")

for star in range(12):
    drawGalaxia(66)
for constelacao in range(12):
    drawConstelacao(6)

hideturtle()
done()
    
