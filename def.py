from pickletools import read_uint1


def divisao(n1, n2):
    if n2 == 0:
        return
        
    return n1 / n2

divide = divisao(8, 2)

if divide:
    print(divide)
else:
    print('Conta Invalida.')

print('***********************')

def saudacao(msg, nome):
    print(msg, nome)

saudacao('Ola', 'Reinaldo')

print('***************************')

def soma(n3, n4, n5):
    return n3 + n4 + n5
calcule = soma(5, 5, 5)
print(calcule)

print('*********************************')

def porcento(m1, m2):
    return m1 * (m2 /100) + m1
porcentagem = porcento(50, 10)
print(porcentagem)

print('******************************')

def numero(x):
    if x % 3 == 0 and x % 5 == 0:
        return f'fizzbuzz, {x} é divisivel por 3 e 5'
    if x % 5 == 0:
        return f'buzz, {x} é divisivel por 5'
    if x % 3 == 0:
        return f'fizz, {x} é divisivel por 3'
    return x

from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(numero(aleatorio))

