#Desafio: Adicione mais cumprimentos

from random import *

print("Gerador de Cumprimentos")
print("-----------------------")

adjetivos = ["maravilhoso","acima da média", "excelente",
             "um caminhão carregado de ouro", "admirável",
             "brilhante", "magnífico", "eminente","bravo"]
hobbies = ["ler", "andar de bicicleta", "programar", "ouvir musica",
           "fazer chá", "fazer caminhada", "correr","meditar",
           "fazer yoga", "cantar", "viajar", "pescar"]
nome = input("Qual o seu nome?: ")
print("Aqui está o seu cumprimento", nome,":")

print(nome, "você é", choice(adjetivos), "em", choice(hobbies))
print("De nada!")
    
    
    
    
