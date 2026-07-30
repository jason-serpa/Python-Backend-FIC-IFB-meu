'''2. Implemente um sistema bancário em Python, utilizando os conceitos de Programação
Orientada a Objetos, conforme o exemplo abaixo. O sistema deve simular operações
bancárias como criação de contas (corrente e poupança), depósitos, saques, transferências,
alteração e histórico de titularidade, além do gerenciamento de chave Pix.

O sistema deve possuir as seguintes características:

Cadastro de clientes (pessoa física ou jurídica) e contas bancárias.

Depósito, saque e transferência entre contas (exceto para contas poupança, que não
permitem transferências).

Alteração do nome do titular da conta, com registro do histórico de alterações (data, nome
antigo e novo).

Consulta do histórico de titularidade, exibindo o número da conta, o titular atual, CPF/CNPJ
e a chave Pix cadastrada.

Gerenciamento de chave Pix: cadastrar e alterar a chave Pix, validando conforme os
padrões do Banco Central (CPF, CNPJ, e-mail, telefone ou chave aleatória UUID). O código
de validação deve citar as referências utilizadas para os padrões de regex.

Exibição do extrato da conta, incluindo todas as transações realizadas e as principais taxas
bancárias.

Busca de contas por número, nome do titular ou CPF/CNPJ, inclusive para alteração de
titularidade ou limite.

Interface de menu para interação com o usuário, permitindo executar todas as operações
acima.'''



## DIA 11 SEM AULA

'''
Menu:
1 - Listar contas
2 - Depositar
3 - Sacar
4 - Transferir
5 - Extrato
6 - Criar nova conta
7 - Alterar titular da conta (por número, nome ou CPF/CNPJ)
8 - Ver histórico de titularidade
9 - Alterar limite de conta corrente
10 - Cadastrar chave Pix
11 - Alterar chave pix
12 - Sair

Escolha uma opção: 10
Número da conta: 2020
Digite a chave pix para cadastrar: 123.456.789-09
Chave Pix '123.456.789-09' cadastrada com sucesso para a conta 2020.
'''
from datetime import datetime as dt
import re
class Validador_REGEX:
    # CPF: 11 dígitos, com ou sem máscara (xxx.xxx.xxx-xx)
    # Referência: Receita Federal - formato numérico de 11 dígitos do CPF
    REGEX_CPF = r'^\d{3}\.?\d{3}\.?\d{3}\-?\d{2}$'

    # CNPJ: 14 caracteres — aceita tanto o formato numérico tradicional quanto o
    # novo formato alfanumérico (raiz + filial alfanuméricas, DV sempre numérico),
    # com ou sem máscara (AA.AAA.AAA/AAAA-DV)
    # Referência: Instrução Normativa RFB nº 2.229/2024 (Receita Federal) -
    # CNPJ alfanumérico, vigente a partir de 31/07/2026
    REGEX_CNPJ = r'^[A-Z0-9]{2}\.?[A-Z0-9]{3}\.?[A-Z0-9]{3}\/?[A-Z0-9]{4}\-?\d{2}$'

    # E-mail: formato simplificado — usuário@domínio.extensão
    # Referência: RFC 5322 (https://www.rfc-editor.org/rfc/rfc5322), seção 3.4.1, simplificada.
    # LIMITAÇÃO CONHECIDA: não valida domínios com múltiplos subdomínios (ex: .com.br);
    REGEX_EMAIL = r'^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$'

    # Telefone: formato E.164 usado como chave Pix — "+55" seguido de DDD e número
    # (10 dígitos para fixo, 11 para celular, incluindo o 9 na frente)
    # Referência: Manual de Padrões para Iniciação do Pix - Banco Central do Brasil
    # (chave celular deve estar no formato E.164: +55DDDNNNNNNNNN)
    REGEX_TELEFONE = r'^\+55\d{10,11}$'

    # Chave aleatória: UUID versão 4 — 32 caracteres hexadecimais em 5 grupos
    # separados por hífen (8-4-4-4-12), com o dígito de versão fixo em "4"
    # Referência: RFC 4122 (https://www.rfc-editor.org/rfc/rfc4122) - formato UUID
    REGEX_UUID = r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'

    @staticmethod
    def validar(chave : str):
        if re.match(Validador_REGEX.REGEX_EMAIL, chave):
            return "email"
        if re.match(Validador_REGEX.REGEX_TELEFONE, chave):
            return "telefone"
        if re.match(Validador_REGEX.REGEX_CNPJ, chave, re.IGNORECASE):
            return "cnpj"
        if re.match(Validador_REGEX.REGEX_CPF, chave):
            return "cpf"
        if re.match(Validador_REGEX.REGEX_UUID, chave):
            return "aleatoria"
        return None
    
