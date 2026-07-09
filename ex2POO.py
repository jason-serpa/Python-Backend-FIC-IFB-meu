'''Implemente um sistema orientado a objetos em Python para
representar uma biblioteca com as classes Biblioteca, Livro,
Autor e Usuário, aplicando os conceitos de associação,
agregação, composição e dependência. A classe Autor deve
armazenar nome e nacionalidade; a classe Livro deve conter
título, ano e uma referência a um Autor (agregação). A
Biblioteca deve possuir um nome e ser responsável por criar e
armazenar os livros internamente (composição). A classe
Usuario deve conter o nome e manter uma referência à
Biblioteca à qual está associado (associação), além de possuir
um método para pegar um livro emprestado, usando
temporariamente o livro sem armazená-lo (dependência).'''

class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade
    
    def exibir_autor(self):
        return f"{self.nome}, {self.nacionalidade}"

class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor #Agregação

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = [] 

    def adicionar_livro(self, titulo, ano, autor): 
        livro = Livro(titulo, ano, autor) #Composição
        self.livros.append(livro)
        return livro


class Usuario:
    def __init__(self, nome, biblioteca):
        self.nome = nome
        self.biblioteca = biblioteca #Associação

    def pegar_livro(self, titulo):
        for livro in self.biblioteca.livros: #Dependência
            if titulo == livro.titulo:
                print(f"Usuário {self.nome} pegou {livro.titulo}, de {livro.ano} por {livro.autor.nome} que é {livro.autor.nacionalidade}.")
                return livro
        print("Livro não encontrado.")
        return None
    

autor1 = Autor(nome="Erin Hunter", nacionalidade="Inglês")
autor2 = Autor(nome="Machado de Assis", nacionalidade="Brasileiro")

biblioteca = Biblioteca("Biblioteca Principal")

biblioteca.adicionar_livro(titulo="Gatos Guerreiros", ano=2003, autor=autor1)
biblioteca.adicionar_livro(titulo="Dom Casmurro", ano=1899, autor=autor2)

admin = Usuario(nome="Admin", biblioteca=biblioteca)

admin.pegar_livro(titulo="Gatos Guerreiros")