#DESAFIO QUIZ
#Mantendo a pontuação

from time import sleep

print('-=' * 40)
print(f'{"JOGO DE PERGUNTAS E RESPOSTAS":^75}')
print('-=' * 40)
print('''Vou fazer 5 perguntas para você, vamos ver quantas você vai conseguir acertar. \nOk?\n
(1). Em qual lugar do mundo encontra-se a Fossa das Marianas? (2 pontos)
[a] - Oceano Pacífico
[b] - Oceano índico
[c] - Oceano Atlântico
[d] - Oceano Glacial Ártico
[e] - Oceano Glacial Antártico''')
resp1 = str(input('Qual a resposta correta? '))
sleep(0.5)

print('''\n(2). Qual desenho/anime tem um personagem chamado Tobirama? (2 pontos)
[a] - Shingeki no Kyojin
[b] - Naruto
[c] - One Piece
[d] - Dragon Ball
[e] - Chaves''')
resp2 = str(input('Qual a resposta correta? '))
sleep(0.5)

print('''\n3 - Qual o filme tem um personagem chamado Neo interpretado por Keanu Reeves? (1 ponto)
[a] - Deu a Louca na Chapeozinho Vermelho
[b] - Matrix
[c] - Constantine
[d] - Harry Potter
[e] - Chaves''')
resp3 = str(input('Qual a resposta correta? '))
sleep(0.5)

print('''\n4 - Quem criou a internet (World Wide Web)? (2 pontos)
[a] - Guido van Rossum
[b] - James Gosling
[c] - Rasmus Lerdorf
[d] - Tim Berners-Lee
[e] - Niklaus Wirth''')
resp4 = str(input('Qual a resposta correta? '))
sleep(0.5)

print('''\n5 - Qual a característica da linguagem Python? (3 pontos)
[a] - É uma linguagem de programação imperativa, interpretada, de alto nível e com tipagem forte e dinâmica.
É considerada uma linguagem multi-paradigma, pois aceita diferentes formas de programação.
[b] - É uma linguagem de alto nível com uma sintaxe bastante estruturada e flexível tornando sua programação bastante simplificada. ·
Os programas são compilados, gerando programas executáveis.
[c] - É capaz de representar em termos de código, tudo o que existe no mundo real. Interpreta tudo a sua volta como sendo um objeto, ou seja,
tem como premissa a concentração na modelagem das características e comportamento dos objetos no mundo real.
[d] - É uma linguagem de programação de domínio específico, ou seja, seu escopo se estende a um campo de atuação que é o desenvolvimento web.
Seu propósito principal é de implementar soluções web velozes, simples e eficientes.
[e] - Apresenta um número muito reduzido de instruções, do tipo operações de movimentação de dados em memória, para registros e para memórias,
e operações lógicas e aritméticas bem simples.Estas instruções são de baixa expressividade, isto é, elas são de baixo nível''')
resp5 = str(input('Qual a resposta correta? '))
sleep(0.5)

score = 0
if resp1 == 'a':
    score = 2
if resp2 == 'b':
    score += 2 
if resp3 == 'b':
    score += 1 
if resp4 == 'd':
    score += 2
if resp5 == 'a':
    score += 3

print(f'Você tirou {score} pontos.')
