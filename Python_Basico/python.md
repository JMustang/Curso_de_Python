# Curso de python

## **Função print**

- Através da função print, nos podemos enviar parâmetros,

- Devem estar contidas obrigatoriamente entre os parênteses

```py
print("parâmetros")
```

## **Comentários em Python.**

- Como inserir comentários no meio do código?

```py
# isso é um comentário.
# não vai ser interpretado pelo compilador.
```

## **Variáveis. **

- O que é uma variável?
- Variável é um local na memória que nos reservamos para armazenar uma informação (um valor).
- Em python toda variável que criarmos \*tera um tipo implícito atribuído a ela.

- Características de variáveis

1. toda variável tem um nome.
2. toda variável tem um tipo.
3. toda variável tem tamanho.
4. toda variável tem um valor.

Em python ficaria assim:

```py
# Características das Variáveis.

# Int
a = 10
# Float
b = 1.2
# string (tudo que for posto entre aspas sera interpretado pelo python como uma string)
msg = "mensagem"
# Boolean
verdade = false

# Programa simples usando a função print e as variáveis.

nome = "junior"
print(nome)

numb = 10
print (numb)

verdadeiro = false
print (verdadeiro)
```

- Para definimos uma variável no python basta atribuímos um valor a um determinado nome.

## **Nomenclatura das Variáveis. **

- Ha regras para nomes de variáveis, métodos e classes

- As variáveis devem se com letras minúsculas e nomes compostos devem ser separados por \_ underline.

- Pode ter números, mas não deve iniciar com números ou carácter especial, o único aceito seria o \_ underline.

EX:

```py
meu_nome_e_bem_grande = “nome”

```

## **Pacote/modulo**

- Usar nomes pequenos.
- Utilizar caracteres minúsculos.

EX:

```py
- OS
- package

```

## **Classes**

- Iniciar com letra maiúscula.
- Nomes compostos com ambas palavras em maiúscula.

EX:

```py
- LetraMaiuscula
- NomeDaClasse

```

## **Funções/métodos**

- Letras minúsculas.
- Nomes compostos unidos por \_ underline

EX:

```py
- utilizar_underline()
- enviar_email()

```

## **Constantes. **

- Letras maiúsculas.
- Nomes compostos unidos por \_ underline

EX:

```py
- PI
- VALOR_MÁXIMO

```

## **Parâmetro de função. **

- Letras minúsculas.
- Nomes compostos unidos por \_ underline

EX:

```py
- enviar(nome_do_arquivo)
- receber(self)

```

## **Concatenar dados**

- Concatenar é juntar dois tipos de dados diferentes.
- Para concatenar dados em python pode ser feito
  com o sinal de "+" ou com uma ",".

EX:

```py
nome = "junior"
print ("Ola " + nome)
# ou
print ("Ola ", nome)
```

## **Entrada de dados. **

- Entrada de dados utilizando input ()

EX:

```py
# programa de login e senha
login = input ("Digite seu login: ")
senha = input ("digite sua senha: ")
print(login)
print(senha)
print ("Ola ", login)
```

## **Operações matemáticas**

- Trabalhar com matemática no python não poderia ser mais simples.
- Ao longo dos anos a linguagem python tem sido a queridinha dos cientistas.

Somar:

```py
somar = 10 + 10
print(somar)
```

subtrair:

```py
subtrair = 10 - 10
print(subtrair)
```

multiplicar:

```py
multiplicar= 10 * 10
print(multiplicar)
```

dividir:

```py
dividir = 10 / 10
print(dividir)
```

## **Modulo de divisão**

- Como obter o modulo de uma divisão? (o resto da divisão)
- Nesses casos, temos um operador para nós auxiliar.
- Toda vez que precisarmos obter o resto da divisão vamos utilizar o sinal de “%” porcentagem.

EX:

```py
resto = 3%2
print(resto)
```

## **Potenciação e radiciação**

- Não é necessário um loop para saber a potência de um numero,
  pois o python trás nativamente esse recurso, isso que faz essa linguagem se destacar dentre
  outras linguagens, então se queremos saber o quadrado de um numero basta
  informar o número e usar o operador de potenciação.

EX:

```py
# se quisermos elevar 5 ao quadrado.
5**2
```

“\*\*” asterisco, asterisco é mais um operador composto que utilizamos para obter a potência de um número.

## **Operadores relacionais**

