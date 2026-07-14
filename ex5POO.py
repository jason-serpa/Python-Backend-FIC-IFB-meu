'''Você foi contratado para desenvolver um sistema para gerenciar
informações e estatísticas dos clubes participantes da Copa do Mundo
de Clubes da FIFA. Para isso, implemente uma classe abstrata chamada
ClubeParticipante com os atributos nome, pais, confederacao,
ranking_fifa, gols_marcados e vitorias, incluindo um método concreto
exibir_dados() para mostrar os dados do clube, e métodos abstratos
calcular_desempenho() — que deve calcular um índice baseado na
fórmula específica da confederação (para clubes da UEFA: desempenho
= vitórias × 3 + gols marcados × 0,5; para clubes da CONMEBOL:
desempenho = vitórias × 3 + gols marcados × 0,7) — e
gerar_relatorio_tecnico(), que deve exibir as informações básicas do
clube junto com o desempenho calculado. Crie duas subclasses
concretas, ClubeUEFA e ClubeCONMEBOL, que implementem esses
métodos de acordo com as regras definidas, e teste a aplicação criando
instâncias de cada tipo, demonstrando o uso de abstração, herança e
polimorfismo em Python.
'''