from listaDoisEx01 import *
from listaDoisEx02 import *
from listaDoisEx03 import *
from listaDoisEx04 import *
from listaDoisEx05 import *
from listaDoisEx06 import *
from listaDoisEx07 import *
from listaDoisEx08 import *
from listaDoisEx09 import *
from listaDoisEx10 import *
from time import sleep
print('''Ex. 1. 
Crie um programa em Python que recebe um valor em reais e
o converte para outra moeda. Use um menu para escolher a
moeda de destino:
1. Dólar
2. Euro
3. Libra
4. Iene
O programa deve perguntar o valor em reais e exibir o
valor convertido para a moeda escolhida. Use valores
fictícios para as taxas de conversão:
1 Real = 0.19 Dólar
1 Real = 0.17 Euro
1 Real = 0.15 Libra
1 Real = 25 Ienes
======================================================
''')

ex1()
sleep(2)

print('''Ex. 2.
Faça um programa em Python que simula as operações de
um banco. O programa deve apresentar um menu com as
seguintes opções:
1. Depositar (O programa deve pedir o valor a ser
depositado e somá-lo ao saldo)
2. Sacar (O programa deve pedir o valor a ser sacado e
subtrair do saldo, desde que o valor seja menor ou igual
ao saldo disponível)
3. Consultar Saldo (O programa deve exibir o saldo
atual)
4. Sair (O programa termina)
O programa deve manter um saldo inicial de R$ 1000,00
e permitir ao usuário realizar depósitos e saques até que
ele escolha a opção "Sair".
======================================================
''')

ex2()
sleep(2)

print('''Ex. 3. 
Faça um programa em Python que leia dois valores inteiros, x
e y. Por meio de multiplicações sucessivas, calcule e exiba a
função de exponenciação xy
(Obs: quando o valor de y for 0,
não importa o valor de x, o resultado sempre será 1. Utilizar
função).
======================================================
''')

ex3()
sleep(2)

print('''Ex. 4. 
Faça um programa em Python que imprima todos múltiplos de
x, entre 1 e 100, onde x é um número informado pelo usuário.
Utilizar função.
======================================================
''')


ex4()
sleep(2)

print('''Ex. 5. 
Você foi contratado para desenvolver um pequeno sistema de
gerenciamento de uma lista de tarefas pessoais. Escreva um
programa em Python que utilize um menu interativo para
permitir ao usuário as seguintes opções:
1. Adicionar uma nova tarefa
2. Listar todas as tarefas
3. Remover uma tarefa pelo nome
4. Sair do programa
O programa deve manter as tarefas em uma lista e permitir
que o usuário realize várias operações até optar por sair.
Utilizar função.
======================================================
''')
ex5()
sleep(2)

print('''Ex. 6. 
Escreva um programa em Python que simule o controle de
uma sala de cinema. O cinema possui 10 assentos
numerados de 1 a 10, e o programa deve manter uma lista de
ocupação dos assentos (com valores booleanos, onde True
indica ocupado e False indica livre). O usuário poderá
interagir com o sistema por meio de um menu com as
seguintes opções:
1. Reservar um assento
2. Liberar um assento
3. Mostrar mapa de ocupação (exibindo quais assentos
estão ocupados e quais estão livres)
4. Sair
O programa deve impedir a reserva de assentos já ocupados
e a liberação de assentos que já estão livres. Utilizar função.
======================================================
''')

ex6()
sleep(2)

