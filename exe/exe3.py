1 - João quer adicionar mais três frutas novas ao seu sistema.
2 - Ele também deseja aumentar o preço das frutas existentes em 20%
3 - João quer incluir mais 20 produtos de cada.
4 - João vendeu todas as maçãs.'''

x= {
    'maca': 2.40,
    'banana': 3.60,
    'uva': 7.60
}
x.update({'morango':5.90,'pera':4.50})
for k,v in x.items():
    x[k] = v* 1.20

x= {
    'maca': {
        'preco': 20,
        'quantidade':10
    },
    'banana': 3.60,
    'uva': 7.60
}