- Na programação e muito comum averiguar condições e assim
  baseado em uma condição nos mudamos o fluxo do nosso programa,
  ou seja, temos que testar o estado da variável como também dos dados que estão sendo
  digitado pelo usuário para que possamos tomar a atitude correta todo instante,
  vamos nos valer de vários conceitos lógicos matemáticos, trabalhando com os operadores condicionais, basicamente os operadores são divididos em duas categorias.
  Operadores de igualdade e os operadores relacionais.
  Toda condição logica obrigatoriamente resultara em verdadeiro ou falso (true, false).
  (valores booleanos, condições logicas).

EX:

```py
(x == y) → x igual a y.
(x! = y) → x diferente de y.

(5<5.1) or (5==5.1)

'a'=='a'
# True
"a"=="b"
# False
'a'! ='b'
# True
```

## **Tomada de decisões**

- Utilizando as tomadas de decisões para altera o
  fluxo do programa.

EX:

```py
(x == y) → x igual a y.
(x! = y) → x diferente de y.

Num = 100

if Num =+ 100:
print (condição verdadeira)
else:
print (condição falsa)
```

Com a instrução “if” nós podemos fazer o nosso programa ter um polco de inteligência.

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
# Nesse caso o programa vai testa se a primeira condição e verdadeira
# se não for, o programa vai pular para a segunda condição e
# testa a segunda.


if(true)
	facaIsso()
elif(false)
	facaAquilo()

# estrutura de seleção múltipla
# uma variável pode ter vários valores
# assim podemos testar múltiplas vezes a mesma variável
# ou seja, seria o mesmo de ter várias estruturas “if”
# porem elas estão agrupadas de uma forma diferente

switch(valor)
	caso 1: facaIsso()
	caso 2: facaAquilo()
	caso 3: facaIssoEAquilo()
```

## **Depuração**

- O que é depuração?
- Basicamente, é uma forma de executarmos um programar e acompanharmos a execução linha por linha a procura de bugs.
- Por vezes empregado no intuito de descobrir erros, em outras, com a finalidade de entender o funcionamento.

## **Operações relacionais compostas**

- Existem quatro operadores relacionais.
- Com eles, podemos fazer qualquer comparativo
  então, toda vez que for necessário comparar dois valores,
  basta usar um desses quatro operadores.

```py
> #maio que
< #menor que
>= #maior ou igual que
<= #menor ou igual que
```

- Um exemplo prático.

```py
idade = int(input (‘informe sua idade’))
	if(idade<=0):
		print (“A sua idade não pode ser 0 ou menor do que 0!”)
	elif(idade>150):
			print (“A sua idade não pode ser maior que 150 anos!)
	elif(idade<18):
				print (“Você precisa ter mais do que 18 anos!”)
```

## **Operadores lógicos. **

- A forma mais fácil e talvez a mais logica de testarmos
  várias condições a o mesmo tempo é usando instruções “if”
  dentro de outras instruções “if” porem instruções “if” aninhadas nem sempre atendem as nossas necessidades e pode nos obrigar a duplicar código, sem contar e a legibilidade do código fica comprometida, existe a necessidade de simplificarmos as condições
  e uma forma de fazermos isso seria utilizando os operadores lógicos.
  A princípio seria bastante simples, porém quando temos uma situação que temos que usar vários operadores uma expressão pode acabar bastante complexa, temos que buscar sempre a melhor forma de usar os
  operadores abaixo.

```py
# and – e
# or – ou
# not – negação
# is – é
# is not – não é
# in – está contido
# not in – não está contido

# exemplo prático

2<4 and 2==4

2>4 or 2<4

not (2>4 or 2<4)

2 is 2

type (2) is int
```

## **Bloco de instruções**

- Um bloco de instrução é o conjunto de funções que sera executada sequencialmente uma após a outra.
- Bloco de instruções no python simplesmente colocamos nossas instruções com o mesmo espaçamento e assim é definido um bloco de instrução no python.

EX:

```py
# isso é um bloco de instrução no python

if(true):
print (“Imprime um texto”)
```

- No python não é necessário uso de delimitadores de instrução,
- Também não existe a necessidade de uso de “;” ponto e vírgula.

- Um bloco de instrução também garante uma maior segurança na manipulação das variáveis.
- Uma variável que é criada dentro de um bloco só pode ser acessada ali dentro
  assim se tentarmos acessar a variável fora do bloco o compilador ou irá levantar uma exceção ou irá tratar essa variável como uma variável independente que não tem relação alguma com a variável que está dentro do bloco.

EX:

```py
if(true):
	a = 50

# a variável “a” não sera impressa.
print (a)
```

EX:

```py
a = 25
if(true):
	a = 50

