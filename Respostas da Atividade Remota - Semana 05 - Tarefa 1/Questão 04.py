#Questão 04


for num in range(10, 1010, 10):
    print(num, end='')
    if num == 1000:
        print('.', end='')
    else:
        print(', ', end='')
