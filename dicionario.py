d1 = {1: 'valor', 2: 'valor', 3: 'valor real da chave'}

print(d1)

d2 = {
    'str' : 'valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla',
    'nome' : 'Reinaldo Augusto',
}

print('str' in d2)
print('str' in d2.keys())
print('valor' in d2.values())

print(len(d2))

d3 = {
    'chave1' : 'valor1',
    'chave2' : 'valor2',
    'chave3' : 'valor3',
}

for k, v in d3.items():
    print(k, v)

clientes = {
    'cliente1' : {
        'nome' : 'Reinaldo',
        'sobrenome' : 'Augusto',
    },
    'cliente2' : {
        'nome' : 'Renata Mendes',
        'sobrenome' : 'Vilanova',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')


d4 = {
    1: 2,
    3 : 4,
    5 : 6,
}

d5 = {
    'a' : 'b',
    'c' : 'd',
}
d4.update(d5)
print(d4)