print('''Ex. 7. 
Uma escola aplicou provas em várias turmas e deseja
registrar as maiores notas obtidas por seus alunos. Cada
nota é representada por uma tupla no formato:
(nome_do_aluno, nota, disciplina). Escreva um programa
com o seguinte menu interativo:
1. Adicionar nota: o usuário deve informar o nome do aluno,
a nota (float) e a disciplina, e esses dados devem ser
adicionados como uma nova tupla à lista.
2. Mostrar melhor aluno por disciplina: para cada disciplina
presente na lista, exiba o nome do aluno com a maior nota.
3. Consultar notas por aluno: o usuário digita o nome de um
aluno e o programa mostra todas as notas dele, com a
respectiva disciplina.
4. Exibir notas ordenadas (decrescente): mostre todas as
tuplas da lista ordenadas da maior para a menor nota, no
formato (nota, nome_do_aluno, disciplina).
5. Sair
O programa deve funcionar em laço até que o usuário
escolha a opção de sair. Use tuplas para armazenar as notas
e manipule-as sem alterar sua estrutura original. Utilizar
função.
======================================================
''')

ex7()
sleep(2)

print('''Ex. 8. 
Uma universidade está organizando os dados de participação
dos alunos em dois eventos acadêmicos: uma palestra sobre
Inteligência Artificial e um workshop de Programação em
Python. Os dados de presença são armazenados em dois
conjuntos distintos: palestra_ia e workshop_python, contendo
os nomes dos alunos que participaram de cada evento.
Escreva um programa em Python com o seguinte menu
interativo:
1. Adicionar aluno a um evento: O programa deve perguntar
o nome do aluno e em qual evento ele participou (IA ou
Python) e adicionar o nome ao conjunto correspondente.
2. Mostrar alunos que participaram de ambos os eventos:
Exiba os nomes que aparecem nos dois conjuntos
(interseção).
3. Mostrar alunos que participaram somente da palestra de
IA: Exiba os nomes que estão no conjunto da palestra, mas
não no workshop (diferença).
4. Mostrar alunos que participaram de pelo menos um evento:
Exiba a união dos dois conjuntos, sem repetições.
5. Verificar participação de um aluno: Solicite o nome de um
aluno e diga se ele participou de ambos, somente um ou
nenhum dos eventos.
6. Sair
O programa deve funcionar em laço até que o usuário
escolha a opção de sair. Utilize operações com conjuntos
(union, intersection, difference) para resolver as tarefas.
Utilizar função.
======================================================
''')

ex8()
sleep(2)

print('''Ex. 9. 
Uma livraria quer controlar seu estoque usando um dicionário
onde as chaves são os títulos dos livros e os valores são a
quantidade disponível em estoque. Implemente um programa
com as seguintes funcionalidades:
1. Adicionar um livro ao estoque: o usuário informa o título e a
quantidade (se o livro já existir, some a quantidade nova à
existente).
2. Remover unidades de um livro: o usuário informa o título e
a quantidade a remover; o programa deve atualizar o estoque
e avisar se o estoque ficar zerado ou se o livro não existir.
3. Consultar quantidade de um livro: o usuário digita o título e
o programa mostra a quantidade disponível ou informa que o
livro não está no estoque.
4. Mostrar todos os livros com suas quantidades ordenados
alfabeticamente.
5. Sair
O programa deve repetir o menu até que o usuário escolha
sair. Utilizar função.
======================================================
''')


ex9()
sleep(2)

print('''Ex. 10. 
Você foi contratado para desenvolver um sistema simples
para gerenciar um campeonato de futebol. O sistema deve
usar um dicionário onde as chaves são os nomes dos times e
os valores são os pontos conquistados. O programa deve
apresentar o seguinte menu:
1. Adicionar time: permite cadastrar um novo time com 0
pontos iniciais.
2. Registrar resultado de partida: o usuário informa os nomes
de dois times e o resultado da partida (quantidade de gols de
cada time). O programa atualiza os pontos dos times: 3
pontos para o vencedor, 1 ponto para empate, 0 para o
perdedor.
3. Mostrar classificação: exibe a lista dos times e seus
pontos, ordenada do maior para o menor número de pontos.
4. Remover time: permite remover um time da competição.
5. Sair
O programa deve funcionar em loop até o usuário escolher
sair. Utilizar função.
======================================================
''')

ex10()
