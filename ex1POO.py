'''
Crie um sistema para gerenciar contas de uma biblioteca. 
Implemente uma classe Livro, com atributos como título, 
autor e um identificador único (ID), sendo que todos devem ser privados. 
A classe deve conter um construtor para inicializar os dados e métodos 
públicos para acessar (get) e modificar (set) os atributos, respeitando 
o encapsulamento. Em seguida, crie uma classe Usuario, com atributos como nome, 
número de matrícula (privado) e uma lista de livros emprestados. Adicione métodos 
públicos para realizar empréstimos e devoluções de livros, garantindo que a 
matrícula seja acessada e modificada apenas por métodos da própria classe.
'''
from time import sleep

class Livro:
    def __init__(self, id, titulo, autor):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor 
    
    def get_id(self):
        return self.__id
    def get_titulo(self):
        return self.__titulo
    def get_autor(self):
        return self.__autor
    
    def set_id(self, novoID):
        self.__id = novoID
    def set_titulo(self, novoTitulo):
        self.__titulo = novoTitulo
    def set_autor(self, novoAutor):
        self.__autor = novoAutor
    
class Usuario:
    def __init__(self, nome, matricula, livrosEmprestados):
        self.nome = nome
        self.__matricula = matricula
        self.livrosEmprestados = livrosEmprestados if livrosEmprestados is not None else []

    def emprestar_livro(self, livro):
        if livro not in self.livrosEmprestados:
            self.livrosEmprestados.append(livro)
            print("Livro emprestado com sucesso.")
        else:
            print("Livro já se encontra emprestado.")

    def devolver_livro(self, livro):
        if livro in self.livrosEmprestados:
            self.livrosEmprestados.remove(livro)
            print("Livro devolvido com sucesso.")
        else:
            print("Livro não possuído.")


    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, novaMatricula):
        self.__matricula = novaMatricula



def main():
    biblioteca = []
    usuarios = []

    biblioteca.append(Livro(id=1, titulo="Dom Casmurro", autor="Machado de Assis"))
    biblioteca.append(Livro(id=2, titulo="Gatos Guerreiros", autor="Erin Hunter"))
    biblioteca.append(Livro(id=3, titulo="O Ladrão de Raios", autor="Rick Riordan"))
    usuarios.append(Usuario(nome="Sergio", matricula="00001", livrosEmprestados=None))
    usuarios.append(Usuario(nome="Ana", matricula="00002", livrosEmprestados=[biblioteca[2]]))

    while True:
        i = int(input('''
====================SGB====================
1- Listar livros
2- Empréstimo de livro
3- Devolução de livro
4- Listar livros emprestados para usuário
                      
> '''))
        
        if i ==1:
            print("\nLivros no sistema:")
            for i in range(len(biblioteca)):
                print(f"- {biblioteca[i].get_titulo()}, {biblioteca[i].get_autor()}")
            pass
            sleep(2)

        elif i == 2: # Empréstimo
            nome = input("Insira o nome do livro:\n> ")
            livro = None
            user = None
            for i in range(len(biblioteca)):
                if nome in biblioteca[i].get_titulo():
                    print(f"\nLivro encontrado: {biblioteca[i].get_titulo()}, {biblioteca[i].get_autor()}")
                    livro = biblioteca[i]
            
            if livro != None:
                matri = input("\nInsira o número da matrícula.\n> ")
                for usuario in usuarios:
                    if usuario.get_matricula() == matri:
                        print(f"\nUsuário {usuario.nome} encontrado\n")
                        user = usuario    
            else:
                print("\nLivro não encontrado.")
                sleep(2)
            
            if user != None:
                i = int(input(f'''
====================SGB====================
Deseja efetuar o empréstimo do livro {livro.get_titulo()}?
para o aluno {user.nome}?                      
1- Sim
2- Não
> '''))
                
                if i == 1:
                    user.emprestar_livro(livro)
                
        elif i == 3: # Devolução
            nome = input("Insira o nome do livro:\n> ")
            livro = None
            user = None
            for i in range(len(biblioteca)):
                if nome in biblioteca[i].get_titulo():
                    print(f"\nLivro encontrado: {biblioteca[i].get_titulo()}, {biblioteca[i].get_autor()}")
                    livro = biblioteca[i]
            
            if livro != None:
                matri = input("\nInsira o número da matrícula.\n> ")
                for usuario in usuarios:
                    if usuario.get_matricula() == matri:
                        print(f"\nUsuário {usuario.nome} encontrado\n")
                        user = usuario    
            else:
                print("\nLivro não encontrado.")
                sleep(2)

            
            if user != None:

                i = int(input(f'''
====================SGB====================
Deseja efetuar a devolução do livro {livro.get_titulo()}?
para o aluno {user.nome}?                      
1- Sim
2- Não
> '''))
                
                if i == 1:
                    user.devolver_livro(livro)

        elif i == 4: # Listar possuídos
            user = None
            matricula = input("Insira o número da matrícula\n> ")
            for usuario in usuarios:
                if matricula == usuario.get_matricula():
                    print(f"\nUsuário {usuario.nome} encontrado")
                    user = usuario
            
            for i in range(len(usuario.livrosEmprestados)):
                print(f"- {usuario.livrosEmprestados[i].get_titulo()}, {usuario.livrosEmprestados[i].get_autor()}")

            sleep(2)



if __name__ == "__main__":
    main()