# a variável “a” sera impressa, pois a foi declarado fora do bloco de “if”.
print (a)
```

## **Escopo**

- Um escopo na programação são as regiões onde uma determinada variável pode ser acessada.
- Variáveis no cabeçalho do código são chamadas de variáveis globais,
  pois elas podem ser acessadas dentro de qualquer bloco de instrução.

EX:

```py
# Essas são variáveis globais
# pois são declaradas fora dos blocos, no escopo global
a = 1
b = 2

def soma_num(var1, var2):
	s = var1 + var2
	return

def imprime(x_vezes):
	for i in range(x_vezes):
		print(i)

print (soma_num(a, b))
print (5)
```

## **Operadores de atribuição**

- Atribuição,
- O valor ao lado direito do operador sera atribuído a variável a esquerda do operador

```py
valor_a_esquerda = valor_a_direita
```

## **Atribuição múltipla**

- Atribuição múltipla seria a capacidade de atribuir valores diferentes a variáveis distintas numa mesma instrução.
- Grosseiramente falando, seria uma forma rápida de atribuir valores as variáveis.

EX:

```py
a, b, c = 5, 7, 9

s1, s2 = “curso”, “python”

# Trocando valores em variáveis
a, b = b, a

```

## **Operadores de atribuição compostos**

- Esses atalhos matemáticos nos proporciona uma melhor estética do nosso código como também faz o nosso código ser executado de maneira mais rápida pois quando utilizamos esses operadores existe um processo de otimização

EX:

```py
+= → (x += y) = 12
-= → (x -= y) = 6
*= → (x *= y) = 27
/= → (x /= y) = 3
%= → (x %= y) = 0
```

## **Atribuição condicional**

- Atribuição condicional seria uma estrutura utilizada para simplificar o código, onde o valor a ser atribuído sera aquele que satisfizer a condição.

EX:

```py
<variável> = <valor1> if (true) else <valor2>

var = 10 if (true) else 20
```

## **Iteração**

- Iteração, laços condicionais, looping é o processo de repetição onde um bloco de instrução sera executado enquanto uma condição for atendida.
- Os laços condicionais fazem parte do tópico de controle de fluxo no estudo da linguagem de programação.
- É uma forma de fazer que um bloco de instrução seja repetido enquanto uma condição for verdadeira.

EX:

```py
# laço “for”
nome = [‘Alice’, ‘Murilo’, ‘yoriki’]
for n in nomes:
	print(n)
else:
	print (“Todos os nomes foram listados com sucesso!”)
```

EX:

```py
while (x<=10):
  print(x)
```

## **Laços de repetição**

- Este processo se repetirá enquanto a condição for verdadeira. Quando esta for falsa, o fluxo de execução prosseguirá pela instrução seguinte ao Fim_enquanto.

EX:

```py
x = 0
while (x <= 10):
	print(x)
	x += 1
```

## **While else**

EX:

```py
x = 0
while (x<10):
	print (x)
	x=x+1;
else:
	print(“else”)
```

## **for loop**

EX:

```py
for c in “palavra”:
	print(c)
```

## **função range**

- A função range sera usada todas as vezes que for necessário gerar uma lista que contenha uma seria de números em um intervalo determinado.
- Na maior parte das vezes iremos usar a função “range” junto com a instrução “for” porem a função “range” não se limita somente a instrução “for”, nós podemos invocar a função “range” todas as vezes em que for preciso criar uma sequência numérica num determinado intervalo

```py
range([start], stop [, step])
```

EX:

```py
arr = list (range (0, 10, 2))
print(arr)
```

```py
# Usando a função “for”
for i in range (10, 0, 1):
	print(i)
```

## **Instrução Break**

- A instrução **Break** interrompe a execução do laço de repetição onde está contido.

EX:

```py
for i in range (10):
	if(true):
		beak
```

EX:

```py
while (i<100):
	i=i+1
	if(true):
		break
```

EX:

```py
# exemplo prático para ter uma noção de como seria importante
# a função **Break** em um código

print (“Antes de entrar no laço”)
for item in range (10):
	print(item)
	if(item==6):
		break
print (“Depois de ter entrado no laço”)
```

## **Instrução Continue**

- A instrução **Continue** interrompe a execução de um único ciclo. Enquanto a instrução **Break** interrompe todos os ciclos de um laço de repetição, a instrução **Continue** finaliza somente o ciclo que está sendo executado.

EX:

```py
for i in range (10):
	if(true):
		continue
```

EX:

```py
while(i<100):
	i=i+1
	if(true):
		continue
```

EX:

```py
# exemplo prático para ter uma noção de como seria importante
# a função **Continue** em um código.

