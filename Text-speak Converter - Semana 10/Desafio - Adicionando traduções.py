#Desafio - Adicionando traduções

textoDicionario = {
    "rs" : "risos",
    "tmb" : "também",
    "vc" : "você",
    "pq" : "porque"
}

frase = input("Insira uma frase para traduzir: ").lower()
traducao = frase.split()
traducaofrase = ""

for texto in traducao:
    if texto in textoDicionario:
        traducaofrase += textoDicionario[texto] + " "
    else:
        traducaofrase += texto + " "
print("==>")
print(traducaofrase)
