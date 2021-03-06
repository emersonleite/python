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
# Arquivo: capitulo 11\11.23 - Utilizando having para listar apenas as regioes com mais de 5 estados.py
##############################################################################


import sqlite3

print("Região Estados População  Mínima    Máxima      Média    Total (soma)")
print("====== =======          ========= ========== ==========  ============")
with sqlite3.connect("brasil.db") as conexão:
	for região in conexão.execute("""
		select região, count(*), min(população),
		       max(população), avg(população), sum(população) as tpop
		from estados
		group by região
		having count(*)>5
		order by tpop desc"""):
		print("{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}".format(*região))


