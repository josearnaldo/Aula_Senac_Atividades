decisao = 's'
while decisao == 's' or decisao =='S':
    print("1 - Adicionar uma nota")
    print("Para sair qualquer letra ")
    decisao2 = input()
    if(decisao2 == '1'):
       print('Digite a nota')
       nota = float(input())    
       if(nota >10 or nota <0):           
            print('Nota Invalida')
    else:
       decisao = ''
       

