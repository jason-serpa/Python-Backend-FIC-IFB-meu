Bancos de dados são conjuntos de registros dispostos em estrutura regular que possibilita a reorganização dos mesmos e produção de informação.
- Criar uma estrutura
- Armazenar dados
- Recuperar informações
Sua organização segue um modelo de dados, que pode ser: <b>relacional</b>, objeto, objeto relacional, hierárquico, redes, espaciais, multimídia e NOSQL

Um banco de dados é uma coleção de dados relacionados
Um banco de dados é uma coleção lógica e coerente de dados com algum significado inerente.
Um banco de dados é projetado, construído e povoado por dados, atendendo a uma proposta específica. 
Possui um grupo de usuários definido e algumas aplicações preconcebidas, de acordo com o interesse desse grupo de usuários.


No modelo relacional, as estruturas têm a forma de tabelas, compostas por tuplas (linhas) e colunas.

<b>Dado:</b> menor unidade identificável que tem algum significado no mundo real, também chamado de <i>coluna</i> ou <i>atributo</i>.
- EX: nome, cor, valor, ID etc.

<b>Registro</b>: grupo de dados relacionados, tratados como uma entidade isolada por uma aplicação, também chamado de <i>linha</i> ou <i>tupla</i>;
- EX: PRODUTO – descrição, marca, valor, unidade etc    

<b>Tabela:</b> é uma coleção de registros de um mesmo tipo;



<h1>Ciclo de Vida do DB</h1>

1: <b>Análise de Requisitos:</b> Coleta de informações e regras.

2: <b>Projeto Lógico:</b> Um diagrama de modelo de dados conceitual contendo os dados seus relacionamentos (DER).
- Modelagem de dados conceitual, Integração da visão, Transformação do modelo de dados conceitual em tabelas e Normalização de tabelas.

3: <b>Projeto Físico:</b> Construção do Banco de Dados.

4: <b>Implementação, Monitoração e Modificação do BD:</b> Finalização do Projeto de Banco de Dados.



</h1>Sistemas gerenciados de BD (SGBD)</h1>

São softwares que permitem a definição de estruturas para armazenamento de informações e fornecimento de mecanismos para manipulá-las.
- Seu principal objetivo é retirar da aplicação cliente a responsabilidade de gerenciar o acesso, a manipulação e a organização dos dados.
- Disponibiliza uma interface para que seus clientes possam incluir, alterar ou consultar dados previamente armazenados.

É uma coleção de programas que permite aos usuários criar e manter uma banco de dados. O SGBD é portanto, um sistema de software de propósito geral que facilita os processos de definição, construção, manipulação, e compartilhamento de bancos de dados entre vários usuários e aplicações.


Características de um SGBD:
- Controle de redundância: A repetição dos dados deve ser evitada para se minimizar possibilidades de inconsistências;

- Compartilhamento de dados: Em um ambiente multi-usuários deve-se possibilitar a manipulação simultânea de dados distintos ou dos mesmos dados conforme algumas regras.

- Controle de acesso: Verificação automática do tipo de acesso pedido por cada usuários, níveis de segurança e identificações de cada usuário (login/senha);

- Controle de transação: Transação é o conjunto de operações que devem ser executadas completamente, são normalmente usadas em situações críticas (atualizações/inclusões)
de longa duração, que podem afetar a consistência do BD. O SGBD deve utilizar mecanismos internos para que nenhuma falha ocorra durante a execução da transação;

- Acesso a múltiplas interfaces: Possibilidade de usar diversas interfaces mesmo se o SGBD estiver sendo utilizado;

- Restrições de integridade: Estabelecimento de um formato para os dados inseridos de modo a garantir uma certa integridade e facilitar o armazenamento.

- Backup e recuperação: Estabelecer o backup automático do BD total ou parcial em momentos estabelecidos pelo DBA, proporciona proteção contra a perda de informações devido a falhas no dispositivo de armazenamento.

- Independência de dados: A descrição física dos arquivos é mantida internamente pelo SGBD e é de sua responsabilidade e exclusividade. Programas aplicativos não dispõeem da descrição física e sim de descrição externa.

- Indexação automática: Com a indicação explícita dos atributos que serão mais utilizados em consultas, o SGBD cria os arquivos de indexação que tornarão mais rápidas as pesquisas. A estrutura de indexação e de organização dos arquivos de dados é próprio de cada SGBD e normalmente não é de domínio dos usuários comuns.



<h>Motivação para o uso de um SGBD</h>

- Consistência de dados e independência de dados;
- É a ferramenta por excelência para promover a integração dos diversos componentes de um sistema de software;
- Concentram o maior potencial para promover aceso compartilhado de informação, sem bloquear desnecessariamente o acesso compartilhado;
- Retiram dos programas aplicativos muita da complexidade de gerenciamento de estruturas de acesso aos dados;
- Facilitam a proteção contra a perda de dados, através de recursos de backup;
- Promovem a adoção de padrões para toda a empresa, facilitando seu emprego..


