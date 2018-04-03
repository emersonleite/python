# Programa para calcular o n-esimo termo de uma série de Fibonacci
# Ex. 0 1 1 2 3 5 8 13 21 

fibo = 0
f0 = 0
f1 = 1
n = int(input("Entre com o n-esimo da série que quer para a série de Fibonacci:"))
i = 0

while i <= n-3:
    fibo = f0 + f1
    f0 = f1
    f1 = fibo
    i = i + 1
print("O termo ", n , "eh", fibo)