frase = input("Digite a frase: ")
palavras = frase.split()
palavras_revertidas = palavras[::-1]
frase_revertida = " ".join(palavras_revertidas)
print(frase_revertida)
