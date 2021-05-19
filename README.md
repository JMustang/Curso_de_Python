# Curso de python

## **Função print:**

- Através da função print, nos podemos enviar parâmetros,

- Devem estar contidas obrigatoriamente entre os parênteses

```py
print("parâmetros")
```

## **Comentarios em Python.**

- Como inserir comentários no meio do código?

```py
# isso e um comentario.
# não sera interpretado pelo copilador.
```

## **Variaveis.**

- O que e uma variável?
- Variável e um local na memoria que nos reservamos para armazenar uma informação (um valor).
- em python toda toda variável que criarmos \*tera um tipo implícito atribuído a ela.

- Características de variáveis

1. toda variável tem um nome.
2. toda variável tem um tipe.
3. toda variável tem tamanho.
4. toda variável tem um valor.

Em python ficaria assim:

```py
# Características das Variáveis.

# int
a = 10
# float
b = 1.2
# string (tudo que for posto entre aspas sera interpretado pelo python como uma string)
msg = "mensagem"
# boolean
verdade = false

# Programa simples usando a função print e as variáveis.

nome = "junior"
print(nome)

numb = 10
print (numb)

verdadeiro = false
print (verdadeiro)
```

- para definimos uma variável no python basta atribuímos um valor a um determinado nome.

## **Nomenclatura das Variáveis.**

- Ha regras para nomes de variáveis, métodos e classes

- as variáveis devem se com letras menusculas e nomes compostos devem ser separados por \_ underline.

- Pode ter números mas não deve iniciar com números ou carácter especial, o único aceito seria o \_ underline.

EX:

```py
meu_nome_e_bem_grande = “nome”

```

## **Pacote/modulo**

- usar nomes pequenos.
- utilizar caracteres minúsculos.

EX:

```py
- OS
- package

```

## **Classes**

- iniciar com letra maiúscula.
- nomes compostos com ambas palavras em maiuscula.

EX:

```py
- LetraMaiuscula
- NomeDaClasse

```

## **Funções/métodos**

- letras menus culas.
- nomes compostos unidos por \_ underline

EX:

```py
- utilizar_underline()
- enviar_email()

```

## **Constantes.**

- letras maiúsculas.
- nomes compostos unidos por \_ underline

EX:

```py
- PI
- VALOR_MÁXIMO

```

## **Parâmetro de função.**

- letras minusculas.
- nomes compostos unidos por \_ underline

EX:

```py
- enviar(nome_do_arquivo)
- receber(self)

```

## **Concatenar dados**

- Concatenar seria juntar dois tipos de dados diferentes.
- Para concatenar dados em python pode ser feito
  com o sinal de "+" ou com uma ",".

EX:

```py
nome = "junior"
print("Ola " + nome)
# ou
print("Ola ", nome)
```

## **Entrada de dados.**

- Entrada de dados utilizando input()

EX:

```py
# programa de login e senha
login = input("Digite seu login: ")
senha = input("digite sua senha: ")
print(login)
print(senha)
print("Ola ", login)
```

# **Operações matemáticas**

- Trabalhar com matemática no python não poderia ser mais simples.
- A o longo dos anos a linguagem python tem sido a queridinha dos cientistas.

Somar:

```py
somar = 10 +10
print(somar)
```

subtrair:

```py
subtrair = 10 -10
print(subtrair)
```

multiplicar :

```py
multiplicar= 10 *10
print(multiplicar)
```

dividir:

```py
dividir = 10 /10
print(dividir)
```

# **Modulo de divisão**

- como obter o modulo de uma divisão?(o resto da divisão)
- Para esses casos, temos um operador para nos auxiliar.
- Toda vez que precisarmos obter o resto da divisão vamos utilizar o sinal de “%” porcentagem.

EX:

```py
resto = 3%2
print(resto)
```

# **Potenciação e radiciação**

- Não seria necessário um loop para saber a potencia de um numero,
  pois o python trás nativamente esse recurso, isso que faz essa linguagem se destacar dentre
  outras linguagens, então se queremos saber o quadrado de um numero basta
  informar o numero e usar o operador de potenciação.

EX:

```py
# se quisermos elevar 5 ao quadrado.
5**2
```

“\*\*” asterisco, asterisco seria mais um operador composto que utilizamos para obter a potencia de um numero.

# **Operadores relacionais**

