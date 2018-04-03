# De: Emerson Leite. 
# Programa para calcular o n-esimo termo de uma série de Fibonacci
# Ex. 0 1 1 2 3 5 8 13 21 

fibo = 0
f0 = 0
f1 = 1
n = int(input("Entre com o n-esimo da série que quer para a série de Fibonacci:"))
i = 0
lista = []
lista2 = []

lista.append(fibo)
lista.append(f1)

if n == 1:
    fibo
elif n == 2:
    fibo = f1
elif n < 1:
    print("Entre com um número maior que 0, natural...")
else:
    while i <= n-3:
        
        fibo = f0 + f1
        f0 = f1
        f1 = fibo
        i += 1
        lista.append(fibo) # Acrescentando o valor da séria a uma lista
        
        if i >=3:
            
            r = lista[i]
            r1 = lista[i-1]
            razao = r1 / r
            lista2.append(razao)
            
#            r2 = lista2[i]
#            r3 = lista2[i-1]
 #           
  #          if r2 - r3 < 0.000001:
  #             break
                

        
print("O termo ", n , "é", fibo)

print(lista)
print(lista2)

