resposta1 = input('Telefone para a vitima?').capitalize()
resposta2 = input('Esteve no local do crime?').capitalize()
resposta3 = input('Mora perto da vitima?').capitalize()
resposta4 = input('Devia para a vitima?').capitalize()
resposta5 = input('Já trablhou com a vitima').capitalize()
classificacao = 0
if(resposta1 == 'Sim' or resposta1 == 'sim' or resposta1 == 's' or resposta1 == 'S'):
    classificacao = classificacao+1
if(resposta2 == 'Sim' or resposta2 == 'sim' or resposta2 == 's' or resposta2 == 'S'):
    classificacao = classificacao+1
if(resposta3 == 'Sim' or resposta3 == 'sim' or resposta3 == 's' or resposta3 == 'S'):
    classificacao = classificacao+1
if(resposta4 == 'Sim' or resposta4 == 'sim' or resposta4 == 's' or resposta4 == 'S'):
    classificacao = classificacao+1
if(resposta5 == 'Sim' or resposta5 == 'sim' or resposta5 == 's' or resposta5 == 'S'):
    classificacao = classificacao+1

if( classificacao == 2):
    print('Suspeita')
elif( classificacao == 3 or classificacao == 4 ):
    print('Cumplice')
elif(classificacao >= 5):
    print('Assassino')
else:
    print('Inocente')
print(classificacao)