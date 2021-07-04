# Criando banco de dados SQLite3 com python.

import sqlite3

# sempre que trabalhar com 'path' usar o 'r' na frente, em qualquer string usar o 'r' na frente.
path = r'C:\Users\junior\OneDrive\Documents\www\python\Curso_de_Python'

conn = sqlite3.connect(path+r'\database.db')

type(conn)
