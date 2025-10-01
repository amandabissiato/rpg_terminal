loja={
    'Civic':{
        'preco':15000,
        'cor': 'branco'
},
'Dodge Charger':{
    'preco':20000,
    'cor': 'preto'
  }
}

for k,v in loja.items():
  loja.get(k)['preco']*=1.15
print(loja)