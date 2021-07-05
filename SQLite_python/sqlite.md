# SQL

## SQLite

- O SQLite e um banco de dados relacional, ou seja, todas as tabelas de um banco de dados se relacionam com outras tabelas atraves de um compartilhamento de uma chave, ou seja, na tabela "A" temos um campo de nome ID, onde cada registro da quela tabela possui um valor unico detro da coluna daquela tabela, esse campo, chamado de chave primaria.
- O SQLite seria um banco de dados relacional
- Na outra tabela temos um campo que contem o valor de um registro da outra tabela, entao, temos uma outra tabela de nome "B" que possui um campo que armazena um registro que diz qual registro da tabela "A" que o registro da tabela "B" esta apontando, dessa forma temos um relacionamento entre as duas tabelas.
- O que seria um banco de dados?
- Sistema especializado em guarda informações (persistir), como tambem, processar, relacionar e retornar os dados mediante solicitacoes.

## Sistema gerenciador de banco de dados relacional (**SGBDR**)

- Um SGBDR e um sistema especializado em gerenciar uma grande quantidade de informacoes, bem como, o mesmo tem a responsabilidade de adiministra as diversas transacoes realizadas em um mesmo tempo, ou seja, e responsabilidade de um SGBDR estabelecer a ordem de acesso a um registro ou a uma tabela, como tambem, gerenciar quem tem a prioridade a realizar uma determinada transacao como tambem, compete a um SGBDR bloquear um registro ou entao uma tabela quando um cliente assim solicitar, como tambem compete a o SGBDR negar acesso a outros clientes quando um detreminado cliente estiver alterando um determinado registro.

## SQL

### Structured Query Language

- O SQL e uma linguagem universal para manipulacao de banco de dados relacionais. A linguagem hoje e um padrao,
  no entanto, cada banco de dados implementa funcoes nativas.

1. Linguagem declarativa.
2. semelhante a um texto em ingles.
3. Trabalha com um conjunto de registros e nao com um unico.

## Tabelas

- Estrutura formadas por linhas e colunas.
- A tabela e a estrutura fundamental dos bancos de dados relacionais,
  todas as informacoes vai estar imbutido dentro de uma tabela, cada tabela vai possuir um conjunto de atributos
  que chamamos de colunas, entao, um conjunto de colunas forma uma tabela.
- Toda tabela dentro de um banco de dados relacionais vai possuir um nome que a distingue e a torna unica.

EX:

```sql
create table if not exists nome_tabela(
    nome_coluna1 tipo_coluna,
    nome_coluna2 tipo_coluna);
```
