'''
 Crie um programa em Python utilizando herança para
representar um sistema simples de funcionários. Implemente
uma classe base chamada Funcionario, com os atributos nome
(String) e salarioBase (double), além de um método
calcularSalario() que retorna o salário base e um método
exibirDados() que imprime o nome e o salário. Em seguida, crie
uma subclasse chamada FuncionarioComissionado, que herda
de Funcionario e possui o atributo adicional comissao (double).
Essa subclasse deve sobrescrever o método calcularSalario()
para retornar a soma do salário base com a comissão, e
também sobrescrever exibirDados() para incluir a comissão nas
informações exibidas. Por fim, instancie um objeto de cada
classe e utilize os métodos definidos para mostrar os dados
dos funcionários.

'''
class Funcionario:
    def __init__(self, nome : str, salarioBase : float):
        self.nome = nome
        self.salarioBase = salarioBase

    def calcular_salario(self):
        return self.salarioBase
    def exibir_dados(self):
        return self.nome, self.salarioBase
    
class FuncionarioComissionado(Funcionario):
    def __init__(self, nome : str, salarioBase : float, comissao : float):
        super().__init__(nome, salarioBase)
        
        self.comissao = comissao
    def calcular_salario(self):
        return self.salarioBase + self.comissao
    def exibir_dados(self):
        return self.nome, self.salarioBase, self.comissao





comm = FuncionarioComissionado("Jorge", 1500, 200)
normal = Funcionario("Antonio", 1500)

print(f"\nNome do funcionário: {normal.exibir_dados()[0]}\
\nSalário base: {normal.exibir_dados()[1]:.2f}\
\nSalário total: {normal.calcular_salario():.2f}")

print(f"\nNome do funcionário: {comm.exibir_dados()[0]}\
\nSalário: {comm.exibir_dados()[1]:.2f}\
\nComissão: {comm.exibir_dados()[2]:.2f}\
\nSalário total: {comm.calcular_salario():.2f}")
    