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
