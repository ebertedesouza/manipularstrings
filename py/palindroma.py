def expandir_centro(s, esquerda, direita):
    while esquerda >= 0 and direita < len(s) and s[esquerda] == s[direita]:
        esquerda -= 1
        direita += 1
    return s[esquerda + 1:direita]

def encontrar_substring_palindroma(s):
    if len(s) < 2:
        return s

    substring_palindroma = ""
    for i in range(len(s)):
        palindromo_impar = expandir_centro(s, i, i)
        if len(palindromo_impar) > len(substring_palindroma):
            substring_palindroma = palindromo_impar

        palindromo_par = expandir_centro(s, i, i + 1)
        if len(palindromo_par) > len(substring_palindroma):
            substring_palindroma = palindromo_par

    return substring_palindroma

string = input("Digite a string: ")
substring_palindroma = encontrar_substring_palindroma(string)
print(substring_palindroma)
