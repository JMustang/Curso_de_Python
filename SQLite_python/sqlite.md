# SQL

## SQLite

- O SQLite e um banco de dados relacional, ou seja, todas as tabelas de um banco de dados se relacionam com outras tabelas através de um compartilhamento de uma chave, ou seja, na tabela "A" temos um campo de nome ID, onde cada registro da quela tabela possui um valor único dentro da coluna daquela tabela, esse campo, chamado de chave primaria.
- O SQLite seria um banco de dados relacional
- Na outra tabela temos um campo que contém o valor de um registro da outra tabela, então, temos uma outra tabela de nome "B" que possui um campo que armazena um registro que diz qual registro da tabela "A" que o registro da tabela "B" está apontando, dessa forma temos um relacionamento entre as duas tabelas.
- O que seria um banco de dados?
- Sistema especializado em guarda informações (persistir), como também, processar, relacionar e retornar os dados mediante solicitações.

## Sistema gerenciador de banco de dados relacional (**SGBDR**)

- Um SGBDR e um sistema especializado em gerenciar uma grande quantidade de informações, bem como, o mesmo tem a responsabilidade de administra as diversas transações realizadas em um mesmo tempo, ou seja, e responsabilidade de um SGBDR estabelecer a ordem de acesso a um registro ou a uma tabela, como também, gerenciar quem tem a prioridade a realizar uma determinada transação como também, compete a um SGBDR bloquear um registro ou então uma tabela quando um cliente assim solicitar, como também compete à o SGBDR negar acesso a outros clientes quando um determinado cliente estiver alterando um determinado registro.

## SQL (Structured Query Language)

- O SQL e uma linguagem universal para manipulação de banco de dados relacionais. A linguagem hoje e um padrão,
  no entanto, cada banco de dados implementa funções nativas.

1. Linguagem declarativa.
2. semelhante a um texto em ingles.
3. Trabalha com um conjunto de registros e não com um único.

## Tabelas

- Estrutura formadas por linhas e colunas.
- A tabela e a estrutura fundamental dos bancos de dados relacionais,
  todas as informações vão estar embutido dentro de uma tabela, cada tabela vai possuir um conjunto de atributos
  que chamamos de colunas, então, um conjunto de colunas forma uma tabela.
- Toda tabela dentro de um banco de dados relacionais vai possuir um nome que a distingue e a torna unica.

EX:

```SQL
create table if not exists nome_tabela(
    nome_coluna1 tipo_coluna,
    nome_coluna2 tipo_coluna);
```