class Cliente:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)

class PessoaJuridica(Cliente):
    def __init__(self, nome, cnpj):
        super().__init__(nome, cnpj)


class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.__contas = []

    def criar_conta(self):
        i = input("Deseja criar uma conta poupança ou corrente?\n1- Poupança\n2- Corrente\n> ")
        nome = input("Informe o nome do titular da conta.\n> ")
        tipo_pessoa = input("Pessoa física ou jurídica?\n1 - Física\n2 - Jurídica\n> ")
        if tipo_pessoa == "1":
            cpf = input("Informe o CPF do titular.\n> ")
            titular = PessoaFisica(nome, cpf)
        elif tipo_pessoa == "2":
            cnpj = input("Informe o CNPJ do titular.\n> ")
            titular = PessoaJuridica(nome, cnpj)
        else:
            print("Valor inválido.")
            return

        if i == "1":
            conta = ContaPoupanca(titular, banco=self)
        elif i == "2":
            conta = ContaCorrente(titular, banco=self)
        else:
            print("Valor inválido.")
            return
        self.__contas.append(conta)
        print(f"Conta {conta.numero} criada com sucesso!")

    def buscar_conta(self, tag, valor):
        # tag in ["numero", "nome", "documento"]
        resultados = []             
        for conta in self.__contas:
            if tag == "numero" and str(conta.numero) == valor:
                resultados.append(conta)
            elif tag == "nome" and valor.lower() in conta.get_titular().lower():
                resultados.append(conta)
            elif tag == "documento" and conta.get_cliente().documento == valor:
                resultados.append(conta)
        return resultados
    
    def buscar_conta_interativa(self, mensagem: str = "conta"):
        """Pede um critério de busca ao usuário e devolve uma única conta,
        ou None se não encontrar (ou se o usuário cancelar diante de múltiplos resultados)."""
        print(f"\nBuscar {mensagem} por:")
        criterio_input = input("1 - Número\n2 - Nome\n3 - CPF/CNPJ\n> ")
        mapa_criterio = {"1": "numero", "2": "nome", "3": "documento"}
        criterio = mapa_criterio.get(criterio_input)
        if criterio is None:
            print("Critério inválido.")
            return None

        valor = input(f"Digite o valor para busca ({criterio}): ")
        resultados = self.buscar_conta(criterio, valor)

        if not resultados:
            print("Nenhuma conta encontrada.")
            return None
        if len(resultados) == 1:
            return resultados[0]

        print("Mais de uma conta encontrada:")
        for c in resultados:
            print(f"  Conta {c.numero} — {c.get_titular()}")
        numero_escolhido = input("Digite o número da conta desejada: ")
        for c in resultados:
            if str(c.numero) == numero_escolhido:
                return c
        print("Número não encontrado entre os resultados.")
        return None

    def listar_contas(self):
        if not self.__contas:
            print("Nenhuma conta cadastrada.")
            return
        for conta in self.__contas:
            tipo = "Corrente" if isinstance(conta, ContaCorrente) else "Poupança"
            print(f"Conta {conta.numero} ({tipo}) — Titular: {conta.get_titular()} — Saldo: R${conta.get_saldo()}")

class Transacao:
    def __init__(self, tipo : int, quantidade : float, horario, contaAlvo = None):
        self.tipo = tipo # 1 para depósito, 2 para saque, 3 para transferência
        self.quant = quantidade
        self.horario = horario
        self.contaAlvo = contaAlvo

