##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2014
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Primeira reimpressão - Outubro/2011
# Segunda reimpressão - Novembro/1012
# Terceira reimpressão - Agosto/2013
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Site: http://python.nilo.pro.br/
# 
# Arquivo: capitulo 08\08.05 - Pesquisa em uma lista.py
##############################################################################






def pesquise(lista, valor):
     for x,e in enumerate(lista):
         if e == valor:
               return x
     return None
L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))
