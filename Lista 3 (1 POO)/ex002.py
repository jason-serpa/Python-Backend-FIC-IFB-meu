
'''2. Faça um programa em Python orientado a objetos que, a
partir de uma string digitada pelo usuário, imprima:
◦ O número de caracteres da string;
◦ A string com todas suas letras em maiúsculo;
◦ A string com todas suas letras em minúsculo;
◦ O número de vogais da string;
◦ Se a substring “IFB” aparece no texto (ignorando
maiúsculas/minúsculas).
'''

class Palavra:
    def __init__(self, palavra : str):
        self.quantidade = len(palavra)
        self.maiusculo = palavra.upper()
        self.minusculo = palavra.lower()
        vogais = ["A", "E", "I", "O", "U"]
        self.vogais = 0
        for letra in palavra.upper():
            if letra in vogais:
                self.vogais +=1
        if "IFB" in palavra.upper():
            self.ifb = True
        else:
            self.ifb = False

amendoim = Palavra("Amendoim")
print("◦ O número de caracteres da string:", amendoim.quantidade)
print("◦ A string com todas suas letras em maiúsculo:", amendoim.maiusculo)
print("◦ A string com todas suas letras em minúsculo:", amendoim.minusculo)
print("◦ O número de vogais da string:", amendoim.vogais)
print("Se a substring “IFB” aparece no texto (ignorando maiúsculas/minúsculas):", amendoim.ifb)
