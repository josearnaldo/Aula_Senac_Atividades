quantidade = int(input("Digite a quantidade de maça"))

if(quantidade <12):
    precototal = quantidade * 0.30
else:
    precototal = quantidade * 0.25

print("O preco total",precototal)