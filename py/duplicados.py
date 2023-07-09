string = input("Digite a string: ")
caracteres_unicos = set()
string_sem_duplicados = ""
for char in string:
    if char not in caracteres_unicos:
        caracteres_unicos.add(char)
        string_sem_duplicados += char

print(string_sem_duplicados)
