#Questão 01

cod = 100
titulo = ""
def ler():
    global titulo
    titulo = str(input("Informe o título do livro: ")).strip()
    return titulo

while ler() != "":
    isbn = input("Informe o ISBN do livro: ").strip()
    autor = input("Qual o autor?: ").strip()
    preco = float(input("Informe o preço do livro: "))
    cod += 1
    if titulo == "":
        break
    print(f'Código: {cod}\nTítulo: {titulo}\nISBN: {isbn}\nAutor: {autor}\nPreço: {preco:.2f}')
        