print(“Inicio”)
i = 10
while(i<10):
	i+=1
	if(i%2==0):
		continue
	print(i)
else:
	print(“else”)
print(“Fim”)
```

## **Estrutura de dados – Listas**

### Introdução a estrutura de dados.

- Estrutura de dados é qualquer meio utilizado para armazenar e recuperar informações.
- A lista considerada a principal e a mãe de todas as outras estruturas.
- Estrutura de dados mutáveis onde a ordenação natural seria estabelecida pela ordem de entrada. O último item de uma lista não ordenada **SEMPRE** sera o último elemento adicionado.

## **Estrutura de dados – Listas, Pilhas, Array, Set**

### Principais estruturas

- LISTA
- PILHA
- ARRAY/MATRIZ/VETOR
- TUPLA
- SET (grupo)
- DICIONARIO
- ARVORE

### PILHA (stack)

- Pilha é o conjunto de objetos/elementos adicionados um sobre o outro.

**NORMAL GERAL: **

1. O último a entrar sera o primeiro a sair.
2. O primeiro a entrar sempre sera o último elemento da lista.

- Estrutura de dados mutável onde a ordenação natural seria estabelecida pela ordem de entrada. O primeiro item da pilha SEMPRE sera o ultimo adicionado

### ARRAY

- Array é uma estrutura de dados estática para a manipulação de um número finito de elemento de um mesmo tipo.

- Array é constituído por um conjunto de elementos finitos e definidos na sua declaração.

1. O índice 0 é o primeiro elemento.
2. O índice do último elemento é o “total_de_itens -1”.

Array, não muito utilizado no python.

### TUPLA

- Estrutura de dados que possui todas as características de uma lista porem, imutável. A Tupla pode conter 0 ou ‘n’ elementos e estes não poderão ser alterados.

- Tupla é uma lista declarada como uma constante.

1. Não é possível adicionar, remover, altera elementos.
2. Toda tupla é um conjunto de objetos, e estes, também são imutáveis. Assim, se adicionarmos o número 10 a posição “1” da Tupla, não sera possível atribuir outro valor na posição “1”.

### SET (conjunto)

- Estruturas de dados semelhante a uma lista. Um set tem como princípio conter uma lista de valores diferentes.
- Set é uma lista sem itens repetidos.

### DICIONARIO

- Estrutura de dados onde cada elemento está associado a uma chave que pode ser de qualquer tipo.
- Cada item do dicionário possui uma chave única. Essa, seria por definição diferente de todas as outras

### ARVORE

- Estrutura de dados dispostas em uma hierarquia. A estrutura de diretórios do nosso computador seria uma arvore.

NORMA GERAL:

1. Raiz – elemento pertencente a o nível um. Toda arvore tera sempre uma única raiz.
2. no/filho – elemento que foi adicionado a outro item.
3. Nível – propriedade que indica quantos nos estão acima de um filho.

## **Class List I**

### LISTA (list)

- Estrutura de dados mutável onde a ordenação natural seria estabelecida pela ordem de entrada. O último item de uma lista não ordenada SEMPRE sera o último elemento adicionado.

- Lista seria qualquer sequência de objetos/elementos em qualquer ordem. Todas as estruturas de dados são também listas.

**NORMA GERAL: **

1. Novos itens SEMPRE serão adicionados após o último item.

2. O primeiro item adicionado à lista SEMPRE serão o primeiro elemento da estrutura.

EX:

```py
# tudo que estiver entre colchetes sera entendido pelo python como uma list.
lista = [1,2,8,5,15,3,6,8,]
print(lista)

# isso também é uma list.
type([‘casa’,1,’23’])
```

## **Class List II**

- Uma lista é um objeto e cada elemento é um objeto também.
- Podemos ter em uma lista objetos de tipos diferentes, tanto strings como objetos numéricos.

EX:

```py
list = [‘casa’,10,” house”]

