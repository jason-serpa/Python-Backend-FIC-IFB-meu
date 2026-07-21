'''9. Implemente em Python um sistema para uma plataforma de
cursos online que utilize herança e polimorfismo,
armazenando os dados em uma lista. Crie uma classe base
chamada Participante, com os atributos nome e email, e um
método emitirCertificado() que retorna uma mensagem
genérica. Em seguida, crie as subclasses Aluno, com o
atributo curso, e Instrutor, com o atributo especialidade,
ambas sobrescrevendo o método emitirCertificado() com
mensagens específicas: o aluno recebe um certificado de
conclusão do curso e o instrutor um certificado de participação
como palestrante. O programa deve conter um menu com as
opções: 1) Cadastrar participante, 2) Listar participantes, 3)
Emitir certificados, e 0) Sair. O usuário deve escolher entre
cadastrar um aluno ou instrutor, e os dados devem ser
armazenados em uma lista de objetos do tipo Participante. O
método emitirCertificado() deve ser chamado de forma
polimórfica para cada participante cadastrado.'''

class Participante:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    def emitir_certificado(self):
        print(f"Certificado emitido para {self.nome}.")

class Aluno(Participante):
    def __init__(self, nome, email, curso):
        super().__init__(nome, email)
        self.curso = curso
        '''o aluno recebe um certificado de
conclusão do curso e o instrutor um certificado de participação
como palestrante.'''
    def emitir_certificado(self):
        print(f"Certificado de conclusão de curso emitido para {self.nome}.")
class Instrutor(Participante):
    def __init__(self, nome, email, especialidade):
        super().__init__(nome, email)
        self.especialidade = especialidade
    def emitir_certificado(self):
        print(f"Certificado de participação de palestrante emitido para {self.nome}")

    
'''1) Cadastrar participante, 2) Listar participantes, 3)
Emitir certificados, e 0) Sair. O usuário deve escolher entre
cadastrar um aluno ou instrutor, e os dados devem ser
armazenados em uma lista de objetos do tipo Participante. O
método emitirCertificado() deve ser chamado de forma
polimórfica para cada participante cadastrado.'''

participantes = []
while True:
    i = int(input('''
================Emissões de Certificado================
1. Cadastrar participante
2. Listar participantes
3. Emitir certificados
4. Sair do programa
> '''))
    if i == 1:
        nome = input("Insira o nome do participante:\n> ").upper()
        email= input("Insira o endereço de email:\n> ").upper()
        escolha = int(input("O participante é aluno ou professor?\n1- Aluno\n2- Professor\n> "))
        if escolha == 1:
            participantes.append(Aluno(nome=nome, email=email, curso=input("Insira o curso:\n> ").upper()))
        if escolha == 2:
            participantes.append(Instrutor(nome=nome, email=email, especialidade=input("Insira a especialidade:\n> ").upper()))
        else:
            print("Escolha inválida")
        
    if i == 2:
        print("Participantes:")
        for participante in participantes:
            print(">", participante.nome)
            print(">> Email:", participante.email)
            if type(participante) == Aluno:
                print(">> Curso:", participante.curso)
            elif type(participante) == Instrutor:
                print(">> Especialidade:", participante.especialidade)
            
            print()
    if i == 3:
        try:
            print("Escolha um participante:")
            quant = 0
            for participante in participantes:
                quant+=1
                print(quant, "-", participante.nome)
            i = int(input("> "))
            if i not in range(quant+1):
                print("Escolha inválida")
                raise Exception
            
            participantes[i-1].emitir_certificado()
        except Exception as err:
            print(f"Algo deu errado.\n>>ERRO: {err}")
    if i == 4:
        break
    