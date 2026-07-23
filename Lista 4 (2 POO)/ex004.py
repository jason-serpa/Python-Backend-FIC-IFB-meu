'''4. Sistema de Votação Eletrônica com Anonimização e Persistência.
Requisitos:
1. Estrutura do sistema
Crie as classes Candidato, Eleitor e Eleicao.
Cada candidato possui nome e contagem de votos.
O eleitor informa seu CPF, mas o sistema armazena apenas o hash do CPF para garantir
anonimato.
2.Fluxo de votação
O menu principal deve apresentar as opções:
1. Votar
2.Resultado da Eleição
3.Sair
Ao votar, o eleitor informa seu CPF e escolhe um candidato.
O sistema impede que o mesmo eleitor vote mais de uma vez.
Caso o eleitor tente votar novamente, deve aparecer:
Este eleitor já votou.
Caso o candidato não exista, deve aparecer:
Candidato não encontrado.
3. Persistência
Os votos devem ser salvos em um arquivo JSON na pasta Downloads do usuário, de forma
anonimizada (apenas hash do CPF e apuração dos votos).
Ao iniciar o programa, os votos anteriores devem ser carregados automaticamente.
4. Apuração
O sistema deve exibir o resultado da eleição, mostrando a quantidade de votos e o
percentual de cada candidato.
Em caso de empate, o sistema deve informar quais candidatos empataram.'''