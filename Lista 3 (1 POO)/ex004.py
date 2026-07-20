'''
4. Crie um programa em Python utilizando orientação a objetos
para gerenciar uma lista de produtos de um carrinho de
compras. Implemente uma classe chamada Produto, com
atributos privados (__nome, __preco e __quantidade) e
métodos públicos para acessar e modificar esses valores de
forma segura (getters e setters). Em seguida, implemente uma
classe CarrinhoDeCompras, que mantém uma lista de objetos
Produto e possui métodos para adicionar um produto ao
carrinho, remover um produto pelo nome, calcular o valor total
da compra e listar os produtos com suas quantidades e
preços individuais. O programa principal deve permitir que o
usuário adicione e remova produtos, visualize o conteúdo do
carrinho e o total da compra. Utilize encapsulamento para
proteger os dados dos produtos e boas práticas de
organização orientada a objetos.'''

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome
    def get_preco(self):
        return self.__preco
    def get_quantidade(self):
        return self.__quantidade
    
    def set_nome(self, novoNome):
        self.__nome = novoNome
    def set_preco(self, novoPreco):
        self.__preco = novoPreco
    def set_quantidade(self, novaQuan):
        self.__quantidade = novaQuan
        


class Carrinho:
    def __init__(self, produtos : list):
        self.produtos = produtos
    
    def Adicionar(self):
        self.produtos.append(Produto(nome=input("\nInsira o nome do produto:\n> "), \
                                    preco=float(input("\nInsira o preço do produto:\n> ")), \
                                    quantidade=int(input("\nInsira a quantidade de produtos:\n> "))))
        
    def Remover(self):
        i = 0
        print("Escolha um dos produtos a seguir:")
        for produto in self.produtos:
            produto : Produto
            i+=1
            print(f"> {i}: {produto.get_nome()}")
        escolha = int(input("\n> "))         
        if escolha not in range(1, i+1):
            print("Escolha inválida")
            return
        
        print("Escolha válida")
        quantAtual = self.produtos[escolha-1].get_quantidade()
        quant = int(input("Deseja remover quantos itens?\n> "))
        if quant > quantAtual:
            print("Quantidade inválida")
            return
        print("Quantidade válida")
        
        self.produtos[escolha-1].set_quantidade(quantAtual-quant)
        if self.produtos[escolha-1].get_quantidade() == 0:
            print("Produto eliminado da lista")
            self.produtos.pop(escolha-1)
        else:
            print("Quantidade atualizada.")
            print(f"Quantidade atual: {self.produtos[escolha-1].get_quantidade()} unidades")
            
    def Calcular(self):
        total = 0
        for produto in self.produtos:
            produto : Produto
            if produto.get_quantidade() != 1:
                total += produto.get_preco()*produto.get_quantidade()
            else:
                total += produto.get_preco()
        print("Valor total:", total, "R$")

    def Listar(self):
        print("-"*20, "Produtos", "-"*20)
        for produto in self.produtos:
            produto : Produto
            print()
            print("-", produto.get_nome())
            print(">>", produto.get_quantidade(), "unidades")
            print(">>", produto.get_preco(), "R$")

carrinhoDeCompras = Carrinho(produtos=[])

while True:
    i = int(input('''
=============Carrinho de Compras=================
1 - Adicionar ao carrinho
2 - Remover do carrinho
3 - Calcular total              
4 - Listar produtos
> '''))
    if i == 1:
        carrinhoDeCompras.Adicionar()
    elif i == 2:
        carrinhoDeCompras.Remover()
    elif i == 3:
        carrinhoDeCompras.Calcular()
    elif i == 4:
        carrinhoDeCompras.Listar()