class ContaPoupanca:
    numero = 0
    def __init__(self, titular : Cliente, banco : Banco):
        self.__titular = titular
        self.banco = banco
        ContaPoupanca.numero += 1
        self.numero = ContaPoupanca.numero
        self.__saldo = float(0)
        self.limite = float(500)
        self.__chave_pix = None
        
        hor = dt.now().strftime("(%d-%m-%Y, %H:%M)")
        self.historico = []
        self.__titulares = [(hor, None, self.__titular)]
        self.__chaves = []

    def depositar(self): 
        quant = input(f"Insira uma quantia que deseja depositar na conta {self.numero}.\n> ")
        try:
            if float(quant) <= 0:
                print("Depósito inválido.")
                raise ValueError("Insira um valor válido.")
            self.set_saldo(float(quant), operacao=True)
            hor = dt.now().strftime("(%d-%m-%Y, %H:%M)")
            self.historico.append(Transacao(1, float(quant), hor))   
        except Exception as err:
            print(f"\nAlgo deu errado.\n>> ERRO: {err}")


    def sacar(self):
        quant = input(f"Insira uma quantia que deseja sacar da conta {self.numero}.\n> ")
        try:
            if float(quant) <= 0:
                print("Saque inválido.")
                raise ValueError("Insira um valor válido.")
            if float(quant) > self.get_saldo():
                print("Saldo insuficiente.")
                raise ValueError("Não há saldo suficiente para a operação de saque.")
            self.set_saldo(float(quant), operacao=False)
            hor = dt.now().strftime("(%d-%m-%Y, %H:%M)")
            self.historico.append(Transacao(2, float(quant), hor))   
        except Exception as err:
            print(f"\nAlgo deu errado.\n>> ERRO: {err}")

    def extrato(self):
        print("-"*10, "Extrato", "-"*10, sep="")
        for transacao in self.historico:
            transacao : Transacao
            print(transacao.horario, " ", end="")
            if transacao.tipo == 1: #Depósito
                print("DEPÓSITO +", end="")
            elif transacao.tipo == 2: #Saque
                print("SAQUE -", end="")
            elif transacao.tipo == 3: #Transferência
                print("TRANSFERENCIA -", end="")

            print(f"R${transacao.quant}", end="")
            if transacao.tipo == 3:
                print(f" Conta \"{transacao.contaAlvo.numero}\"", end="")
            print()
        print("\n")
    def historico_titularidade(self):
        print("-"*10, "Histórico de Titularidade", "-"*10, sep="")
        print(f"Conta: {self.numero}")
        print(f"Titular atual: {self.get_titular()}")
        print(f"CPF/CNPJ: {self.get_cliente().documento}")
        chave = self.__chave_pix if self.__chave_pix is not None else "Não cadastrada"
        print(f"Chave Pix: {chave}")
        print("\nAlterações de titularidade:")
        for hor, antigo, novo in self.__titulares:
            nome_antigo = antigo.nome if antigo is not None else "—"
            print(f">> {hor}: {nome_antigo} > {novo.nome}")
        print()
                        

    def set_saldo(self, quant, operacao):
        if operacao:
            self.__saldo += quant
            print(f"Depósito de R${quant} realizado com sucesso.")
        else:
            self.__saldo -= quant
            print(f"Saque de R${quant} realizado com sucesso.")

    def set_titular(self):
        titAntigo = self.__titular
        if type(self.__titular) == PessoaFisica:
            self.__titular = PessoaFisica(nome=input("Insira o nome do cliente:\n>"),cpf=input("Insira o CPF do cliente:\n>"))
        elif type(self.__titular) == PessoaJuridica:
            self.__titular = PessoaJuridica(nome=input("Insira o nome do cliente:\n>"),cnpj=input("Insira o CNPJ do cliente:\n>"))
        hor = dt.now().strftime("(%d-%m-%Y, %H:%M)")
        self.__titulares.append((hor, titAntigo, self.__titular))

    def set_chave_pix(self, novaChave : str):
        tipo = Validador_REGEX.validar(novaChave)
        if tipo is None:
            print("Chave inválida.")
            return
        chaveAntiga = None
        if self.__chave_pix != None:
            chaveAntiga = self.__chave_pix
        self.__chave_pix = novaChave
        if chaveAntiga != None:
            self.__chaves.append((chaveAntiga, novaChave, dt.now().strftime("(%d-%m-%Y, %H:%M)")))
        print(f"Chave Pix '{novaChave}' cadastrada com sucesso ({tipo}) para a conta {self.numero}.")


    def get_saldo(self):
        return self.__saldo
    def get_titular(self):
        return self.__titular.nome
    def get_cliente(self):
        return self.__titular
    
