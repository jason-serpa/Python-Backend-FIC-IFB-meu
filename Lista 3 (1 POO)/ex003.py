
'''3. Faça um programa em Python orientado a objetos que receba
uma frase dada pelo usuário e a criptografe. A criptografia
consistirá na troca das vogais da frase por um número
correspondente: A – 4, E – 3, I – 1, O – 0, U – 8.'''

class Palavra:
    def __init__(self, palavra : str):
        self.palavra = palavra.upper()
        self.criptografada = self.palavra.replace("A", "4").replace("E", "3").replace("I", "1").replace("O", "0").replace("U", "8").capitalize()


amendoim = Palavra("Amendoim")
print("Palavra original:", amendoim.palavra)
print("Palavra criptografada:", amendoim.criptografada)