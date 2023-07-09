import re

def capitalizar_frases(string):
    # Divide a string em frases com base em diferentes sinais de pontuação
    frases = re.split(r'(?<=[.!?;])\s+', string)
    frases_capitalizadas = [frase.capitalize() for frase in frases]  # Capitaliza a primeira letra de cada frase
    string_capitalizada = ' '.join(frases_capitalizadas)  # Junta as frases capitalizadas novamente na string
    return string_capitalizada

# Solicita que o usuário insira a frase
string = input("Digite a frase: ")
string_capitalizada = capitalizar_frases(string)
print(string_capitalizada)
