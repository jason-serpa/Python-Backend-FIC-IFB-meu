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