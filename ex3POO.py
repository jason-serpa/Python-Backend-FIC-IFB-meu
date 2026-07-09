''' 
Implemente um sistema de biblioteca em Python utilizando Orientação a Objetos. O
sistema deve permitir gerenciar livros, autores e usuários, possibilitando empréstimos de forma
simplificada.
Requisitos:
Classes principais:
Autor: armazena nome e nacionalidade.
Livro: armazena título, ano e referência a um Autor.
Biblioteca: armazena nome e mantém internamente os livros; deve permitir adicionar e listar
livros.
Usuário: armazena nome e mantém referência à biblioteca; deve permitir pegar livros
emprestados temporariamente.
Funcionalidades do sistema:
Listar livros disponíveis.
Adicionar livros à biblioteca.
Permitir empréstimo de livros pelo usuário.
Encerrar o sistema.'''

from time import sleep
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
        self.disponivel = True

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = [] 

    def adicionar_livro(self, titulo, ano, autor): 
        livro = Livro(titulo, ano, autor) #Composição
        self.livros.append(livro)
        return livro
    def listar_livros(self):
        if self.livros == []:
            print("Não há livros no sistema.")
            return
        for livro in self.livros:
            if livro.disponivel:
                dispText = "Disponível"
            else:
                dispText = "Emprestado"
            print("===========================================")
            print(f"- Título: {livro.titulo}\n- Ano: {livro.ano}\n- Autor: {livro.autor.nome}\n- Nacionalidade: {livro.autor.nacionalidade}\n- Status: {dispText}\n")
            return
            


class Usuario:
    def __init__(self, nome, biblioteca):
        self.nome = nome
        self.biblioteca = biblioteca #Associação

    def emprestar_livro(self, titulo):
        for livro in self.biblioteca.livros: #Dependência
            if titulo == livro.titulo and livro.disponivel == True:
                print(f"Usuário {self.nome} pegou {livro.titulo}, de {livro.ano} por {livro.autor.nome} que é {livro.autor.nacionalidade}.")
                livro.disponivel = False
                return livro
                
        print("Livro não encontrado.")
        return None


def main():
    autor1 = Autor(nome="Erin Hunter", nacionalidade="Inglês")
    autor2 = Autor(nome="Machado de Assis", nacionalidade="Brasileiro")
    autor3 = Autor(nome="Rick Riordan", nacionalidade="Norte-Americano")

    biblioteca = Biblioteca("Biblioteca Principal")

    biblioteca.adicionar_livro(titulo="Gatos Guerreiros", ano=2003, autor=autor1)
    biblioteca.adicionar_livro(titulo="Dom Casmurro", ano=1899, autor=autor2)
    biblioteca.adicionar_livro(titulo="O Ladrão de Raios", ano=2005, autor=autor3)

    usuarios = []
    usuarios.append(Usuario(nome="Sergio A", biblioteca=biblioteca))
    usuarios.append(Usuario(nome="Ana B", biblioteca=biblioteca))
    usuarios.append(Usuario(nome="Admin C", biblioteca=biblioteca))

    while True:
        i = int(input('''
====================SGB====================
1- Listar livros
2- Adicionar Livro
3- Empréstimo
4- Listar livros emprestados para usuário
                      
> '''))
        
        if i == 1: # Listar livros
            biblioteca.listar_livros()

        elif i == 2: # Addicionar livros
            titulo = input("Insira o título do livro:\n")
            ano = input("Insira o ano do livro:\n")
            autor = input("Insira o autor do livro:\n")
            if autor != autor1.nome and autor != autor2.nome and autor != autor3.nome:
                nacionalidade = input("Autor não encontrado, informe nacionalidade:\n")
                autor = Autor(autor, nacionalidade)
            if autor == autor1.nome:
                autor = autor1
            if autor == autor2.nome:
                autor = autor2
            if autor == autor3.nome:
                autor = autor3
            
            biblioteca.adicionar_livro(titulo=titulo, ano=ano, autor=autor)
            
        elif i == 3: # Empréstimo

            livroNome = input("Insira o nome do livro:\n> ")

            usuario = None
            usuarioNome = input("Insira o nome do usuário:\n> ")
            
            for user in usuarios:
                if user.nome == usuarioNome:
                    usuario = user
            
            if usuario != None:
                i = int(input(f'''
====================SGB====================
Deseja efetuar o empréstimo do livro {livroNome}
para o usuário {usuario.nome}?                      
1- Sim
2- Não
> '''))
                
                if i == 1:
                    usuario.emprestar_livro(livroNome)

        elif i == 4: # Encerrar sistema
            break
        sleep(2)


if __name__ == "__main__":
    main()