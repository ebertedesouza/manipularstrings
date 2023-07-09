def e_anagrama_palindromo(string):
    contagem_caracteres = {}

    # Conta a quantidade de ocorrências de cada caractere na string
    for caractere in string:
        if caractere in contagem_caracteres:
            contagem_caracteres[caractere] += 1
        else:
            contagem_caracteres[caractere] = 1

    contagem_impares = 0  # Contador de caracteres com ocorrência ímpar

    # Verifica a quantidade de caracteres com ocorrência ímpar
    for contagem in contagem_caracteres.values():
        if contagem % 2 != 0:
            contagem_impares += 1

    # Retorna True se a quantidade de caracteres com ocorrência ímpar for no máximo 1, caso contrário, retorna False
    return contagem_impares <= 1


string = input("Digite a string: ")
e_anagrama_palindromo = e_anagrama_palindromo(string)
print(e_anagrama_palindromo)