# Isso também e uma lista.
# uma lista com três objetos que também são listas
list2 = [[], [],[]]
list3 = [[“a”,”b”,”c”], [1,1,2,3,], []]
```

### Estruturas de dados

- Esse capítulo descreve algumas coisas que você já aprendeu em detalhes e adiciona algumas coisas novas também.

**Mais sobre listas**

- O tipo de dado lista tem ainda mais métodos. Aqui estão apresentados todos os métodos de objetos do tipo lista:

1. list.append(x)

- Adiciona um item ao fim da lista. Equivalente a a[len(a):] = [x].

2. list.extend(iterable)

- Prolonga a lista, adicionando no fim todos os elementos do argumento iterable passado como parâmetro. Equivalente a a[len(a):] = iterable.

3. list.insert(i, x)

- Insere um item em uma dada posição. O primeiro argumento é o índice do elemento antes do qual será feita a inserção, assim a.insert(0, x) insere um elemento na frente da lista e a.insert(len(a), x) e equivale a a.append(x).

4. list.remove(x)

- Remove o primeiro item encontrado na lista cujo valor é igual a x. Se não existir valor igual, uma exceção ValueError é levantada.

5. list.pop([i])

- Remove um item em uma dada posição na lista e o retorna. Se nenhum índice é especificado, a.pop() remove e devolve o último item da lista. (Os colchetes ao redor do i na demonstração do método indica que o parâmetro é opcional, e não que é necessário escrever estes colchetes ao chamar o método. Você verá este tipo de notação frequentemente na Biblioteca de Referência Python.)
  6)list.clear()
- Remove todos os itens de uma lista. Equivalente a del a [:].
  list.index(x [, start [, end]])
  Devolve o índice base-zero do primeiro item cujo valor é igual a x, levantando ValueError se este valor não existe.
  Os argumentos opcionais start e end são interpretados como nas notações de fatiamento e são usados para limitar a busca para uma subsequência específica da lista. O índice retornado é calculado relativo ao começo da sequência inteira e não referente ao argumento start.

7. list.count(x)

- Devolve o número de vezes em que x aparece na lista.
  list.sort(\*, key=None, reverse=False)
  Ordena os itens na lista (os argumentos podem ser usados para personalizar a ordenação, veja a função sorted() para maiores explicações).

8. list.reverse()

- Inverte a ordem dos elementos na lista.

9. list.copy()

- Devolve uma cópia rasa da lista. Equivalente a a[:].
  Um exemplo que usa a maior parte dos métodos das listas:

```py
 fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
 fruits.count('apple')
2

 fruits.count('tangerine')
0

 fruits.index('banana')
3

 fruits.index('banana', 4) # Find next banana starting a position 4
6

 fruits.reverse()
 fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
 fruits.append('grape')
 fruits