class ContaCorrente(ContaPoupanca):
    def __init__(self, titular, banco):
        ContaPoupanca.__init__(self, titular, banco)

    def sacar(self):
        quant = input(f"Insira uma quantia que deseja sacar da conta {self.numero}.\n> ")
        try:
            if float(quant) <= 0:
                print("Saque inválido.")
                raise ValueError("Insira um valor válido.")
            if float(quant) > self.get_saldo():
                print("Saldo insuficiente.")
                raise ValueError("Não há saldo suficiente para a operação de saque.")
            if float(quant) > self.limite:
                print("Limite insuficiente.")
                raise ValueError("Limite insuficiente para saque.")
            self.set_saldo(float(quant), operacao=False)
            hor = dt.now().strftime("(%d-%m-%Y, %H:%M)")
            self.historico.append(Transacao(2, float(quant), hor))   
        except Exception as err:
            print(f"\nAlgo deu errado.\n>> ERRO: {err}")

    def transferir(self, conta : "ContaCorrente"):
        quant = input(f"Insira uma quantia para transferir da conta {self.numero} para a conta {conta.numero}.\n> ")
        try:
            if float(quant) <= 0:
                raise ValueError("Valor inválido para transferência")
            if float(quant) > self.get_saldo():
                raise ValueError("Saldo insuficiente para transação")
            if float(quant) > self.limite:
                raise ValueError("Transferência ultrapassa o limite atual.")
            self.set_saldo(float(quant), operacao=False)
            conta.set_saldo(float(quant), operacao=True)
            hor = dt.now().strftime("(%d-%m-%Y, %H:%M)")
            self.historico.append(Transacao(3, float(quant), hor, conta))   
        except Exception as err:
            print(f"\nAlgo deu errado.\n>> ERRO: {err}")    

    def alterar_limite(self, quantia):
        if quantia == self.limite:
            print(f"O limite já está definido como R${quantia}.")
            return
        confirm = input(f"Deseja alterar o limite atual de {self.limite} para {quantia}?\n1 - Sim\n2- Não\n> ")
        if confirm != "1":
            return
        self.limite = quantia


def main():
    banco = Banco("Meu Banco")

    while True:
        i = input("""
Menu:
1 - Listar contas
2 - Depositar
3 - Sacar
4 - Transferir
5 - Extrato
6 - Criar nova conta
7 - Alterar titular da conta
8 - Ver histórico de titularidade
9 - Alterar limite de conta corrente
10 - Cadastrar chave Pix
11 - Alterar chave pix
12 - Sair

> """)

        if i == "1":
            banco.listar_contas()

        elif i == "2":
            conta = banco.buscar_conta_interativa()
            if conta:
                conta.depositar()

        elif i == "3":
            conta = banco.buscar_conta_interativa()
            if conta:
                conta.sacar()

        elif i == "4":
            conta = banco.buscar_conta_interativa(mensagem="conta de origem")
            if conta is None:
                pass
            elif not isinstance(conta, ContaCorrente):
                print("Contas poupança não permitem transferência.")
            else:
                conta_destino = banco.buscar_conta_interativa(mensagem="conta de destino")
                if conta_destino:
                    conta.transferir(conta_destino)

        elif i == "5":
            conta = banco.buscar_conta_interativa()
            if conta:
                conta.extrato()

        elif i == "6":
            banco.criar_conta()

        elif i == "7":
            conta = banco.buscar_conta_interativa()
            if conta:
                conta.set_titular()

        elif i == "8":
            conta = banco.buscar_conta_interativa()
            if conta:
                conta.historico_titularidade()

        elif i == "9":
            conta = banco.buscar_conta_interativa()
            if conta is None:
                pass
            elif not isinstance(conta, ContaCorrente):
                print("Contas poupança não possuem limite.")
            else:
                try:
                    quantia = float(input("Novo limite: "))
                    conta.alterar_limite(quantia)
                except ValueError:
                    print("Valor inválido.")

        elif i in ("10", "11"):
            conta = banco.buscar_conta_interativa()
            if conta:
                nova_chave = input("Digite a chave Pix: ")
                conta.set_chave_pix(nova_chave)

        elif i == "12":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()