- Na programação e muito comum averiguar condições e assim
  baseado em uma condição nos mudamos o fluxo do nosso programa,
  ou seja, temos que testar o estado da variável como também dos dados que estão sendo
  digitado pelo usuário para que possamos tomar a atitude correta todo instante,
  vamos nos valer de vários conceitos lógicos matemáticos, trabalhando com os operadores condicionais, basicamente os operadores são divididos em duas categorias .
  Operadores de igualdade e os operadores relacionais.
  Toda condição logica obrigatoriamente resultara em verdadeiro ou falso (true, false).
  (valores booleanos, condições logicas).

EX:

```py
( x == y) → x igual a y.
(x != y) → x diferente de y.

(5<5.1)or(5==5.1)

'a'=='a'
# true
"a"=="b"
# false
'a'!='b'
# true
```

# **Tomada de decisoes**

- Utilizando as tomadas de decisões para altera o
  fluxo do programa.

EX:

```py
( x == y) → x igual a y.
(x != y) → x diferente de y.

Num = 100

if Num =+ 100 :
print(condição verdadeira)
else:
print(condição falsa)
```

Com a instrução “if” nos podemos fazer o nosso programa ter um polco de inteligencia.

EX:

```py
# Estrutura de seleção única.
# aqui a instrução ‘if’ testa se a condição
# entre parênteses “true” e verdadeira,
# sendo verdadeira o bloco que esta
# depois da instrução “if” sera executado “facaIsso()”

if (true)
	facaIsso()

# Estrutura de seleção dupla.

if(true)
	facaIsso()
else
	facaAquilo()

# Outra estrutura de seleção dupla.
# Nesse caso o programa ira testa se a primeira condição e verdadeira
# se não for o programa ira pular para a segunda condição e
# testa a segunda.


if(true)
	facaIsso()
elif(false)
	facaAquilo()

# estrutura de seleção múltipla
# uma variável pode ter vários valores
# assim podemos testar múltiplas vezes a mesma variável
# ou seja, seria o mesmo de ter varias estruturas “if”
# porem elas estao agrupadas de uma forma diferente

switch(valor)
	caso 1: facaIsso()
	caso 2: facaAquilo()
	caso 3: facaIssoEAquilo()
```

# **Depuração**

- Oque seria depuração?
- Basicamente seria uma forma de executarmos um programar e acompanharmos a execução linha por linha a procura de bugs.
- Por vezes empregado no intuito de descobrir erros, em outras, com a finalidade de entender o funcionamento.

# **Operações relacionais compostas**

- Existem quatro operadores relacionais.
- com eles podemos fazer qualquer comparativo
  então toda vez que for necessário comparar dois valores
  basta usar um desses quatro operadores.

```py
> #maio que
< #menor que
>= #maior ou igual que
<= #menor ou igual que
```

- um exemplo pratico seria.

```py
idade = int(input(‘informe sua idade’))
	if(idade<=0):
		print(“A sua idade não pode ser 0 ou menor do que 0!”)
	elif(idade>150):
			print(“A sua idade não pode ser maior que 150 anos!)
	elif(idade<18):
				print(“Você precisa ter mais do que 18 anos!”)
```

# **Operadores lógicos.**

- A forma mais fácil e talvez a mais logica de testarmos
  varias condições a o mesmo tempo seria usando instruções “if”
  dentro de outras instruções “if” porem instruções “if” aninhadas nem sempre atendem as nossas necessidades e pode nos obrigar a duplicar código, sem contar e a legibilidade do código fica comprometida, existe a necessidade de simplificarmos as condições
  e uma forma de fazermos isso seria utilizando os operadores lógicos.
  A principio seria bastante simples, porem quando temos uma situação que temos que usar vários operadores uma expressão pode acabar bastante complexa, temos que buscar sempre a melhor forma de usar os
  operadores abaixo.

```py
# and – e
# or – ou
# not – negação
# is – é
# is not – não é
# in – esta contido
# not in – não esta contido

# exemplo pratico

2<4 and 2==4

2>4 or 2<4

not (2>4 or 2<4)

2 is 2

type (2) is int
```

# **Bloco de instruções**

- Um bloco de instrução é o conjunto de funções que sera executada sequencialmente uma após a outra.
- bloco de instruções no python simplesmente colocamos nossas instruções com o mesmo espaçamento e assim é definido um bloco de instrução no python.

EX:

```py
# isso é um bloco de instrução no python

if(true):
print(“Imprime um texto”)
```

- no python não é necessário uso de delimitadores de instrução,
- também não exite a necessidade de uso de “;” ponto e virgula.
