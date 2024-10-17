decisao = input('Digite A para alcool ou G para gasolina')
litros = float(input('Litros de combustivel'))
if(decisao == 'A'):
    if(litros <=20):
        desconto = 1.90 - (1.90*0.03) 
        preco = litros * desconto
    else:
        desconto = 1.90 - (1.90*0.05) 
        preco = litros * desconto
elif(decisao == 'G'):
    if litros <= 20:
        desconto = 2.5 - (2.5*0.04) 
        preco = litros * desconto
    else:
        desconto = 2.5 - (1.90*0.06) 
        preco = litros * desconto
print(preco)