['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
 fruits.sort()
 fruits

['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
 fruits.pop()
'pear'
```

## **Class List III**

EX:

```py
lista = [1,2,3,4,5]

# adicionando um elemento novo no final da lista

lista = lista + [6]
print (lista)

# adicionando um elemento novo ao fim da lista

lista = [0] + lista
print (lista)

# concatenando duas listas

lista = lista + [7,8,9, 10]
print (lista)

# função append(), adiciona um novo elemento a lista

lista.append(11)
print(lista)

# função del() deleta um elemento da lista

del(lista[-1])
print(lista)

```

## **Iterando listas**

- Iterar, percorrer todos os itens de uma array.

EX:

```py
# dessa forma não funciona.
lista_nums = [100,200,300,400]
for item in lista_nums:
	item += 1000
	print(item)
```

EX:

```py
# Somando um valor a cada item do array.
lista_nums = [100,200,300,400]
lista_indice = [0,1,2,3]
for item in lista_indice:
	lista_nums [item] += 1000
	print(lista_nums)
```

EX:

```py
# Somando um valor a cada item do array.
lista_nums = [100,200,300,400,500]
# usando a função range
lista_indice = range (5)
for item in lista_indice:
	lista_nums [item] += 1000
	print(lista_nums)
```

- Enxugar o código.

EX:

```py
# Somando um valor a cada item do array.
lista_nums = [100,200,300,400,500]
# usando a função range
for item in range (5):
	lista_nums [item] += 1000
	print(lista_nums)
```

- Usando a função **len()**.

EX:

```py
# Somando um valor a cada item do array.
lista_nums = [100,200,300,400,500]
# usando a função range
for item in range(len(lista_nums)):
	lista_nums [item] += 1000
	print(lista_nums)
```

- Função enumerate.
- Essa função adiciona um valor numérico a cada valor da lista.

EX:

```py
l = [‘aaa’,’bbb’,’ccc’,’ddd’]
list(enumerate(l))
```

EX:

```py
# Somando um valor a cada item do array.
lista_nums = [100,200,300,400,500]
# usando a função enumerate
for idx, item in enumerate(lista_nums):
	lista_nums [idx] += 1000
	print(lista_nums)
```

## **Fatiando listas**

- Slicing do inglês significa fatiar. Podemos fazer cortes em uma lista a fim de obter uma nova lista.
- Em todas as listas teremos valores positivos e valores negativos.
- Os índices positivos são os que já estávamos trabalhando, os índices negativos devem-se pensar neles com a contagem começando do último elemento da nossa lista, então podemos acessar os índices de uma lista utilizando tanto os índices positivos quanto dos índices negativos

EX:

```py
lista = ‘python’
lista [2::2]
print(lista)
```

EX:

```py
# Lista de trás pra frente
lista = ‘python’
lista [::-1]
print(lista)
```

## **Incluindo, alterando e excluindo elementos**

EX:

```py
lista = [‘aa’, ‘cc’, ‘bb’]
print (lista)

# adiciona um elemento no final do array.
lista.append(‘ee’)

# te dá a opção de escolher em qual posição do array nós queremos inserir um elemento, onde o primeiro elemento indica a posição o segundo seria o elemento em si.
lista.insert(0,’ff’)

# isso nos dá a opção de alterar o elemento na posição desejada.
lista [1] = ‘tt’

# Isso exclui todos os elementos dentro do array.
lista.clear()

# A função pop (), se não for passado nenhum valor ela exclui o elemento da última posição.
lista.pop()

# Se um valor for adicionado ela excluirá o elemento da posição especificada.
lista.pop(3)

# A função del() excluirá os elementos especificados como parâmetros.
del(lista [2:4])
```

## **Ordenamento de listas**

EX:

```py
lista = [‘clau’,’mari’,’jao’,’fula’,’cicla’]

# A função reverse () inverte a ordem do array.
lista.reverse()

# A função sort() ordena o array de forma acendente(ordem alfabética).
Lista.sort()

# Um exemplo com as duas funções.
Lista.sort(reverse=True)
```

## **Array - quantidade de elementos**

EX:

```py
lista = [‘Jose’, ‘clau’,’mari’,’jao’, ‘Jose’,’fula’,’cicla’]

# A função len() retorna o número de elementos em um array.
len(lista)

# A função count() retorna à quantidade de vezes que um elemento se repeti em um array.
lista.count(‘Jose’)

# A função index () retorna à posição do elemento no array.
# Se ocorrer de ter mais de um mesmo elemento dentro do array
# A função index () retorna à primeira ocorrência.
lista.index(‘Jose’)
```

## **Tuplas**

- Estruturas que contempla características e funcionalidades de uma lista, porém, sua estrutura e seus elementos são **ReadOnly** (somente leitura).
- Uma tupla pode conter 0 ou ’n’ elementos de tipos iguais ou distintos.
- No python uma tupla seria uma lista imutável então podemos pensar que uma tupla seria uma lista que restringe adição, alteração ou remoção de elementos, porem pensar em uma tupla como sendo somente em uma lista imutável acabar por ser um erro até porque pensar em uma lista e uma tupla, ainda que semelhantes, não são iguais, sendo assim temos que uma tupla tem as mesmas características que fundamentam as listas.

- Tupla é uma lista declarada como uma constante.

NORMA GERAL:

1. Não seria possível adicionar, remover, alterar elementos.
2. A estrutura e objeto de uma tupla não podem ser alterados. Assim, se definimos o número 10 na posição “1” de uma Tupla, não sera possível alterá-lo.

EX:

```py
t = tuple(“abc”)
print(t)
type(t)
```

## **Operador IN e NOT IN**

- O operador **IN** é para verificar se o objeto está contido.
- O operador **NOT IN** serve para verificar o oposto do operador **IN**.

EX:

```py
# lista
x in […]

# tupla
x in (…)

# dicionário
x in {…}

2 in (1,2,3,4,5)
```

```py
x = range (1,6)
if 3 in x:
	print(“Contido”)
else:
	print (“Não está contido”)
```

EX:

```py
# lista
x not in […]

# tupla
x not in (…)

# dicionário
x not in {…}

6 not in (1,2,3,4,5)
```

```py
x = range (1,6)
if 3 not in x:
	print(“Contido”)
else:
	print (“Não está contido”)
```

## **Operadores AND, OR e IN**

EX:

```py
x and y in […]
x or y in [...]
```

EX:

```py
4 and 3 in range (1, 10)
```

EX:

```py
4 or 3 in range (1, 10)
```

EX:

```py
((1 and 6) or (5 and 6)) in range (1, 10)
```

## **Strings**

- Conjunto de caracteres.
- Strings é qualquer tipo de texto que estiver entre aspas simples ou aspas duplas.

EX:

```py
‘texto – aspas simples’

“texto - aspas duplas”

‘’’texto - 3 aspas simples,
para strings com várias linhas’’’

“”” texto – 3 aspas duplas,
para strings com várias linhas”””
```

## **Fatiando strings**

- Para o python toda string é um conjunto de caracteres imutável, ou seja, não podemos adicionar ou remover uma parte da string.
- Porem, isso não nos impede de manipularmos de diversas maneiras uma string, inclusive, gerar uma nova string que contenha uma determinada alteração.
- Importante que saibamos que o python não vai reaproveitar uma string, então, a partir do momento que não estivermos mais utilizando uma determinada string a mesma sera liberada da memória.

EX:

```py
s = ‘isso é uma string’

print(s)

# se quisermos saber qual carácter está em uma determinada posição, faremos assim.

s [0]

# isso não modifica a string, e sim cria uma outra em outro local da memória.

# da mesma forma que é utilizado em um array pode ser usado aqui.

S [5:11]
```

## **Propriedades das strings**

EX:

```py
s = “Lista de caracteres”
# retorna a quantidade de caracteres.
len(s)
```

EX:

```py
# retorna o carácter especificado.
s [6]
```

EX:

```py
# Isso irá separar a string pelo carácter especificado.
# Nesse caso, espaço em branco.
s.split(“ ”)
```

EX:

```py
# O replace() é uma função que substituí um carácter ou um conjunto de caracteres por outro objeto de caracteres.
s.replace()

s = “Lista de caracteres”
# Nesse caso especificado a string “de” sera substituída pela string ““.
s.replace(“de”, ““)
```

## **Comparando strings**

- O critério usado para comparar duas strings se baseia na tabela ASCI

EX:

```py
# o carácter “a” minúsculo recebe o código 97, enquanto que o carácter “9” recebe o código 57, a comparação abaixo vai ser “True”.
“a” > “9”
```

Ex:

```py
# A função “chr()” ou “ord()” recebe uma letra como parâmetro e retorna o código “ASCI” da mesma.
# isso retorna “d”.
chr (100)

# Isso retorna o inverso de “chr()”.
ord(“d”)
```

## **Iterando strings**

EX:

```py
# Esse exemplo irá imprimir a string ‘s’ letra por letra pulando linha.
s = ‘Iterando Strings’
for c in s:
	print(c)
```

EX:

```py
# Esse exemplo é igual ao primeiro, mas essa ira pôr o valor do índice ao lado da string
s = ‘Iterando string’
indice = 0
while indice < len(s):
	print (indice, s[indice])
	indice+=1
```

EX:

```py
# Esse exemplo é igual ao segundo, irá imprimir o índice e a string mas usando a função “enumerate()”.
s = ‘Iterando string’
for k,v in enumerate (‘Iterando string’):
	print(k,v)
```

## **Introdução aos Dicionários**

- Dicionário é um tipo de lista não ordenada onde cada elemento está associado a uma chave.
- A diferença da lista para o dicionário, nossa responsabilidade a construção e o desenvolvimento do índice, e também com os dicionários no podemos utilizar como índice, qualquer objeto não mutável, ou seja, nós podemos definir que cada item do nosso dicionário tera uma cadeia de caracteres vinculada, logo, para termos acesso a esses itens basta informa a sequência de caracteres desejada, da mesma forma temos a possibilidade de associar um número como índice, ou então, nós podemos definir que alguns elementos terão vinculados um número, outros de uma string e outros de uma tupla, ou seja, nós podemos definir qualquer objeto como sendo a chave de um elemento.
- São comumente chamados de estruturas chave valor.

## **Dicionários na pratica**

- O grande recurso de trabalharmos com dicionários, a capacidade que nós temos de vincular um determinado valor a uma determinada chave que pode ser de qualquer tipo imutável.
  EX:

```py
d1 [‘aaa’] = 1000
d1 [‘bbb’] = 2000
d1 [‘ccc’] = 3000
# Isso imprime um dicionário com três elementos.
print (d1)
```

## **Funções dos dicionários**

EX:

```py
tel = {
	1234567890: “bibi”,
	1987654321: “bobo”,
	1122334455: “bu-bu”,
	1232343454: “da-ad”
	}
tel2 = {99999999: “teu”, 555555555: “beu”}
t = (10,10,10)
print (tel)
print (tel2)

# Retorna o número de elementos
len(del)

# Deleta um elemento do dicionário
del(tel[1234567890])

# Retorna a lista de chaves do dicionário
tel.keys()

# Retorna os valores do dicionário
tel.values()

# retorna o valor associado a chave especificada
tel[1987654321]

# retorna o valor associado a chave especificada
tel.get(1987654321)

# Essa função retorna um elemento aleatoriamente e remove-o do dicionário
tel.popitem()

# Busca a chave especificada dentro do dicionário e retorna um valor booleano
1987654321 in tel

# Adiciona os valores de um dicionário a outro
# Ira adicionar todos os elementos de tel2 em tel
tel.update(tel2)


# os caracteres “junior” serão relacionados a tupla tel
tel[t] = “junior”
```

## **Introdução as funções**

- Funções, são blocos de instruções que pode ser usado em qualquer parte do nosso código, toda função por definição possuí nome como também seria capas de receber uma lista de parâmetros e pode retornar um valor.
- Nem toda função retornara um parâmetro, da mesma forma nem toda função retornara um valor, porem a implementação sempre seguira uma mesma estrutura.
- O que define uma função seria sua capacidade de retorna valores.
  EX:

```py
# toda função em python deve ser precedido da palavra-chave “def”(de definição)
def minha_func():
	print (“holla dev”)
minha_func()
```

## **Parâmetro de funções**

- **Parâmetro** seria uma variável declarada entre os parênteses de uma função.

EX:

```py
def soma (a, b):
	total = a + b
	print (“O total da soma de a mais b: “, total)
soma (10,50)
```

## **Parâmetro default**

- Parâmetros default ou parâmetros pre definidos, são parâmetros que recebem o valor na implementação da função, ou seja, o param entro seria atribuído na função dentro dos parêntesis, os parâmetros default funcionam da mesma forma das inicializações de variáveis, definimos um valor default no momento da declaração, esse recurso faz como que o valor seja omitido quando a função for invocada.

EX:

```py
def login (user=” root”, senha”123”):
	print (“Usuário: “, user)
	print (“senha: “, senha)
login ()
```

## **Argumentos nomeados vs argumentos posicionais**

- O python permite que invoquemos uma função passando os parâmetros de forma posicionada ou de forma nomeada.
- Argumentos posicionais seria o nome utilizado na passagem de valores onde cada valor estará na ordem implementado na função,
  ou seja, os valores devem estar na mesma ordem que os parâmetros são passados na função.
- Argumentos nomeados, seria o recurso que permite a passagem de valores pela associação chave valor, e assim, os mesmos não precisa estar em uma ordem pre estabelecida.
  EX:

```py
def func(param1, param2, param3):
	pass
```

```py
de dados_pessoais(nome, sobrenome, idade, sexo):
	print (“Nome: {} \nSobrenome: {}\nIdade: {}\nSexo: {}”
		.format(nome, sobrenome, idade, sexo))
dados_pessoais(“Alice”, “Carvalho”, 9, false)
```

## **Retorno de valores por função**

- Toda função seria capaz de retorna valor.
- A função **return** seria utilizada tanto para retorna valores como para finalizar a função.

```py
def soma ():
	return 10
soma ()
# Esse programa retornara o valor 10 que foi o valor retornado na função soma ()
print(soma ())
```

```py
def mult(x,y)
	num = x*y
	return num
print(mult(10,20))
```

## **Retorno de valores múltiplos**

- O retorno de múltiplos valores em python seria consequência de definição de linguagem, e não uma implementação propriamente dita.
- O retorno de valores, um conceito simples, porém, faz grande diferença no desenvolvimento. Isso porque, não seria necessário criar explicitamente uma lista, adicionar os valores a serem retornados e por fim retornar a mesma.

```py
def func():
	return 20,30
x,y = func()
```

### Função variaticas

- São funções que podem receber uma quantidade arbitraria de parâmetros
  \_ São funções capaz receber quantidades variadas de parâmetros, ou seja, funções que podem receber 0 ou n quantidade de parâmetros.
- Uma função é capaz de receber quantidade arbitrarias de duas maneiras.

1. A primeira, quando nós passamos uma lista de valores, ou seja, nós enviamos os valores de forma posicional.
2. A segunda maneira é o envio de argumentos associativos. ou seja, argumentos nomeados, quando o nome do parâmetro está associado ao seu valor, logo, temos que essa forma de trabalhar resulta em um dicionário.

- Toda função que irá receber quantidade arbitrarias de parâmetros deverá utilizar uma notação especificada pelo python.

EX:

```py
def func (*args, **kwargs):
	pass
```

EX:

```py
def lista_de_argumentos(*lista):
	print(lista)
lista_de_argumentos(1,2,3,4,5,6)

def lista_de_argumentos_associados(**dicionário):
	print(dicionário)

	lista_de_argumentos_associados(a=1, b=2, c=3, d=4)
	lista_de_argumentos_associados(um=1, dois=2, tres=3, quatro=4)
```
