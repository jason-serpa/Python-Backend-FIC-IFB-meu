'''
5. Implemente uma classe Impressora com o método
imprimir(Documento d), que recebe um objeto da classe
Documento e imprime suas informações na tela. A classe
Documento deve conter os atributos título e conteúdo. A
classe Impressora apenas utiliza o documento, sem manter
uma referência permanente a ele, caracterizando uma relação
de dependência. Desenvolva um programa com um menu
interativo no console que permita criar vários documentos,
visualizar seu conteúdo por meio da impressora e encerrar o
programa.'''


class Documento:
    def __init__(self, titulo, conteudo):
        self.title = titulo
        self.cont = conteudo


class Impressora:
    def imprimir(self, doc : Documento):
        print()
        print("-"*7, doc.title, "-"*7, sep="")
        print(doc.cont)
        
docs = []
hp = Impressora()
    
while True:
    
    i = int(input('''
==============IMPRESSORA==============
1 - Criar documento
2 - Visualizar documento criado
3 - Finalizar programa
> '''))
    if i == 1:
        # Criar doc
        docNovo = Documento(titulo=input("Insira o título do documento: "), conteudo=input("Insira o conteúdo do documento:\n"))
        docs.append(docNovo)
        print("Documento criado.")
    if i == 2:
        num = 0
        print("Escolha um documento da lista:")
        for doc in docs:
            doc : Documento
            num+=1
            print(f"{num} - {doc.title}")
        escolha = int(input("> "))
        if escolha not in range(1, num+1):
            print("Escolha inválida")
        else:
            hp.imprimir(docs[escolha-1])

    if i == 3:
        break
    